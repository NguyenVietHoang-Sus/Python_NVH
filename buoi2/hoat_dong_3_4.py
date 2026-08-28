import math

#hoat dong 3
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen)) # ep int -> float
print(int(so_thuc)) # ep float -> int (cat phan thap phan)

a = -7
b = 2.6789
c, d = 17, 5

print(abs(a)) # gia tri tuyet doi
print(round(b)) # lam tron
print(round(b, 2)) # lam tron 2 chu so thap phan
print(pow(c, 2)) # c mu 2
print(divmod(c, d)) # tra ve (thuong, du) dang tuples

a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

#hoat dong 4
cau = "Lap trinh Python rat thu vi"
print(cau[0]) # ky tu dau tien
print(cau[-1]) # ky tu cuoi cung
print(cau[4:10]) # cat tu vi tri 4 den truoc vi tri 10
print(cau[:8]) # tu dau den vi tri 8
print(cau[11:]) # tu vi tri 11 den het
print(cau[::-1]) # dao nguoc chuoi
print(cau[-1] == cau[::-1])

ten = "Nam"
# Thu gan lai mot ky tu: ten[0] = "T" -> quan sat loi TypeError
ten_moi = "T" + ten[1:]
#ten[0] = "T"
print(ten_moi)

cau = " Toi dang HOC Python rat vui "
print(cau.strip()) # bo khoang trang 2 dau
print(cau.strip().upper()) # in hoa toan bo
print(cau.strip().lower()) # in thuong toan bo
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split()) # tach thanh danh sach cac tu
print(len(cau.strip().split())) # dem so tu trong cau
print(cau.count("o")) # dem so lan xuat hien ky tu 'o'
print(cau.find("Python")) # vi tri bat dau cua "Python"
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

ho_ten_tho = " nguyen   van   an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) # Nguyen Van An