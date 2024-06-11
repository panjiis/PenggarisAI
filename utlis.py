import cv2
import numpy as np

def getContours(img, cThr=[100, 100], showCanny=False, minArea=1000, filter=0, draw=False):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Mengonversi ke grayscale
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # Menerapkan Gaussian blur
    imgCanny = cv2.Canny(imgBlur, cThr[0], cThr[1])  # Mendeteksi tepi menggunakan Canny
    kernel = np.ones((5, 5))  # Membuat kernel untuk dilasi
    imgDial = cv2.dilate(imgCanny, kernel, iterations=3)  # Melakukan dilasi pada tepi
    imgThre = cv2.erode(imgDial, kernel, iterations=2)  # Melakukan erosi untuk menutup celah
    if showCanny:
        cv2.imshow('Canny', imgThre)  # Menampilkan gambar Canny jika diperlukan
    contours, hiearchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Menemukan kontur
    finalCountours = []
    for i in contours:
        area = cv2.contourArea(i)  # Menghitung area kontur
        if area > minArea:
            peri = cv2.arcLength(i, True)  # Menghitung perimeter
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)  # Mengaproksimasi poligon
            bbox = cv2.boundingRect(approx)  # Mendapatkan bounding box
            if filter > 0:
                if len(approx) == filter:
                    finalCountours.append([len(approx), area, approx, bbox, i])
            else:
                finalCountours.append([len(approx), area, approx, bbox, i])
    finalCountours = sorted(finalCountours, key=lambda x: x[1], reverse=True)  # Mengurutkan kontur berdasarkan area
    if draw:
        for con in finalCountours:
            cv2.drawContours(img, con[4], -1, (0, 0, 255), 3)  # Menggambar kontur akhir jika diperlukan
    return img, finalCountours

def reorder(myPoints):
    myPointsNew = np.zeros_like(myPoints)  # Menginisialisasi array baru
    myPoints = myPoints.reshape((4, 2))  # Mengubah bentuk titik menjadi (4, 2)
    add = myPoints.sum(1)  # Menghitung jumlah titik
    myPointsNew[0] = myPoints[np.argmin(add)]  # Titik kiri atas
    myPointsNew[3] = myPoints[np.argmax(add)]  # Titik kanan bawah
    diff = np.diff(myPoints, axis=1)  # Menghitung perbedaan titik
    myPointsNew[1] = myPoints[np.argmin(diff)]  # Titik kanan atas
    myPointsNew[2] = myPoints[np.argmax(diff)]  # Titik kiri bawah
    return myPointsNew

def warpImg(img, points, w, h, pad=20):
    points = reorder(points)  # Mengurutkan titik
    pts1 = np.float32(points)  # Mengonversi ke float32
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])  # Titik tujuan
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # Mendapatkan matriks transformasi perspektif
    imgWarp = cv2.warpPerspective(img, matrix, (w, h))  # Menerapkan warp perspektif
    imgWarp = imgWarp[pad:imgWarp.shape[0] - pad, pad:imgWarp.shape[1] - pad]  # Memotong tepi yang diberi padding
    return imgWarp

def findDis(pts1, pts2):
    return ((pts2[0] - pts1[0]) ** 2 + (pts2[1] - pts1[1]) ** 2) ** 0.5  # Menghitung jarak Euclidean
