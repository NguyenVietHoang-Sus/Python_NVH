# hoat dong 3
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)

# hoat dong 5

# 5.1
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# 5.2
diem = 6.5
tuoi = 20

kiem_tra_diem = (diem >= 6.5) and (diem < 8.0)
print("Điểm loại Khá:", kiem_tra_diem)

kiem_tra_tuoi = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60:", kiem_tra_tuoi)

phu_dinh_tuoi = not kiem_tra_tuoi
print("Phủ định điều kiện tuổi:", phu_dinh_tuoi)

# 5.3
x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x /= 4
print(x)
x //= 2
print(x)
x **= 3
print(x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh_sach không?", 3 in danh_sach)
danh_sach_2 = danh_sach #tham chieu = dia chi bo nho
print("2 biến có cùng tham chiếu không?", danh_sach is danh_sach_2)

# 5.4
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False) # not -> and -> or

# hoat dong 6

# 6.1
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

# 6.2
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)

print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))