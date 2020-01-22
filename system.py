##subprocess --> if u want to store output..
#os.system --> you just need to execute.

import os
import subprocess

a = os.system("dir")
print ("="*10)
print (a)

a = subprocess.check_output("dir", shell = True)
print ("="*10)
print (a)





