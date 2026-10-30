import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diem_sinh_vien.csv")
"""
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

plt.figure(figsize = (6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.savefig("bieu_do_cot.png")
plt.show()
"""
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize = (6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")
plt.savefig("bieu_do_duong.png")
plt.show()