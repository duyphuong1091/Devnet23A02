# def tinh_tong(a, b):
#     return a + b
# print(tinh_tong(2, 5))

# Nhập giá trị 
# name = input("Nhập tên của bạn: ")
# print("Tên của bạn là: " + name)

# Câu lệnh if else
# Nhập số liệu từ bàn phím
# b = input("Nhập vào giá trị: ")

# # Kiểm tra giá trị nhập vào
# if b.isdigit():
#     # Chuyển chuỗi thành số
#     b = int(b)
    
#     # So sánh b với 0
#     if b < 0:
#         print("b is less than zero")
#     elif b == 0:
#         print("b is exactly zero")
#     elif b > 0:
#         print("b is greater than zero")
#     else:
#         print("is something else")
        
# else:
#     print("Giá trị nhập vào là chuỗi nên không so sánh được")

###### HÀM #########
# def phep_tinh(a, b, phep_toan):
#     if phep_toan == "*":
#         return a * b
#     elif phep_toan == "/":
#         return a/b
#     elif phep_toan == "+":
#         return a + b
#     elif phep_toan == "-":
#         return a - b
#     else:
#         print("Không tồn tại phép toán '{}' trong hàm này !".format(phep_toan))

# gia_tri = phep_tinh(5, 6, "//")
# print(gia_tri)

# Nhập nhiều giá trị từ bàn phím
# gt = input("Nhập các giá trị cách nhau bằng dấu cách: ")
# # if gt.isdigit():
# arr_gt = gt.split(" ")
# max = int(arr_gt[0])

# for elem in arr_gt:
    
#     if int(elem) > max:
#         max = int(elem)
# print("Giá trị lớn nhất trong những giá trị nhập vào: ", max)

##### KIỂU DỮ LIỆU #####
# tname = ('a','b','c')
# #tname[0] = 'd' : KHÔNG THỂ THAY ĐỔI GIÁ TRỊ CỦA PHẦN TỬ TRONG KIỂU TUPLE
# print(tname)

# dname = ['a','b','c']
# dname[0] = 'd'
# print(dname)

# dict_name = {'name':'Phương', 'phone':123}
# print(type(dict_name))
# dict_name['name'] = "Tuấn"
# print(dict_name)

##### IMPORT THƯ VIỆN #####
# import random
# a = random.randint(0,10)
# print(a)

# from random import randint
# a = randint(0, 100)
# print(a)

##### ĐỌC FILE DỮ LIỆU ######
# r: đọc file 
# w: ghi đè vào file 
# a: ghi nối vào file
# f = open('data.txt', 'r')
# data = f.read()
# print(type(data))
# print(data)
# i = 0
# for d in data: 
#     print(i, d)
#     i += 1

# data1 = f.readlines()
# print(data1)
# f.close() : đóng file dữ liệu

# Ghi đè dữ liệu vào file data.txt
# f = open('data.txt','w')
# f.write('Hello World')
# f.close()

# Ghi nối vào file dữ liệu tiếp theo
# f = open('data.txt','a')
# f.write('\nMy name is Phuong') # \n : là xuống hàng
# f.close()