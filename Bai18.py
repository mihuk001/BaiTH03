n=int(input("nhap so luong san pham: "))
sku_dict={}
for i in range(n):
    print(f"nhap thong tin san pham thu {i+1}")
    sku= input("nhap ma SKU(vi du SKU1): ").strip()
    quantity= int(input("nhap so luong: "))
    sku_dict[sku]= sku_dict.get(sku, 0) + quantity
ket_qua= list(sku_dict.items())
print(f"danh sach san pham khong trung: {ket_qua}")    