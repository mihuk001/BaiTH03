def nhap_dictionary(ten_dict):
    a= {}
    n= int(input(f"Nhập số lượng phần tử của {ten_dict}: "))
    for i in range(n):
        key = input(f"  Nhập key (tên) thứ {i + 1}: ")
        value = int(input(f"  Nhập value (số lượng) cho '{key}': "))
        a[key] = value
    return a

print("--- NHẬP DICTIONARY 1 ---")
dict1 = nhap_dictionary("Dictionary 1")

print("--- NHẬP DICTIONARY 2 ---")
dict2 = nhap_dictionary("Dictionary 2")

ket_qua = dict1.copy() 

for key, value in dict2.items():
    if key in ket_qua:
        ket_qua[key] += value   
    else:
        ket_qua[key] = value  

print("Dictionary sau khi gộp:")
print(ket_qua)