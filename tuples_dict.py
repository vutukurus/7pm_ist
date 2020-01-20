#Tuples and Dicts..
#tuples are immutable..
#Why ?
#all immutables are allowed as keys.
#string,tuples,sets

a = (10,20,30)
print (a[0])

#Dicts..
#key , value pairs...
t = {"hyd":"10.9.10", "sd":"sandeigo", "LA":"losangles"}

print (t)
print (t["hyd"])
print (t["LA"])

for k,v in t.items():
    if v == "losangles":
        print (k)
    #print (k)
    #print (v)
t["abc"] = "hyderabad"
print (t)    





