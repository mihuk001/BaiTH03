n= input("nhap danh sach so nguyen(cach nhau bang dau cach): ").split()
danh_sach= [int(x) for x in n]
N= int(input("nhap so N: "))
min_diff= float('inf')
for i in range(len(danh_sach)):
    for j in range(i+1, len(danh_sach)):
        tong= danh_sach[i] + danh_sach[j]
        diff = abs(N-tong)
        if diff < min_diff:
            min_diff = diff
            ket_qua = (danh_sach[i], danh_sach[j])
print(f"cap so co tong gan N nhat la: {ket_qua[0]} va {ket_qua[1]}" )