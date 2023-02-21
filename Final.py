from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Kalkulator Bangun Ruang")
# window.setStyleSheet("background-color: yellow;")
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
btn_prismasgt = buat_tombol("Prisma Segitiga Sama Sisi")
btn_limas4 = buat_tombol("Limas Segiempat")
btn_limas = buat_tombol("Limas Segitiga Sama Sisi")
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

    def total():
        try:
            s = float(edit_sisi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = (s*s*s)*30/100
            lupe = 6 * s**2
            k = 12 * s

            volume.setText(f"Volume               : {v} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m^2")
            keliling.setText(f"Keliling               : {k} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 220)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 270)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 320)

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

    def total():
        try:
            p = float(edit_panjang.text())
            l = float(edit_lebar.text())
            t = float(edit_tinggi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = p * l * t
            lupe = 2*(p*l + l*t + p*t)
            k = 4*(p + l + t)

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 310)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 360)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 420)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 480)

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
    windbar.setWindowTitle("Prisma Segitiga Sama Sisi")

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

    def total():
        try:
            a = float(edit_alas.text())
            ts = float(edit_tinggi_segt.text())
            tp = float(edit_tinggi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = ((a * ts) / 2) * tp
            lupe = ((a * ts) / 2) + ((a * 3) + tp)
            k = (2*(a*3)) + tp * 3

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 310)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 360)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 420)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 480)

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

    def total():
        try:
            pa = float(edit_alas.text())
            la = float(edit_lebar.text())
            tl = float(edit_tinggi.text())
            ts = float(edit_tinggi_sgt.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            rt_p = math.sqrt((1/2*pa)**2 + ts**2)
            rt_l = math.sqrt((1/2*la)**2 + ts**2)

            v = 1/3 * (pa*la) * tl
            lupe = (pa*la) + 2*(1/2 * pa*ts) + 2*(1/2 * la*ts)
            k = 2*(pa + la) + 2*rt_p + 2*rt_l

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 410)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 470)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 530)

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
    windbar.setWindowTitle("Limas Segitiga Sama Sisi")

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

    tinggi_alas = QLabel("Tinggi Alas        :", windbar)
    tinggi_alas.setFont(QFont("Arial", 13))
    tinggi_alas.setFixedWidth(400)
    tinggi_alas.move(30, 130)
    edit_tinggi_alas = QLineEdit(windbar)
    edit_tinggi_alas.setFont(QFont("Arial", 13))
    edit_tinggi_alas.setFixedSize(200, 40)
    edit_tinggi_alas.move(160, 125)
    satuan_tinggi_alas = QLabel("meter", windbar)
    satuan_tinggi_alas.setFont(QFont("Arial", 13))
    satuan_tinggi_alas.move(370, 130)

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

    def total():
        try:
            a = float(edit_alas.text())
            ta = float(edit_tinggi_alas.text())
            tl = float(edit_tinggi.text())
            ts = float(edit_tinggi_sgt.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            rt_l = math.sqrt((1/2 * a)**2 + ts**2)

            v = 1/3 * (1/2 * a * ta) * tl
            lupe = (1/2 * a * ta) + (3*(1/2 * a * ts))
            k = (3 * a) + (3 * rt_l)

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 360)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 410)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 470)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 530)

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

    def total():
        try:
            r = float(edit_jari.text())
            t = float(edit_tinggi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = 3.14 * r**2 * t
            lupe = 2 * 3.14 * r * (r + t)
            k = 2 * 3.14 * r

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 230)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 280)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 330)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 380)

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

    def total():
        try:
            r = float(edit_jari.text())
            t = float(edit_tinggi.text())
            s = float(edit_sisi.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = 1/3 * 3.14 * r**2 * t
            lupe = 3.14 * r * (s * r)
            k = 2 * 3.14 * r

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling Alas        : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 290)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 340)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 390)

    keliling = QLabel("Keliling Alas        :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 440)

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

    def total():
        try:
            r = float(edit_jari.text())

        except ValueError:
            notif = QMessageBox.about(
                windbar, "Error", "Harap masukkan angka saja!!")

        else:
            v = 4/3 * 3.14 * r**3
            lupe = 4 * 3.14 * r**2
            k = 4/3 * 3.14 * r**2

            volume.setText(f"Volume               : {v:.3f} m^3")
            lp.setText(f"Luas Permukaan : {lupe:.3f} m")
            keliling.setText(f"Keliling               : {k:.3f} m")

    hitung.clicked.connect(total)

    lbl_hasil = QLabel("Hasil", windbar)
    lbl_hasil.setFont(QFont("Arial", 18))
    lbl_hasil.setFixedWidth(400)
    lbl_hasil.move(28, 170)

    volume = QLabel("Volume               :", windbar)
    volume.setFont(QFont("Arial", 13))
    volume.setFixedWidth(400)
    volume.move(30, 220)

    lp = QLabel("Luas Permukaan :", windbar)
    lp.setFont(QFont("Arial", 13))
    lp.setFixedWidth(400)
    lp.move(30, 270)

    keliling = QLabel("Keliling               :", windbar)
    keliling.setFont(QFont("Arial", 13))
    keliling.setFixedWidth(400)
    keliling.move(30, 320)

    kembali = QPushButton("Kembali", windbar)
    kembali.move(30, 390)

    def tombol_kembali():
        window.show()
        windbar.hide()

    kembali.clicked.connect(tombol_kembali)

    window.hide()
    windbar.show()

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
