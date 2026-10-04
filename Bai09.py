danh_sach=list(map(int,input("Nhập day so nguyen(cach nhau bang dau cach): ").split()))
ket_qua=[]
for i in danh_sach:
    if i not in ket_qua:
        ket_qua.append(i)
print(f"cac so khong trung lap(giu nguyen thu tu): {ket_qua}")