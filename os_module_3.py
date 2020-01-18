#os module.
import os

path = r"C:\Users\Vswear\Desktop\04_11_2019"

list_of_files = os.listdir(path)

for file in list_of_files:
    if file.endswith(".py"):
        #full_path = path+"\\"+file
        full_path = os.path.join(path,file)
        print (full_path)
        os.remove(full_path)
        print ("Deleted", file)
print ("=Completed=")
