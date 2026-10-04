thong_tin = {}
for i in range(3):
    print(f"--- Nhập thông tin người thứ {i + 1} ---")
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    thong_tin[ten] = tuoi

print("kết quả:")
print(thong_tin)