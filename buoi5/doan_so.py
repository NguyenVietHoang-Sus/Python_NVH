import random

so_can_doan = random.randint(1, 100)
so_luot_toi_da = 7
luot_hien_tai = 0

while luot_hien_tai < so_luot_toi_da:
    luot_hien_tai += 1
    so_doan = int(input(f"Luot {luot_hien_tai}/{so_luot_toi_da} - Nhap so ban doan(1-100): "))
    if so_doan == so_can_doan:
        print(f"Chinh xac! Ban da doan dung sau {luot_hien_tai} luot.")
        break
    elif so_doan < so_can_doan:
        print("Goi y: so can doan LON HON so ban vua nhap")
    else:
        print("Goi y: so can doan NHO HON so ban vua nhap")
else:
    print(f"Ban da het luot doan. So can tim la: {so_can_doan}")
