ten_truong ="hoc vien cong nghe buu chinh vien thong"

print(ten_truong[4:8])
#Note : trong python co ca chi so am va duong , chi so duong giong c++ , con chi so am bat dau tu -1    
print(ten_truong[0])
print(ten_truong[-1])
# ky thuat slicing ( giong  substr y het )
a = "chao mung den voi binh nguyen vo tan"
print("chuoi duoc cat ra la :" , a[:10][:9])
#su dung toan tu % de dinh dang chuoi
s = "binh nguyen vo tan"
print("chao mung den voi %s !" % s)
#noi chuoi bang f string 
gia_but_bi = 2500  
so_luong_but = 3
gia_quyen_vo = 8000 
tong_tien = f'Tong tien mua {so_luong_but} but bi va 1 quyen vo : {gia_but_bi * so_luong_but + gia_quyen_vo} vnd'
print(tong_tien)
# mot so ham dinh dang nen dung 
   #capitalize() : viet_hoa_chu_cai_dau
# giong nhu trong c++
'''
string s 
for(int i= 0 ; i < s.size() ; i++){
s[0] = toupper(s[0]);
}'''
# swapcase() : dao nguoc kieu chu viet hoa thanh thuong va nguoc lai 
# title() : viet hoa chu dau va cac chu con lai viet thuong 

#split() : tach chuoi theo theo 1 ky tu phan tach va tra ve danh sach cac chuoi con 
# isalnum() , isdigit() , isalpha() .... 