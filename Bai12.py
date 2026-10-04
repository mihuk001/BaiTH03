chuoi = input("Nhập chuỗi ký tự: ")
tan_suat = {}
for i in chuoi:
    if i in tan_suat:
        tan_suat[i] += 1  
    else:
        tan_suat[i] = 1   

print("Dictionary đếm tần suất xuất hiện ký tự:")
print(tan_suat)