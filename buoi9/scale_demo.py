import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du scale")
cua_so.geometry("300x180")

def khi_keo_thanh_truot(gia_tri):
    nhan_gia_tri.config(text=f"Gia tri hien tai: {gia_tri}")

thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal",
command = khi_keo_thanh_truot)
thanh_truot.pack(pady=20, padx=20, fill="x")
nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0")
nhan_gia_tri.pack()

cua_so.mainloop()