#()
# *, /
#+, -

a  = (10+20)/100

print (a)

#If conditions..

cost  = input("Enter your cost")
print ("user given value",cost)
print (type(cost))
#>= --> greater and equal
#<= --> less and equal

cost = int(cost)
if cost > 100:
    print ("got discuount of 10 rs")   

if cost < 100:
    print ("got discuount of 5 rs")

if cost == 100:
    print ("No discuont")

print ("="*10)
#second way..
if cost > 100:
    print ("got discuount of 10 rs")   
elif cost < 100:
    print ("got discuount of 5 rs")
elif cost == 100:
    print ("No discuont")
else:
    pass
    
    
    

    
    
    
    