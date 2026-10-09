import tkinter as tk

def khi_go_phim(event):
    nhan_thong_bao.config(text=f"Ban vua nhan phim: {event.char}")

def khi_click_chuot(event):
    nhan_thong_bao.config(text=f"Ban vua click tai toa do: ({event.x}, {event.y})")

cua_so = tk.Tk()
cua_so.title("Vi du bind()")
cua_so.geometry("350x200")

nhan_thong_bao = tk.Label(cua_so, text="Hay go phim hoac click chuot", font=("Arial", 12))
nhan_thong_bao.pack(pady=30)

cua_so.bind("<Key>", khi_go_phim)
cua_so.bind("<Button-1>", khi_click_chuot)

cua_so.mainloop()