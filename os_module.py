#os module.
import os

#create a directory
#director/file existnace..

if os.path.exists("test"):
    print ("dir already exists no need to create")
else:
    os.mkdir("test")
    print ("dir created..")

os.rmdir("test")

if os.path.exists(r"tt"):
    os.removedirs(r"tt\uu\iii")
else:
    os.makedirs(r"tt\uu\iii")

