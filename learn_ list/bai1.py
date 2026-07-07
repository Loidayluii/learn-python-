#truy cap cac gia tri cua list
'''
danh_sach_1 = ["An", "vat_ly", 21, 69.75]  # List chứa chuỗi, số nguyên, số thực
danh_sach_2 = [1, 2, 3, 4, 5]         # List chứa toàn số nguyên
danh_sach_3 = ["a", "b", "c", "d"]      # List chứa các ký tự
danh_sach_4 = [25.50, True, -55, 1+2j]   # List chứa số thực, bool, số nguyên, số phức
trai_cay = ['xoai' , 'cam' , 'tao' , 18 , 36] 
so_nguyen = [1,2,3,4,5,6,7]

print(trai_cay[0]) 
print ("4 phan tu so nguyen tu 1 den 4 la :" , so_nguyen[1:5])
print ("cac phan tu la so nguyen la :" , trai_cay [3:5])      # slicing cat tu n den (m-1)


list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("Sau khi xóa giá trị tại index 2 : ")
print(list1)
'''
#cac phep toan tren list 
list2 = [1,2,3,4,5,6]
list3 = [7,8]
print(3 in (list2))
print(list2 + list3)
# mot so ham dung san 

list4 = [1,2,3,4,5]
print(len(list4))
print(max(list4))
print(min(list4))