#for loop on lists.

def count(d):
    print (d)
    
def len_own(d):
    t = 0
    for i in d:
        print (i)
        t+=1 #t = t+1
        
    print (t)
    return t

if __name__ == "__main__":
    a = [10, 20.5, 'perl', 'python', 100, 10, 90, 80, 70]

    b = [20,30,60,70]
     
    len_own(a)
    len_own(b)