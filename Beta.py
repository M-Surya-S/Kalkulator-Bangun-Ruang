from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Kalkulator Bangun Ruang")
window.setGeometry(400, 50, 500, 400)

lbl_window = QLabel("Mau mengitung apa hari ini?")
lbl_window.setFixedSize(400, 50)
lbl_window.setFont(QFont("Arial", 24))


def buat_tombol(label):
    btn = QPushButton(label, window)
    btn.setFont(QFont("Arial", 11))
    btn.setFixedSize(200, 50)
    return btn


btn_kubus = buat_tombol("Kubus")
btn_balok = buat_tombol("Balok")
btn_prismasgt = buat_tombol("Prisma Segitiga")
btn_limas4 = buat_tombol("Limas Segiempat")
btn_limas = buat_tombol("Limas Segitiga")
btn_tabung = buat_tombol("Tabung")
btn_kerucut = buat_tombol("Kerucut")
btn_bola = buat_tombol("Bola")


def buat_layout(layout):
    lyt = QHBoxLayout()
    lyt.addWidget(layout)
    return lyt


layout_hor1 = buat_layout(lbl_window)
layout_hor2 = buat_layout(btn_kubus)
layout_hor2.addWidget(btn_limas)
layout_hor3 = buat_layout(btn_balok)
layout_hor3.addWidget(btn_tabung)
layout_hor4 = buat_layout(btn_prismasgt)
layout_hor4.addWidget(btn_kerucut)
layout_hor5 = buat_layout(btn_limas4)
layout_hor5.addWidget(btn_bola)

layout_ver = QVBoxLayout()
layout_ver.addLayout(layout_hor1)
layout_ver.addLayout(layout_hor2)
layout_ver.addLayout(layout_hor3)
layout_ver.addLayout(layout_hor4)
layout_ver.addLayout(layout_hor5)

widget = QWidget()
widget.setLayout(layout_ver)
window.setCentralWidget(widget)


