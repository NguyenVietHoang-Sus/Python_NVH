# Hoat dong 5
# 5.1
diem = 6.5

if diem >= 8.0:
    pass #skip
elif diem >= 5.0:
    print("Dat yeu cau")
else:
    pass

# 5.2
so = 29
la_so_nguyen_to = True

if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break  # thoat khi tim thay uoc so

print(f"{so} co phai la so nguyen to khong? {la_so_nguyen_to}")

# 5.3
n = 20
so_hien_tai = n + 1

while True:
    la_so_nguyen_to1 = True
    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to1 = False
            break

    if la_so_nguyen_to1:
        break

    so_hien_tai += 1

print(f"So nguyen to dau tien lon hon {n} la {so_hien_tai}")

# 5.4
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue  # bo qua cac so khong duong, khong them vao danh sach
    danh_sach_hop_le.append(so)

print("Cac so hop le (duong): ", danh_sach_hop_le)

# Hoat dong 6
# 6.1
n1 = 5
for i in range(1, n1 + 1):
    for j in range(i):
        print("*", end="")  # tam giac
    print()

# 6.2
n2 = 4

# Nua tren hinh thoi
for i in range(1, n2 + 1):
    print(" " * (n2 - i) + "*" * (2 * i - 1))

# Nua duoi hinh thoi
for i in range(n2 - 1, 0, -1):
    print(" " * (n2 - i) + "*" * (2 * i - 1))