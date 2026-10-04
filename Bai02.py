danh_sach= input("nhap cac chuoi (cach nhau bang dau cach): ").split()
tu_can_dem= input("nhap tu can dem: ")
so_lan= danh_sach.count(tu_can_dem)
print(f"tu '{tu_can_dem}' xuat hien {so_lan} lan trong danh sach.")