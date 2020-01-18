import shutil
import os
import sys

clean_path = sys.argv[1]
clean_path = r"{}".format(clean_path)
#r"c:\users"

cleaned_dir = os.path.join(clean_path, "cleaned_dir")

if os.path.exists(cleaned_dir):
    print ("cleaned dir exists")
else:
    os.mkdir(cleaned_dir)
    
get_list = os.listdir(clean_path)
files_lists = []

for i in get_list:
    full_path = os.path.join(clean_path, i)
    if os.path.isdir(full_path):
        pass
    else:
        
        files_lists.append(full_path)
print (files_lists)

print ("="*10)
print ("extraacing the extenstions")

for i in files_lists:
    
    t = i.split(".")
    print (t[1])
    full_path = os.path.join(cleaned_dir,t[1])

    if not os.path.exists(full_path):
        os.mkdir(full_path)
       
print ("="*10)
print ("Copy the files to needed ext folders..")

for i in files_lists:
    src = i
    get_ext = i.split(".")[1]
    get_file = os.path.basename(i)
    dst = os.path.join(cleaned_dir, get_ext, get_file)
    print (dst)
    #cp -f src dst
    shutil.copy(src, dst)






    
    
    
    
    
    
    