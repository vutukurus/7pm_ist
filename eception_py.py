#exceptional handling.

a = [10,20,30,40]

try:
    print (a[0] + "this")
except IndexError:
    print ("Error: You are giving index out of range")
except:
    print ("Some other error")
finally:
    print ("I am finaly")
print ("Script completed")




try:
    a = 10/0
    print (a)
except ZeroDivisionError:
    print ("You are divifding by zero")
except:
    print ("some other error")