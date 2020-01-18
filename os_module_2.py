#os module..
import os

#os.listdir

a = os.listdir(r"C:\Users\Vswear\Desktop\7pm_ist\7pm_ist")

print (a)

for i in a:
    if i.endswith(".txt"):
        print (i)
        
for i in a:
    if i.find(".txt") >= 0:
        print (i)