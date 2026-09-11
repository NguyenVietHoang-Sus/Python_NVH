doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

danh_sach_tu = doan_van.split()
tan_suat = {}

for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")