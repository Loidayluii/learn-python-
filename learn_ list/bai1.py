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
#duyet cac phan tu trong list 
'''
a = (34,54,67,21,78,97,45,44,80,19)
total = 0
for i in a:
   total += i
print ("Tong =", total)
'''
#range(start , end , step) voi start = 0 , end = n - 1 , step = 1 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
chan = []
le = []

for x in numbers:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

print("Số chẵn:", chan)
print("Số lẻ:", le)'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i], "la so chan")
    else:
        print(numbers[i], "la so le")
        '''
        len()

split() : tách chuỗi theo chuỗi ký tự 
 
a = "xin , chao , toi , la , Loi "
print(a.split(","))
# kết quả : [xin , chao , toi , la , Loi]
replace() : thay the 
text = "Xin chào thế giới"
result = text.replace("thế giới", "Python")
# Kết quả: 'Xin chào Python'

strip()  : loại bỏ các khoảng trắng thừa 

'''

