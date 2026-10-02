danh_sach_sv = [
    {"ma_sv": "2411060369", "ho_ten": "Nguyen Viet Hoang", "lop": "DH14C1", "diem_tb": 8.5},
    {"ma_sv": "hunre1", "ho_ten": "Nguyen Viet Anh", "lop": "DH14C1", "diem_tb": 7.0},
    {"ma_sv": "hunre2", "ho_ten": "Vuong Quoc Chinh", "lop": "DH14C1", "diem_tb": 7.5},
    {"ma_sv": "hunre3", "ho_ten": "Pham Tuan Duong", "lop": "DH14C1", "diem_tb": 9.0}
]

def hien_thi_danh_sach():
    print("\n" + "=" * 65)
    print(f"{'Ma SV': <15}{'Ho va ten': <20}{'Lop': <15}{'Diem TB': <10}")
    print("=" * 65)
    for sv in danh_sach_sv:
        print(f"{sv['ma_sv']: <15}{sv['ho_ten']: <20}{sv['lop']: <15}{sv['diem_tb']: <10}")
    print("=" * 65)

def tim_sv_theo_ma(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

def tim_kiem_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sv}.")
    else:
        print("\n--- KET QUA TIM KIEM ---")
        print(f"Ma SV: {sv['ma_sv']}")
        print(f"Ho ten: {sv['ho_ten']}")
        print(f"Lop: {sv['lop']}")
        print(f"Diem trung binh: {sv['diem_tb']}")
        print("-" * 25)

def them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return
    danh_sach_sv.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "lop": lop,
        "diem_tb": diem_tb
    })
    print(f"-> Da them sinh vien {ho_ten} thanh cong.")

def xoa_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sv}.")
        return
    danh_sach_sv.remove(sv)
    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")

def cap_nhat_thong_tin(ma_sv_cu, ma_sv_moi, ho_ten_moi, lop_moi, diem_tb_moi):
    sv = tim_sv_theo_ma(ma_sv_cu)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sv_cu}.")
        return
    if ma_sv_moi != ma_sv_cu and tim_sv_theo_ma(ma_sv_moi) is not None:
        print(f"-> Ma sinh vien moi '{ma_sv_moi}' da ton tai, khong the them.'")
        return

    sv["ma_sv"] = ma_sv_moi
    sv["ho_ten"] = ho_ten_moi
    sv["lop"] = lop_moi
    sv["diem_tb"] = diem_tb_moi
    print(f"-> Da cap nhat thong tin.")

def thong_ke_hoc_luc():
    gioi = len([sv for sv in danh_sach_sv if sv["diem_tb"] >= 8.0])
    kha = len([sv for sv in danh_sach_sv if 6.5 <= sv["diem_tb"] < 8.0])
    tb_yeu = len([sv for sv in danh_sach_sv if sv["diem_tb"] < 6.5])

    print("\n--- THONG KE HOC LUC ---")
    print(f"Sinh vien Gioi (>= 8.0): {gioi}")
    print(f"Sinh vien Kha (6.5 - 7.9): {kha}")
    print(f"Sinh vien Tb/Yeu (< 6.5): {tb_yeu}")

def nhap_diem_an_toan(loi_nhac):
    while True:
        try:
            diem = float(input(loi_nhac))
            if 0 <= diem <= 10:
                return diem
            else:
                print("-> Diem phai tu 0 den 10. Vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so thuc.")

def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien moi")
    print("3. Cap nhat thong tin sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke hoc luc")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            print("\n--- THEM SINH VIEN ---")
            ma_sv = input("Nhap ma sv: ").strip()
            ho_ten = input("Nhap ho ten: ").strip().title()
            lop = input("Nhap lop: ").strip()
            diem_tb = nhap_diem_an_toan("Nhap diem trung binh (0-10): ")
            them_sinh_vien(ma_sv, ho_ten, lop, diem_tb)

        elif lua_chon == "3":
            print("\n--- CAP NHAT THONG TIN ---")
            ma_sv_cu = input("Nhap ma SV can cap nhat: ").strip()

            # Kiểm tra xem mã cũ có tồn tại trước khi cho nhập cả nùi thông tin mới
            if tim_sv_theo_ma(ma_sv_cu) is None:
                print(f"-> Khong tim thay sinh vien co ma {ma_sv_cu}.")
            else:
                print("Nhap thong tin moi:")
                ma_sv_moi = input("- Nhap ma SV moi: ").strip()
                ho_ten_moi = input("- Nhap ho ten moi: ").strip().title()
                lop_moi = input("- Nhap lop moi: ").strip()
                diem_tb_moi = nhap_diem_an_toan("- Nhap diem trung binh moi (0-10): ")
                cap_nhat_thong_tin(ma_sv_cu, ma_sv_moi, ho_ten_moi, lop_moi, diem_tb_moi)

        elif lua_chon == "4":
            ma_sv = input("Nhap ma sv can xoa: ").strip()
            xoa_sinh_vien(ma_sv)

        elif lua_chon == "5":
            ma_sv = input("Nhap ma SV can tim: ").strip()
            tim_kiem_sinh_vien(ma_sv)

        elif lua_chon == "6":
            thong_ke_hoc_luc()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()
