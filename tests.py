#this is other file..
import sys
print ("initial",sys.path)

sys.path.append(r"C:\Users\Vswear\Desktop\7pm_ist\7pm_ist\project")

import functions_sample as fs

print ("after",sys.path)

#sys.exit(0) #0 pass, -vve failure..

data = [10,90,80,50]

d = fs.len_own(data)

print ("count is ",d)
