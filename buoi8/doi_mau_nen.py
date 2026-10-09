import tkinter as tk

danh_sach_mau = ["white", "lightblue", "lightgreen", "lightyellow", "lightpink"]
vi_tri_mau_hien_tai = 0

def doi_mau_nen():
    global vi_tri_mau_hien_tai
    vi_tri_mau_hien_tai = (vi_tri_mau_hien_tai + 1) % len(danh_sach_mau)
    cua_so.configure(bg = danh_sach_mau[vi_tri_mau_hien_tai])

cua_so = tk.Tk()
cua_so.title("Doi mau nen")
cua_so.geometry("350x200")

nut_doi_mau = tk.Button(cua_so, text="Doi mau nen", command=doi_mau_nen)
nut_doi_mau.pack(pady=80)

cua_so.mainloop()