# PenggarisAI

## Anggota
| Nama Anggota | NPM |
| Panji Iman Sujatmiko | 140810220011 |
| Vernandika Stanley Hansen | 140810220031 |
| Darren Christian Liharja | 140810220043 |
| Leonardo Louis | 140810220049 |
| Jason Natanael Krisyanto | 140810220051 |

## Latar Belakang
Dalam era teknologi digital yang terus berkembang, kebutuhan akan aplikasi yang dapat menganalisis dan memproses informasi visual semakin meningkat. Salah satu bidang yang sedang mengalami pertumbuhan pesat adalah computer vision, yaitu cabang kecerdasan buatan yang memungkinkan komputer untuk memperoleh, menginterpretasikan, dan memahami informasi dari gambar atau video. Teknologi ini telah menemukan berbagai aplikasi dalam industri, kesehatan, keamanan, dan banyak bidang lainnya.

Salah satu aplikasi penting dari computer vision adalah pengukuran panjang objek. Kemampuan untuk mengukur panjang suatu objek dari gambar atau video secara otomatis memiliki berbagai manfaat dan dapat diterapkan dalam berbagai konteks. Misalnya, dalam bidang manufaktur, pengukuran otomatis dapat meningkatkan efisiensi dan akurasi proses produksi. Dalam sektor kesehatan, teknologi ini dapat digunakan untuk analisis medis, seperti mengukur panjang luka atau bagian tubuh tertentu untuk tujuan diagnosis dan perawatan.

Namun, pengukuran panjang objek secara otomatis melalui gambar atau video bukanlah tugas yang sederhana. Hal ini memerlukan pengembangan algoritma yang mampu mendeteksi objek, mengidentifikasi batas-batasnya, dan mengukur panjangnya dengan presisi tinggi. Beberapa tantangan utama dalam pengembangan sistem ini meliputi variasi dalam pencahayaan, orientasi objek, serta gangguan latar belakang yang dapat mempengaruhi akurasi pengukuran.

Proyek ini dirancang untuk mengukur objek secara real-time menggunakan webcam. Proyek ini memanfaatkan OpenCV, yakni library Computer Vision dan pembelajaran Machine Learning open-source, untuk mendeteksi dan mengukur kontur dalam gambar. Tujuan utamanya adalah mengidentifikasi kontur terbesar dalam frame dan menghitung dimensi objek tersebut dalam ukuran centimeter.

## Tujuan
1. Menggunakan webcam untuk mendapatkan gambar secara real-time.
2. Mendapatkan kontur dari gambar yang memiliki area minimum 50.000 piksel dan memfilter kontur dengan 4 sisi (segi empat)
3. Melakukan transformasi perspektif (warp) pada gambar berdasarkan kontur terbesar yang ditemukan.
4. Mencari kontur pada gambar yang telah di-warp dengan area minimum 2000 piksel.
5. Mengukur lebar dan tinggi objek dalam sentimeter berdasarkan jarak antar titik kontur.
6. Menampilkan gambar yang diproses dan gambar asli yang telah diubah ukurannya.
