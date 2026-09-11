tu_dien_anh_viet={
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

#Tra tu
print(tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"));
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"));

#Them tu moi
tu_dien_anh_viet["computer"] = "may tinh";

#Xoa mot tu
tu_dien_anh_viet.pop("table")

print("Tu dien hien tai:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")