def kubus():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 440)
    windbar.setWindowTitle("Kubus")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    sisi = QLabel("Sisi      :", windbar)
    sisi.setFont(QFont("Arial", 13))
    sisi.move(30, 70)
    edit_sisi = QLineEdit(windbar)
    edit_sisi.setFont(QFont("Arial", 13))
    edit_sisi.setFixedSize(200, 40)
    edit_sisi.move(100, 65)
    satuan = QLabel("meter", windbar)
    satuan.setFont(QFont("Arial", 13))
    satuan.move(310, 70)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 120)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 220)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 215)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 220)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 270)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 265)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 270)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 320)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 315)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 320)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 390)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def balok():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 600)
    windbar.setWindowTitle("Balok")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    panjang = QLabel("Panjang  :", windbar)
    panjang.setFont(QFont("Arial", 13))
    panjang.move(30, 70)
    edit_panjang = QLineEdit(windbar)
    edit_panjang.setFont(QFont("Arial", 13))
    edit_panjang.setFixedSize(200, 40)
    edit_panjang.move(110, 65)
    satuan_panjang = QLabel("meter", windbar)
    satuan_panjang.setFont(QFont("Arial", 13))
    satuan_panjang.move(320, 70)

    lebar = QLabel("Lebar     :", windbar)
    lebar.setFont(QFont("Arial", 13))
    lebar.move(30, 130)
    edit_lebar = QLineEdit(windbar)
    edit_lebar.setFont(QFont("Arial", 13))
    edit_lebar.setFixedSize(200, 40)
    edit_lebar.move(110, 125)
    satuan_lebar = QLabel("meter", windbar)
    satuan_lebar.setFont(QFont("Arial", 13))
    satuan_lebar.move(320, 130)

    tinggi = QLabel("Tinggi     :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.move(30, 190)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(110, 185)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(320, 190)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 240)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 310)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 360)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 355)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 360)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 420)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 415)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 420)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 480)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 475)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 480)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 550)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def prisma_segitiga():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 600)
    windbar.setWindowTitle("Prisma Segitiga")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    alas = QLabel("Alas Segitiga    :", windbar)
    alas.setFont(QFont("Arial", 13))
    alas.setFixedWidth(400)
    alas.move(30, 70)
    edit_alas = QLineEdit(windbar)
    edit_alas.setFont(QFont("Arial", 13))
    edit_alas.setFixedSize(200, 40)
    edit_alas.move(160, 65)
    satuan_alas = QLabel("meter", windbar)
    satuan_alas.setFont(QFont("Arial", 13))
    satuan_alas.move(370, 70)

    tinggi_segt = QLabel("Tinggi Segitiga  :", windbar)
    tinggi_segt.setFont(QFont("Arial", 13))
    tinggi_segt.setFixedWidth(400)
    tinggi_segt.move(30, 130)
    edit_tinggi_segt = QLineEdit(windbar)
    edit_tinggi_segt.setFont(QFont("Arial", 13))
    edit_tinggi_segt.setFixedSize(200, 40)
    edit_tinggi_segt.move(160, 125)
    satuan_tinggi_segt = QLabel("meter", windbar)
    satuan_tinggi_segt.setFont(QFont("Arial", 13))
    satuan_tinggi_segt.move(370, 130)

    tinggi = QLabel("Tinggi Prisma    :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 190)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 185)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 190)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 240)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 310)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 360)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 355)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 360)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 420)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 415)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 420)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 480)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 475)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 480)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 550)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def limas_segiempat():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 650)
    windbar.setWindowTitle("Limas Segiempat")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    panjang_alas = QLabel("Panjang Alas     :", windbar)
    panjang_alas.setFont(QFont("Arial", 13))
    panjang_alas.setFixedWidth(400)
    panjang_alas.move(30, 70)
    edit_alas = QLineEdit(windbar)
    edit_alas.setFont(QFont("Arial", 13))
    edit_alas.setFixedSize(200, 40)
    edit_alas.move(160, 65)
    satuan_alas = QLabel("meter", windbar)
    satuan_alas.setFont(QFont("Arial", 13))
    satuan_alas.move(370, 70)

    lebar_alas = QLabel("Lebar Alas        :", windbar)
    lebar_alas.setFont(QFont("Arial", 13))
    lebar_alas.setFixedWidth(400)
    lebar_alas.move(30, 130)
    edit_lebar = QLineEdit(windbar)
    edit_lebar.setFont(QFont("Arial", 13))
    edit_lebar.setFixedSize(200, 40)
    edit_lebar.move(160, 125)
    satuan_lebar = QLabel("meter", windbar)
    satuan_lebar.setFont(QFont("Arial", 13))
    satuan_lebar.move(370, 130)

    tinggi = QLabel("Tinggi Limas     :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 190)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 185)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 190)

    tinggi_sgt = QLabel("Tinggi Segitiga  :", windbar)
    tinggi_sgt.setFont(QFont("Arial", 13))
    tinggi_sgt.setFixedWidth(400)
    tinggi_sgt.move(30, 250)
    edit_tinggi_sgt = QLineEdit(windbar)
    edit_tinggi_sgt.setFont(QFont("Arial", 13))
    edit_tinggi_sgt.setFixedSize(200, 40)
    edit_tinggi_sgt.move(160, 245)
    satuan_tinggi_sgt = QLabel("meter", windbar)
    satuan_tinggi_sgt.setFont(QFont("Arial", 13))
    satuan_tinggi_sgt.move(370, 250)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 300)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 410)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 405)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 410)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 470)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 465)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 470)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 530)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 525)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 530)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 600)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def limas_segitiga():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 650)
    windbar.setWindowTitle("Limas Segitiga")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    panjang_alas = QLabel("Panjang Alas     :", windbar)
    panjang_alas.setFont(QFont("Arial", 13))
    panjang_alas.setFixedWidth(400)
    panjang_alas.move(30, 70)
    edit_alas = QLineEdit(windbar)
    edit_alas.setFont(QFont("Arial", 13))
    edit_alas.setFixedSize(200, 40)
    edit_alas.move(160, 65)
    satuan_alas = QLabel("meter", windbar)
    satuan_alas.setFont(QFont("Arial", 13))
    satuan_alas.move(370, 70)

    lebar_alas = QLabel("Tinggi Alas        :", windbar)
    lebar_alas.setFont(QFont("Arial", 13))
    lebar_alas.setFixedWidth(400)
    lebar_alas.move(30, 130)
    edit_lebar = QLineEdit(windbar)
    edit_lebar.setFont(QFont("Arial", 13))
    edit_lebar.setFixedSize(200, 40)
    edit_lebar.move(160, 125)
    satuan_lebar = QLabel("meter", windbar)
    satuan_lebar.setFont(QFont("Arial", 13))
    satuan_lebar.move(370, 130)

    tinggi = QLabel("Tinggi Limas     :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 190)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 185)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 190)

    tinggi_sgt = QLabel("Tinggi Segitiga  :", windbar)
    tinggi_sgt.setFont(QFont("Arial", 13))
    tinggi_sgt.setFixedWidth(400)
    tinggi_sgt.move(30, 250)
    edit_tinggi_sgt = QLineEdit(windbar)
    edit_tinggi_sgt.setFont(QFont("Arial", 13))
    edit_tinggi_sgt.setFixedSize(200, 40)
    edit_tinggi_sgt.move(160, 245)
    satuan_tinggi_sgt = QLabel("meter", windbar)
    satuan_tinggi_sgt.setFont(QFont("Arial", 13))
    satuan_tinggi_sgt.move(370, 250)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 300)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 410)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 405)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 410)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 470)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 465)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 470)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 530)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 525)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 530)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 600)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def tabung():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 500)
    windbar.setWindowTitle("Tabung")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    jari = QLabel("Jari-jari            :", windbar)
    jari.setFont(QFont("Arial", 13))
    jari.setFixedWidth(400)
    jari.move(30, 70)
    edit_jari = QLineEdit(windbar)
    edit_jari.setFont(QFont("Arial", 13))
    edit_jari.setFixedSize(200, 40)
    edit_jari.move(160, 65)
    satuan_jari = QLabel("meter", windbar)
    satuan_jari.setFont(QFont("Arial", 13))
    satuan_jari.move(370, 70)

    tinggi = QLabel("Tinggi Tabung   :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 130)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 125)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 130)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 180)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 230)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 280)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 275)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 280)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 330)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 325)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 330)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 380)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 375)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 380)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 450)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def kerucut():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 560)
    windbar.setWindowTitle("Kerucut")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    jari = QLabel("Jari-jari            :", windbar)
    jari.setFont(QFont("Arial", 13))
    jari.setFixedWidth(400)
    jari.move(30, 70)
    edit_jari = QLineEdit(windbar)
    edit_jari.setFont(QFont("Arial", 13))
    edit_jari.setFixedSize(200, 40)
    edit_jari.move(160, 65)
    satuan_jari = QLabel("meter", windbar)
    satuan_jari.setFont(QFont("Arial", 13))
    satuan_jari.move(370, 70)

    tinggi = QLabel("Tinggi Kerucut   :", windbar)
    tinggi.setFont(QFont("Arial", 13))
    tinggi.setFixedWidth(400)
    tinggi.move(30, 130)
    edit_tinggi = QLineEdit(windbar)
    edit_tinggi.setFont(QFont("Arial", 13))
    edit_tinggi.setFixedSize(200, 40)
    edit_tinggi.move(160, 125)
    satuan_tinggi = QLabel("meter", windbar)
    satuan_tinggi.setFont(QFont("Arial", 13))
    satuan_tinggi.move(370, 130)

    sisi = QLabel("Sisi Kerucut   :", windbar)
    sisi.setFont(QFont("Arial", 13))
    sisi.setFixedWidth(400)
    sisi.move(30, 190)
    edit_sisi = QLineEdit(windbar)
    edit_sisi.setFont(QFont("Arial", 13))
    edit_sisi.setFixedSize(200, 40)
    edit_sisi.move(160, 185)
    satuan_sisi = QLabel("meter", windbar)
    satuan_sisi.setFont(QFont("Arial", 13))
    satuan_sisi.move(370, 190)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 240)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 290)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 340)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 335)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 340)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 390)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 385)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 390)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 440)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 435)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 440)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 510)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


