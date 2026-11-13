import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sanpham.csv")
print("df")
print("-" * 40)

tong_so_sp = len(df)
tong_so_luong_ton = df["SoLuong"].sum()
gia_trung_binh = df["Gia"].mean()

vi_tri_gia_max = df["Gia"].idxmax()
ten_sp_gia_max = df.loc[vi_tri_gia_max, "TenSP"]
gia_max = df.loc[vi_tri_gia_max, "Gia"]

print(f"Tong so mat hang san pham: {tong_so_sp} (Tong so luong ton kho: {tong_so_luong_ton})")
print(f"Gia trung binh cua cac san pham: {gia_trung_binh:,.0f} đ")
print(f"San pham co gia cao nhat: {ten_sp_gia_max} ({gia_max:,.0f} đ)")

plt.figure(figsize=(8, 5))
plt.bar(df["TenSP"], df["SoLuong"], color="steelblue", edgecolor="black")
plt.xlabel("Ten san pham")
plt.ylabel("So luong ton kho")
plt.title("Bieu do ton kho cua tung san pham")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig("bieudo.png")
plt.close()
print("Da luu bieu do thanh cong")

df_sap_het = df[df["SoLuong"] < 10]
df_sap_het.to_csv("canh_bao_hang.csv", index=False, encoding="utf-8")
print("Da xuat cac san pham san het hang")