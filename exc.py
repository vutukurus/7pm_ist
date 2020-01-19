import sys

a = [10,20,30,40]

try:
    print (a[0] + "this")
except IndexError:
    print ("Error: You are giving index out of range")
except:
    print ("Some other error",sys.exc_info())
finally:
    print ("I am finaly")
print ("Script completed")
