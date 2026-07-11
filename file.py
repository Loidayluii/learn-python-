import os 

file_path = "test1.txt"

if ( os.path.exists(file_path)):
    print(f"the location of '{file_path}' exist ")
else :
    print("the location doesn't exist")