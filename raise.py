#raising our own exceptions

a = int(input("enter a value"))

print (a)

if a < 0 :
    try:
        raise ("Don't give negative valuies")
    except:
        print ("test")

