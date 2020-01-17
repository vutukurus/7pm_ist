#string inbuilt methods.

a = "hashedkey.py"

#['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#count
print ( a.count("l") )

#endswith
print (a.endswith("pdf"))

if a.endswith("pdf"):
    print ("this is a pdf file")
elif a.endswith("py"):
    print ("this is a py file")
else:
    print ("unkonw file")
    
#find..
print (a.find("z"))

if a.find("ash") > 0:
    print ("found")
else:
    print ("not found")
    
#join, strip, lstrip, rstrip, split, index..
#join(to covert a list to string)
t = "apple"
b = "guava"

print (t+ "-"+ b)
print ("***".join([t,b]))

#strip..
t = "@@afs@ad@@"
print (t.strip("@"))
print (t.lstrip("@"))
print (t.rstrip("@"))

#len of the string..
print (len(t))

#index..
print (t.index("@"))
















