import os 

file_path = "test.txt" 

if os.path.exists(file_path):
    print(f"the location of'{file_path}' exists")
else :
    print ("the location doesn't exist" )