import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form_dang_nhap.ui", self)

        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)
    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du thong tin tai khoan va mat khau")
            return

        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

app = QApplication(sys.argv)
cua_so = CuaSoDangNhap()
cua_so.show()
sys.exit(app.exec_())