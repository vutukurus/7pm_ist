#os.walk
import os

path  = r"C:\Users\Vswear\Desktop\30_11_2017"

#r - root
#d - dir
#f - file
for r,d,f in os.walk(path):
    print (r)
    print (d)
    print (f)
    