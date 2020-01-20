#Files handling...
#read --> read a file..(r)
#write (w)
#append.. (a)

with open("sample.txt","r") as f:
    a = f.readlines()
    print (a)
    print (a[2])
    if a[2].find("this") > 0:
        print ("This is found")
    