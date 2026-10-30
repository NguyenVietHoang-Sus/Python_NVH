import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print(type(diem_list), type(diem_array))

# phep toan vector hoa
diem_cong_them = diem_array + 0.5
print(diem_cong_them)

# su dung list comprehension/vong lap
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)

print("Trung binh: ", np.mean(diem_array))
print("Lon nhat: ", np.max(diem_array))
print("Nho nhat: ", np.min(diem_array))
print("Do lech chuan: ", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)
