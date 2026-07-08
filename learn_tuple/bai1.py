# ve co ban tuple kha giong list , khac voi list o mot cho l list co the thay doi cac phan tu con tuple thi khongthe chinh sua , xoa ...
# va tuple duoc dat trong ngoac tron 

tup1 = (1,2,3,'toan' , 'ly' , 3.14 , 5+3j)

# list comprehension
# Tuple ban đầu
doanh_thu_quy = (1000, 1500, 800, 2200) 

# Chuyển Tuple thành List
doanh_thu_quy_list = list(doanh_thu_quy)

# Sử dụng List Comprehension để dự đoán doanh thu quý sau, tăng thêm 10%
doanh_thu_quy_sau_list = [int(doanh_thu * 1.1) for doanh_thu in doanh_thu_quy_list]

# Chuyển List đã cập nhật thành Tuple
doanh_thu_quy_sau = tuple(doanh_thu_quy_sau_list)

# In Tuple ban đầu và Tuple đã cập nhật
print("doanh thu quy hien tai:", doanh_thu_quy)
print("du doan doanh thu quy sau:", doanh_thu_quy_sau)

#Unpacking
# Ví dụ Unpack Tuple
thong_tin_ca_nhan = ("Nguyễn Văn A", 30, "Hà Nội")
ten, tuoi, dia_chi = thong_tin_ca_nhan

print("Tên:", ten)
print("Tuổi:", tuoi)
print("Địa chỉ:", dia_chi)