import tkinter as tk

so_lan_bam = 0

def tang_so_lan_bam():
    global so_lan_bam
    so_lan_bam += 1
    nhan_dem.config(text=f"So lan da bam: {so_lan_bam}")

cua_so = tk.Tk()
cua_so.title("Dem so lan bam nut")
cua_so.geometry("350x200")

nhan_dem = tk.Label(cua_so, text="So lan da bam: 0", font=("Arial", 14))
nhan_dem.pack(pady=20)

nut_bam = tk.Button(cua_so, text="Bam vao day", command=tang_so_lan_bam)
nut_bam.pack(pady=10)

cua_so.mainloop()