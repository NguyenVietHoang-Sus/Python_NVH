import sqlite3

TEN_FILE_CSDL = "sinh_vien.db"


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        """
        CREATE TABLE IF NOT EXISTS sinh_vien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ma_sv TEXT UNIQUE NOT NULL,
            ho_ten TEXT NOT NULL,
            lop TEXT NOT NULL,
            diem_gpa REAL NOT NULL
        )
    """
    )
    ket_noi.commit()
    ket_noi.close()


def them_sinh_vien(ma_sv, ho_ten, lop, diem_gpa):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        """
        INSERT INTO sinh_vien (ma_sv, ho_ten, lop, diem_gpa)
        VALUES (?, ?, ?, ?)
    """,
        (ma_sv, ho_ten, lop, diem_gpa),
    )
    ket_noi.commit()
    ket_noi.close()


def lay_toan_bo_sinh_vien():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT id, ma_sv, ho_ten, lop, diem_gpa FROM sinh_vien ORDER BY id"
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


def cap_nhat_sinh_vien(id_sv, ma_sv, ho_ten, lop, diem_gpa):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        """
        UPDATE sinh_vien 
        SET ma_sv = ?, ho_ten = ?, lop = ?, diem_gpa = ?
        WHERE id = ?
    """,
        (ma_sv, ho_ten, lop, diem_gpa, id_sv),
    )
    ket_noi.commit()
    ket_noi.close()


def xoa_sinh_vien(id_sv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM sinh_vien WHERE id = ?", (id_sv,))
    ket_noi.commit()
    ket_noi.close()


def thong_ke_theo_lop():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT lop, COUNT(*) FROM sinh_vien GROUP BY lop")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


if __name__ == "__main__":
    print("--- 1. Khởi tạo bảng ---")
    tao_bang_neu_chua_co()

    print("\n--- 2. Thêm sinh viên mẫu ---")
    try:
        them_sinh_vien("SV01", "Nguyen Van An", "CNTT1", 8.2)
        them_sinh_vien("SV02", "Tran Thi Bich", "CNTT2", 7.5)
        them_sinh_vien("SV03", "Le Van Cuong", "CNTT1", 9.0)
        them_sinh_vien("SV04", "Pham Minh Duc", "DTVT1", 6.8)
        print("Đã thêm 4 sinh viên mẫu thành công.")
    except sqlite3.IntegrityError:
        print("Dữ liệu mẫu đã tồn tại từ trước.")

    print("\n--- 3. Danh sách toàn bộ sinh viên ---")
    danh_sach = lay_toan_bo_sinh_vien()
    for sv in danh_sach:
        print(sv)

    print("\n--- 4. Cập nhật điểm cho sinh viên đầu tiên (id=1) ---")
    if danh_sach:
        id_dau = danh_sach[0][0]
        cap_nhat_sinh_vien(id_dau, "SV01", "Nguyen Van An", "CNTT1", 8.8)
        print(f"Đã cập nhật sinh viên id={id_dau}: điểm mới là 8.8")

    print("\n--- 5. Thống kê số lượng sinh viên theo lớp ---")
    du_lieu_tk = thong_ke_theo_lop()
    print("Kết quả thống kê:", du_lieu_tk)