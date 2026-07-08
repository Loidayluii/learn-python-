# set kha giong trong c++

list1 = [1,2,3,4,5,6,7,7,8]

my_set = set(list1)
print(my_set)
# them mot phan tu vao set thi su dung ham add()
# xoa mot phan tu khoi set thi dung ham remove()
# mot so ham tuong tu nhu trong c++ : union() , intersection()  , difference() : a \ b  , synmetric_difference() : thuoc 1 trong 2 set nhung khong nam trong ca 2 set 

# set comprehensions
binh_phuong = { x ** 2 for x in range(1,6)}
print(binh_phuong)

Set = {x for x in range(1,11) if x % 2 == 0 }
print(Set)

nest_set = {(x,y) for x in range(1,3) for y in range(1,3)}
print(nest_set)  # { (1,1) (1,2) (2,1) (2,2) }
