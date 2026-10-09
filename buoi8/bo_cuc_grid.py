import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bo cuc bang grid()")
cua_so.geometry("300x250")

tk.Label(cua_so, text="Ho_ten:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Button(cua_so, text="Dong y").grid(row=3, column=0, padx=10, pady=15)
tk.Button(cua_so, text="Huy").grid(row=3, column=1, padx=10, pady=15)

cua_so.mainloop()