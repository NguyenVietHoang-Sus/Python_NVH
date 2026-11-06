import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_sinh_vien as db

DANH_SACH_LOP = ["CNTT1", "CNTT2", "DTVT1", "KTPM1", "HTTT1"]


class UngDungSinhVien(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Quản lý Sinh viên")
        self.geometry("680x580")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sinh_vien()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(
            self, text="Thông tin sinh viên", padx=10, pady=10
        )
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Mã sinh viên:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.o_nhap_ma_sv = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Họ và tên:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.o_nhap_ho_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Lớp:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.chon_lop = ttk.Combobox(
            khung_nhap, values=DANH_SACH_LOP, width=28, state="readonly"
        )
        self.chon_lop.current(0)
        self.chon_lop.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Điểm GPA:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.o_nhap_diem_gpa = tk.Entry(khung_nhap, width=30)
        self.o_nhap_diem_gpa.grid(row=3, column=1, padx=10, pady=5)

        khung_nut_form = tk.Frame(khung_nhap)
        khung_nut_form.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(
            khung_nut_form,
            text="Thêm sinh viên",
            command=self.xu_ly_them_sinh_vien,
            width=15,
        ).pack(side="left", padx=5)
        tk.Button(
            khung_nut_form,
            text="Cập nhật",
            command=self.xu_ly_cap_nhat_sinh_vien,
            width=15,
        ).pack(side="left", padx=5)
        tk.Button(
            khung_nut_form,
            text="Làm mới form",
            command=self.xoa_trang_o_nhap,
            width=12,
        ).pack(side="left", padx=5)

        khung_danh_sach = tk.LabelFrame(
            self, text="Danh sách sinh viên", padx=10, pady=5
        )
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        cot = ("id", "ma_sv", "ho_ten", "lop", "diem_gpa")
        self.bang_sinh_vien = ttk.Treeview(
            khung_danh_sach, columns=cot, show="headings", height=10
        )

        self.bang_sinh_vien.heading("id", text="ID")
        self.bang_sinh_vien.column("id", width=50, anchor="center")
        self.bang_sinh_vien.heading("ma_sv", text="Mã SV")
        self.bang_sinh_vien.column("ma_sv", width=100, anchor="center")
        self.bang_sinh_vien.heading("ho_ten", text="Họ và tên")
        self.bang_sinh_vien.column("ho_ten", width=220, anchor="w")
        self.bang_sinh_vien.heading("lop", text="Lớp")
        self.bang_sinh_vien.column("lop", width=100, anchor="center")
        self.bang_sinh_vien.heading("diem_gpa", text="Điểm GPA")
        self.bang_sinh_vien.column("diem_gpa", width=80, anchor="center")

        thanh_cuon = tk.Scrollbar(
            khung_danh_sach,
            orient="vertical",
            command=self.bang_sinh_vien.yview,
        )
        self.bang_sinh_vien.configure(yscrollcommand=thanh_cuon.set)

        self.bang_sinh_vien.pack(side="left", fill="both", expand=True)
        thanh_cuon.pack(side="right", fill="y")

        self.bang_sinh_vien.bind(
            "<<TreeviewSelect>>", self.khi_chon_dong_sinh_vien
        )

        khung_nut_duoi = tk.Frame(self)
        khung_nut_duoi.pack(pady=10)

        tk.Button(
            khung_nut_duoi,
            text="Xóa sinh viên",
            command=self.xu_ly_xoa_sinh_vien,
            width=15,
        ).pack(side="left", padx=10)
        tk.Button(
            khung_nut_duoi,
            text="Thống kê theo lớp",
            command=self.xu_ly_thong_ke,
            width=20,
        ).pack(side="left", padx=10)

    def xoa_trang_o_nhap(self):
        self.o_nhap_ma_sv.delete(0, tk.END)
        self.o_nhap_ho_ten.delete(0, tk.END)
        self.o_nhap_diem_gpa.delete(0, tk.END)
        self.chon_lop.current(0)
        # Bỏ chọn trên bảng nếu đang chọn
        if self.bang_sinh_vien.selection():
            self.bang_sinh_vien.selection_remove(
                self.bang_sinh_vien.selection()
            )

    def tai_lai_danh_sach_sinh_vien(self):
        for item in self.bang_sinh_vien.get_children():
            self.bang_sinh_vien.delete(item)

        self.danh_sach_hien_tai = db.lay_toan_bo_sinh_vien()
        for sv in self.danh_sach_hien_tai:
            self.bang_sinh_vien.insert("", tk.END, values=sv)

    def khi_chon_dong_sinh_vien(self, event):
        lua_chon = self.bang_sinh_vien.selection()
        if not lua_chon:
            return

        gia_tri = self.bang_sinh_vien.item(lua_chon[0], "values")
        self.o_nhap_ma_sv.delete(0, tk.END)
        self.o_nhap_ma_sv.insert(0, gia_tri[1])

        self.o_nhap_ho_ten.delete(0, tk.END)
        self.o_nhap_ho_ten.insert(0, gia_tri[2])

        if gia_tri[3] in DANH_SACH_LOP:
            self.chon_lop.set(gia_tri[3])

        self.o_nhap_diem_gpa.delete(0, tk.END)
        self.o_nhap_diem_gpa.insert(0, gia_tri[4])

    def xu_ly_them_sinh_vien(self):
        ma_sv = self.o_nhap_ma_sv.get().strip()
        ho_ten = self.o_nhap_ho_ten.get().strip()
        lop = self.chon_lop.get()
        diem_gpa_str = self.o_nhap_diem_gpa.get().strip()

        if ma_sv == "" or ho_ten == "" or diem_gpa_str == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tất cả thông tin.")
            return

        try:
            diem_gpa = float(diem_gpa_str)
            if not (0.0 <= diem_gpa <= 10.0):
                messagebox.showerror(
                    "Lỗi", "Điểm GPA phải nằm trong thang điểm từ 0.0 đến 10.0."
                )
                return
        except ValueError:
            messagebox.showerror(
                "Lỗi", "Điểm GPA phải là một số thực hợp lệ (ví dụ: 8.5)."
            )
            return

        try:
            db.them_sinh_vien(ma_sv, ho_ten, lop, diem_gpa)
            self.tai_lai_danh_sach_sinh_vien()
            self.xoa_trang_o_nhap()
            messagebox.showinfo(
                "Thành công", f"Đã thêm sinh viên: {ho_ten} ({ma_sv})"
            )
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Lỗi", f"Mã sinh viên '{ma_sv}' đã tồn tại trong hệ thống."
            )

    def xu_ly_cap_nhat_sinh_vien(self):
        lua_chon = self.bang_sinh_vien.selection()
        if not lua_chon:
            messagebox.showerror(
                "Lỗi", "Vui lòng chọn một sinh viên trong danh sách để cập nhật."
            )
            return

        id_sv = self.bang_sinh_vien.item(lua_chon[0], "values")[0]
        ma_sv = self.o_nhap_ma_sv.get().strip()
        ho_ten = self.o_nhap_ho_ten.get().strip()
        lop = self.chon_lop.get()
        diem_gpa_str = self.o_nhap_diem_gpa.get().strip()

        if ma_sv == "" or ho_ten == "" or diem_gpa_str == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            diem_gpa = float(diem_gpa_str)
            if not (0.0 <= diem_gpa <= 10.0):
                messagebox.showerror(
                    "Lỗi", "Điểm GPA phải nằm trong khoảng 0.0 - 10.0."
                )
                return
        except ValueError:
            messagebox.showerror("Lỗi", "Điểm GPA phải là số thực hợp lệ.")
            return

        try:
            db.cap_nhat_sinh_vien(id_sv, ma_sv, ho_ten, lop, diem_gpa)
            self.tai_lai_danh_sach_sinh_vien()
            self.xoa_trang_o_nhap()
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin sinh viên.")
        except sqlite3.IntegrityError:
            messagebox.showerror(
                "Lỗi", f"Mã sinh viên '{ma_sv}' bị trùng với sinh viên khác."
            )

    def xu_ly_xoa_sinh_vien(self):
        lua_chon = self.bang_sinh_vien.selection()
        if not lua_chon:
            messagebox.showerror(
                "Lỗi", "Vui lòng chọn một sinh viên trong danh sách để xóa."
            )
            return

        sv = self.bang_sinh_vien.item(lua_chon[0], "values")
        id_sv, ma_sv, ho_ten = sv[0], sv[1], sv[2]

        xac_nhan = messagebox.askyesno(
            "Xác nhận", f"Bạn có chắc chắn muốn xóa sinh viên {ho_ten} ({ma_sv})?"
        )
        if xac_nhan:
            db.xoa_sinh_vien(id_sv)
            self.tai_lai_danh_sach_sinh_vien()
            self.xoa_trang_o_nhap()
            messagebox.showinfo("Thành công", "Đã xóa sinh viên thành công.")

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_lop()
        if not du_lieu_thong_ke:
            messagebox.showinfo(
                "Thông báo", "Chưa có dữ liệu sinh viên để thống kê."
            )
            return

        cac_lop = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_lop, so_luong, color="cornflowerblue")
        plt.title("Số lượng sinh viên theo lớp")
        plt.xlabel("Lớp")
        plt.ylabel("Số lượng sinh viên")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungSinhVien()
    ung_dung.mainloop()