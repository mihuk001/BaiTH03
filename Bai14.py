n= int(input("Nhập số lượng cặp (x, y): "))
toa_do = []
for i in range(n):
    x,y=map(float, input(f"Nhập cặp (x, y) thứ {i +1}: ").split())
    toa_do.append((x, y))
    tong_x= sum(x[0] for x in toa_do)
    tong_y= sum(y[1] for y in toa_do)
tb_x= tong_x/n
tb_y= tong_y/n
print(f"Tọa độ trung bình của các điểm là: ({tb_x}, {tb_y})")