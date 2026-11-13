def them_san_pham(danh_sach, ma, ten, gia, soluong):
    sp = {
        "MaSP": ma,
        "TenSP": ten,
        "Gia": int(gia),
        "SoLuong": int(soluong)
    }
    danh_sach.append(sp)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    tu_khoa_thuong = tu_khoa.lower()
    ket_qua = []
    for sp in danh_sach:
        if tu_khoa_thuong in sp["TenSP"].lower():
            ket_qua.append(sp)
    return ket_qua

def tong_gia_tri_ton_kho(danh_sach):
    tong = 0
    for sp in danh_sach:
        tong += sp["Gia"] * sp["SoLuong"]
    return tong

def hien_thi_danh_sach(danh_sach):
    if not danh_sach:
        print("Khong co san pham")
        return
    for sp in danh_sach:
        print(f"{sp['MaSP']} - {sp['TenSP']} - Gia: {sp['Gia']} - SL: {sp['SoLuong']}")

if __name__ == "__main__":
    ds_san_pham = [
        {"MaSP": "SP001", "TenSP": "Bút bi Thiên Long", "Gia": 3000, "SoLuong": 150},
        {"MaSP": "SP002", "TenSP": "Vở học sinh 96 trang", "Gia": 8000, "SoLuong": 8},
        {"MaSP": "SP003", "TenSP": "Bút chì 2B", "Gia": 2500, "SoLuong": 200}
    ]

    while True:
        print("-" * 10)
        hien_thi_danh_sach(ds_san_pham)
        print("-" * 10)
        print("1. Them san pham")
        print("2. Tim kiem theo ten")
        print("3. Xem tong gia tri ton kho")
        print("4. Thoat chuong trinh")

        chon = input("Chon chuc nang (1-4): ")

        if chon == "1":
            ma = input("Nhap ma sp: ")
            ten = input("Nhap ten sp: ")
            gia = int(input("Nhap gia sp: "))
            soluong = int(input("Nhap so luong sp: "))
            them_san_pham(ds_san_pham, ma, ten, gia, soluong)
            print("Them san pham thanh cong")
        elif chon == "2":
            tu_khoa = input("Nhap tu khoa ten sp: ")
            kq = tim_kiem_theo_ten(ds_san_pham, tu_khoa)
            print("Ket qua tim kiem: ")
            hien_thi_danh_sach(kq)
        elif chon == "3":
            tong_tien = tong_gia_tri_ton_kho(ds_san_pham)
            print(f"Tong gia tri ton kho la: {tong_tien:,} đ")
        elif chon == "4":
            print("Da thoat chuong trinh")
            break
        else:
            print("Khong hop le, chon lai")