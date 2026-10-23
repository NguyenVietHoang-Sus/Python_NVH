import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout, QLineEdit
)

class FormThongTin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vi du widget co ban")
        self.resize(320, 250)

        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("Nhap ho ten...")

        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems(["Ha Noi", "Da Nang", "TP.HCM", "Hue"])

        nut_xac_nhan = QPushButton("Xac nhan")
        self.nhan_ket_qua = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ho ten:"))
        layout.addWidget(self.o_nhap_ten)
        layout.addWidget(QLabel("Thanh pho:"))
        layout.addWidget(self.chon_thanh_pho)
        layout.addWidget(nut_xac_nhan)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        nut_xac_nhan.clicked.connect(self.xu_ly_xac_nhan)
    def xu_ly_xac_nhan(self):
        ten = self.o_nhap_ten.text()
        thanh_pho = self.chon_thanh_pho.currentText()
        self.nhan_ket_qua.setText(f"Xin chao {ten}, den tu {thanh_pho}")

app = QApplication(sys.argv)
cua_so = FormThongTin()
cua_so.show()
sys.exit(app.exec_())