def bola():
    windbar = QMainWindow(window)
    windbar.setGeometry(400, 50, 500, 440)
    windbar.setWindowTitle("Bola")

    lbl_window = QLabel("Silahkan Masukkan", windbar)
    lbl_window.setFont(QFont("Arial", 18))
    lbl_window.setFixedWidth(400)
    lbl_window.move(30, 20)

    jari = QLabel("Jari-jari  :", windbar)
    jari.setFont(QFont("Arial", 13))
    jari.move(30, 70)
    edit_jari = QLineEdit(windbar)
    edit_jari.setFont(QFont("Arial", 13))
    edit_jari.setFixedSize(200, 40)
    edit_jari.move(110, 65)
    satuan = QLabel("meter", windbar)
    satuan.setFont(QFont("Arial", 13))
    satuan.move(320, 70)

    hitung = QPushButton("Hitung", windbar)
    hitung.move(30, 120)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 220)
    edit_volume = QLineEdit(windbar)
    edit_volume.setReadOnly(True)
    edit_volume.setFont(QFont("Arial", 13))
    edit_volume.setFixedSize(200, 40)
    edit_volume.move(170, 215)
    satuan_v = QLabel("meter^3", windbar)
    satuan_v.setFont(QFont("Arial", 13))
    satuan_v.move(380, 220)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 270)
    edit_lp = QLineEdit(windbar)
    edit_lp.setReadOnly(True)
    edit_lp.setFont(QFont("Arial", 13))
    edit_lp.setFixedSize(200, 40)
    edit_lp.move(170, 265)
    satuan_lp = QLabel("meter", windbar)
    satuan_lp.setFont(QFont("Arial", 13))
    satuan_lp.move(380, 270)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 320)
    edit_keliling = QLineEdit(windbar)
    edit_keliling.setReadOnly(True)
    edit_keliling.setFont(QFont("Arial", 13))
    edit_keliling.setFixedSize(200, 40)
    edit_keliling.move(170, 315)
    satuan_keliling = QLabel("meter", windbar)
    satuan_keliling.setFont(QFont("Arial", 13))
    satuan_keliling.move(380, 320)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 390)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()


btn_kubus.clicked.connect(kubus)
btn_balok.clicked.connect(balok)
btn_prismasgt.clicked.connect(prisma_segitiga)
btn_limas4.clicked.connect(limas_segiempat)
btn_limas.clicked.connect(limas_segitiga)
btn_tabung.clicked.connect(tabung)
btn_kerucut.clicked.connect(kerucut)
btn_bola.clicked.connect(bola)

window.show()
app.exec()
