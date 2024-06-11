import cv2
import utlis

###################################
webcam = True
path = '1.jpg'
cap = cv2.VideoCapture(1)
cap.set(10, 160) #Mengatur brightness kamera
cap.set(3, 1920) #Mengatur lebar frame video
cap.set(4, 1080) #Mengatur tinggi frame video
scale = 3
wP = 297 * scale
hP = 210 * scale
###################################

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    # mendapatkan kontur dari gambar dengan area minimum 50.000 pixels dan filter untuk kontur dengan 4 sisi
    imgContours, conts = utlis.getContours(img, minArea=50000, filter=4)
    if len(conts) != 0:
        biggest = conts[0][2]
        # Melakukan perspektif transformasi (warp) pada gambar berdasarkan kontur terbesar
        imgWarp = utlis.warpImg(img, biggest, wP, hP)

        # Mencari kontur pada gambar yang sudah di-warp dengan area minimum 2000 dan filter 4 sisi
        imgContours2, conts2 = utlis.getContours(imgWarp,
                                                 minArea=2000, filter=4,
                                                 cThr=[50, 50], draw=False)

        # Jika kontur ditemukan pada gambar yang di-warp (len(conts2) != 0), maka setiap kontur diproses
        if len(conts) != 0:
            for obj in conts2:
                # Menggambar kontur dengan garis hijau.
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                # Mengurutkan titik-titik kontur.
                nPoints = utlis.reorder(obj[2])

                # Menghitung lebar dan tinggi objek dalam cm berdasarkan jarak antar titik kontur yang di-skalakan
                nW = round(
                    (utlis.findDis(nPoints[0][0]//scale, nPoints[1][0]//scale)/10), 1)
                nH = round(
                    (utlis.findDis(nPoints[0][0]//scale, nPoints[2][0]//scale)/10), 1)

                # Menggambarkan garis panah
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]

                # Menambahkan teks yang menunjukkan ukuran objek (lebar dan tinggi) dalam cm.
                cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
        # Menampilkan gambar yang telah diproses dengan nama jendela 'A4'
        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img, (0, 0), None, 0.5, 0.5) #Mengubah ukuran gambar asli menjadi setengah dari ukuran aslinya
    cv2.imshow('Original', img) #Menampilkan gambar asli yang telah diubah ukurannya dengan nama 'Original'
    cv2.waitKey(1) #Menunggu selama 1 ms untuk menampilkan frame berikutnya
