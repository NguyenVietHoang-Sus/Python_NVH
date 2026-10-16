import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi - Nguyễn Việt Hoàng - 2411060369")
cua_so.geometry("400x250")

bieu_thuc = tk.StringVar(value="")

o_hien_thi = tk.Entry(cua_so, textvariable=bieu_thuc, font=("Arial", 24), justify="right")
o_hien_thi.grid(row=0, column=0, columnspan=4, sticky="nsew")


def nhan_nut(gia_tri):
    chuoi_hien_tai = bieu_thuc.get()
    bieu_thuc.set(chuoi_hien_tai + str(gia_tri))


def tinh_toan():
    try:
        ket_qua = str(eval(bieu_thuc.get()))
        bieu_thuc.set(ket_qua)
    except Exception:
        bieu_thuc.set("Lỗi")

def xoa():
    bieu_thuc.set("")

cac_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (nhan, hang, cot) in cac_nut:
    if nhan == '=':
        btn = tk.Button(cua_so, text=nhan, font=("Arial", 16), command=tinh_toan)
    elif nhan == 'C':
        btn = tk.Button(cua_so, text=nhan, font=("Arial", 16), command=xoa)
    else:
        btn = tk.Button(cua_so, text=nhan, font=("Arial", 16), command=lambda t=nhan: nhan_nut(t))

    btn.grid(row=hang, column=cot, sticky="nsew", padx=2, pady=2)

cua_so.mainloop()