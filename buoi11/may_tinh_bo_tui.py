import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính bỏ túi - Nguyễn Việt Hoàng - 2411060369")
        self.resize(400, 300)

        self.o_hien_thi = QLineEdit()
        self.o_hien_thi.setFont(QFont("Arial", 20))
        self.o_hien_thi.setAlignment(Qt.AlignRight)
        self.o_hien_thi.setReadOnly(True)

        luoi_nut = QGridLayout()

        cac_nut = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        font_nut = QFont("Arial", 14)

        for nhan, hang, cot in cac_nut:
            btn = QPushButton(nhan)
            btn.setFont(font_nut)
            btn.setFixedHeight(45)

            if nhan == '=':
                btn.clicked.connect(self.tinh_toan)
            elif nhan == 'C':
                btn.clicked.connect(self.xoa)
            else:
                btn.clicked.connect(lambda checked=False, t=nhan: self.nhan_nut(t))

            luoi_nut.addWidget(btn, hang, cot)

        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.o_hien_thi)
        layout_chinh.addLayout(luoi_nut)
        self.setLayout(layout_chinh)

    def nhan_nut(self, gia_tri):
        chuoi_hien_tai = self.o_hien_thi.text()
        if chuoi_hien_tai == "Lỗi":
            chuoi_hien_tai = ""
        self.o_hien_thi.setText(chuoi_hien_tai + str(gia_tri))

    def tinh_toan(self):
        try:
            bieu_thuc = self.o_hien_thi.text()
            if bieu_thuc:
                ket_qua = str(eval(bieu_thuc))
                self.o_hien_thi.setText(ket_qua)
        except Exception:
            self.o_hien_thi.setText("Lỗi")

    def xoa(self):
        self.o_hien_thi.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())

