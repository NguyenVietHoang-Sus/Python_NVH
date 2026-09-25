# Hoat dong 1
# 1.1
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return uscln(b, a) # a*b

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print(uscln(24, 36))
print(bscnn(4, 6))
print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28))

# 1.2
def in_loi_chao(ten):
    print(f"xin chao, {ten}!")
    return # tra ve none

def chia_lay_thuong_du(a, b):
    return a // b, a % b # tra nhieu gia tri qua tuple

in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")

# Hoat dong 2
def gioi_thieu(ten, tuoi=18, lop="chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

gioi_thieu("An")
gioi_thieu("Binh", 20)
gioi_thieu("Chi", lop="CNTT01")
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)

# Hoat_dong_3
# 3.1
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong()) # tra ve 0

# 3.2
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")

in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")

