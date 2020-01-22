##subprocess --> if u want to store output..
#os.system --> you just need to execute.

import os
import subprocess

a = os.system("dir")
print ("="*10)
print (a)

a = subprocess.check_output("dir", shell = True)
print ("="*10)
print (a) #string


a = subprocess.check_call("dir", shell = True)
print ("="*10)
print (a)


p = subprocess.Popen(["dir"], stdout=subprocess.PIPE, shell = True)
a = p.communicate()
print (a) #list..




