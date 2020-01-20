#raising our own exceptions

a = int(input("enter a value"))

print (a)

if a < 0 :
    raise Exception("Don't give negative valuies")

