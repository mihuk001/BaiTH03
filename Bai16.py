n = int(input("Nhập số lượng sinh viên: "))
diem={}
for i in range(n):
    print(f"--- Nhập thông tin sinh viên thứ {i + 1} ---")
    ten = input("Nhập tên: ")
    diem_so = float(input("Nhập điểm số: "))
    diem[ten] = diem_so
diem_sap_xep= sorted(diem.items(), key=lambda x: x[1], reverse=True)
print("Danh sách sinh viên theo thứ tự điểm số giảm dần:")    
for ten, diem_so in diem_sap_xep:
    print(f"{ten}: {diem_so}")