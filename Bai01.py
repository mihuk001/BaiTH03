a=input("Nhập day so nguyen(cach nhau bang dau cach): ")
tach_chuoi= a.split()
ds_so=[]
for i in tach_chuoi:
    ds_so.append(int(i))
tong=sum(ds_so)
print("Tổng các số nguyên là: ", tong)