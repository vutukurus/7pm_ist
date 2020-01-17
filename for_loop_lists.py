#for loop on lists.
a = [10, 20.5, 'perl', 'python', 100, 10, 90, 80, 70]

t = 0
for i in a:
    print (i)
    t = t +1
    
print (t)


b = ["perl" , "count"]

for i in b:
    print (i)
    for j in i:
        if j == "r":
            print ("found r for ", i)

#Functions../Modules...
#python modules -> os