# 1.1
print("Bai-1.1")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
print(diem_so[0]) # phan tu dau tien
print(diem_so[-1]) # phan tu cuoi cung
print(diem_so[1:4]) # cat tu vi tri 1 den truoc 4
print(diem_so[::2]) # lay cach 1 phan tu (step = 2)
print(diem_so[::-1]) # dao nguoc danh sach

# 1.2
print("\nBai-1.2")
ten_sv = ["An", "Binh", "Chi"]
ten_sv.append("Dung") # them vao cuoi
ten_sv.insert(1, "Em") # chen vao vi tri 1
print(ten_sv)
ten_sv.remove("Chi") # xoa theo gia tri
pop_ra = ten_sv.pop() # xoa va lay ra phan tu cuoi
print(ten_sv, "- da xoa:", pop_ra)
ten_sv.sort() # sap xep tang dan (theo bang chu cai)
print(ten_sv)
ten_sv.reverse() # dao nguoc thu tu hien tai
print(ten_sv)
ten_sv.extend(["Giang", "Hoa"]) # noi them mot list khac vao
print(ten_sv)

# 2.1
print("\nBai-2.1")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
tong = 0
for diem in diem_so:
    print(diem)
    tong = tong + diem
print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))

# 2.2
print("\nBai-2.2")
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# In ra theo tung hang
for hang in ma_tran:
    print(hang)
# In ra tung phan tu, duyet theo hang roi theo cot
tong1 = 0
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
        tong1 = tong1 + phan_tu
    print()
print("Tổng các phần tử trong ma trận là: ", tong1)

# 3.1
print("\nBai-3.1")
day_so = list(range(1, 21)) # day so tu 1 den 20
so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]
print("So chan:", so_chan)
print("So le:", so_le)

# 3.2
print("\nBai-3.2")
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_cong = [round(diem + 0.5, 2) for diem in diem_so]
print(diem_cong)