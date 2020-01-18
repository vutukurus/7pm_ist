import sys

#arguments passing..
#include paths from other folders..
#exit from the code..
#version or platform ..

print (sys.version)
print (sys.version_info)
print (sys.platform)

if sys.version == 3.7.3:
    #code...
    
elif sys.version == 2.7:
    #code...
    
if sys.platform == win32:
    path = r"C:\Users\Vswear\Desktop\7pm_ist\7pm_ist\project"
elif sys.platform == mac:
    paht = r"/local/mnt/workspace"