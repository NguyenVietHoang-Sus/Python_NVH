# Hoat dong 1
sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa

sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["diem_tb"] = 9.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc

print(sinh_vien)

#Hoat dong 2
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
    print(mon)

for diem in diem_mon_hoc.values():
    print(diem)

for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#Hoat dong 3
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2) # giao: mon hoc chung 2 hoc ky
print(mon_hoc_ky1 | mon_hoc_ky2) # hop: tat ca mon hoc ca 2 hoc ky
print(mon_hoc_ky1 - mon_hoc_ky2) # mon chi co o hoc ky 1
