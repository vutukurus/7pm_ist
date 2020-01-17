#argument passing..
import sys

print (sys.argv)
cost = sys.argv[1]
print (sys.argv[2])

print (cost)
cost = int(cost)


if cost > 100:
    print ("got discuount of 10 rs")   

if cost < 100:
    print ("got discuount of 5 rs")

if cost == 100:
    print ("No discuont")