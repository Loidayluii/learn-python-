'''import os 

file_path = "test1.txt"

if ( os.path.exists(file_path)):
    print(f"the location of '{file_path}' exist ")
else :
    print("the location doesn't exist")
'''

capitals =["Ha_Noi" , "Tokyo" ,"Berlin" ,"Praha"]

file_path = "C:/Users/Admin/OneDrive/Desktop/output.txt"
# neu thay w bang a thi append(them vao) data mot lan nua 
try :
    with open(file_path,"w") as file:
        for capital in capitals:
            file.write(capital + " ")
    print(f"txt file '{file_path}' was created")
except FileExistsError :
    print("this file already exist")