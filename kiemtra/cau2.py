import tkinter as tk
from tkinter import messagebox

ds_san_pham = [
    {"MaSP": "SP001", "TenSP": "Bút bi Thiên Long", "Gia": 3000, "SoLuong": 150},
    {"MaSP": "SP002", "TenSP": "Vở học sinh 96 trang", "Gia": 8000, "SoLuong": 8},
    {"MaSP": "SP003", "TenSP": "Bút chì 2B", "Gia": 2500, "SoLuong": 200}
]

def cap_nhat_listbox(danh_sach):
    listbox_sp.delete(0, tk.END)
    for sp in danh_sach:
        dong_hien_thi = f"{sp['MaSP']} - {sp['TenSP']} - {sp['Gia']}đ - SL: {sp['SoLuong']}"
        listbox_sp.insert(tk.END, dong_hien_thi)

def xu_ly_them():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia_str = entry_gia.get().strip()
    sl_str = entry_sl.get().strip()

    if not ma or not ten:
        messagebox.showerror("Loi", "MaSP va TenSP khong duoc de trong")
        return

    try:
        gia = int(gia_str)
        soluong = int(sl_str)
        if gia < 0 or soluong < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Loi", "Gia va so luong phai lon hon 0")
        return

    sp_moi = {"MaSP": ma, "TenSP": ten, "Gia": gia, "SoLuong": soluong}
    ds_san_pham.append(sp_moi)
    cap_nhat_listbox(ds_san_pham)

    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_sl.delete(0, tk.END)

def xu_ly_tim_kiem():
    tu_khoa = entry_tim.get().strip().lower()
    ket_qua = [sp for sp in ds_san_pham if tu_khoa in sp["TenSP"].lower()]
    cap_nhat_listbox(ket_qua)

root = tk.Tk()
root.title("Cau 2")
root.geometry("500x450")

frame_form = tk.LabelFrame(root, text="Thong tin san pham", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=5)

tk.Label(frame_form, text="Ma SP:").grid(row=0, column=0, sticky="w", pady=3)
entry_ma = tk.Entry(frame_form, width=35)
entry_ma.grid(row=0, column=1, padx=5, pady=3)

tk.Label(frame_form, text="Ten SP:").grid(row=1, column=0, sticky="w", pady=3)
entry_ten = tk.Entry(frame_form, width=35)
entry_ten.grid(row=1, column=1, padx=5, pady=3)

tk.Label(frame_form, text="Gia:").grid(row=2, column=0, sticky="w", pady=3)
entry_gia = tk.Entry(frame_form, width=35)
entry_gia.grid(row=2, column=1, padx=5, pady=3)

tk.Label(frame_form, text="So luong:").grid(row=3, column=0, sticky="w", pady=3)
entry_sl = tk.Entry(frame_form, width=35)
entry_sl.grid(row=3, column=1, padx=5, pady=3)

btn_them = tk.Button(frame_form, text="Them san pham", command=xu_ly_them)
btn_them.grid(row=4, column=0, columnspan=2, pady=8)

# --- Ý c: Khu vực tìm kiếm ---
frame_tim = tk.Frame(root, padx=10, pady=5)
frame_tim.pack(fill="x")

tk.Label(frame_tim, text="Tu khoa tim kiem:").pack(side="left")
entry_tim = tk.Entry(frame_tim, width=25)
entry_tim.pack(side="left", padx=5)
btn_tim = tk.Button(frame_tim, text="Tim kiem", command=xu_ly_tim_kiem)
btn_tim.pack(side="left", padx=2)
btn_hien_tat_ca = tk.Button(frame_tim, text="Hien tat ca", command=lambda: cap_nhat_listbox(ds_san_pham))
btn_hien_tat_ca.pack(side="left", padx=2)

# --- Vùng hiển thị danh sách sản phẩm ---
frame_ds = tk.LabelFrame(root, text="Danh sach san pham", padx=10, pady=10)
frame_ds.pack(fill="both", expand=True, padx=10, pady=5)

listbox_sp = tk.Listbox(frame_ds, font=("Arial", 10))
listbox_sp.pack(fill="both", expand=True)

# Hiển thị dữ liệu mẫu lúc mới mở app
cap_nhat_listbox(ds_san_pham)

root.mainloop()