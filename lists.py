#lists
#store multiple data types.
#mutable..
#indexing start 0..
#slicing/indexing..


d = [ 10,20.5, "python" ]


print (d)

print (d[0])

print (d[-1])

print (d[0:2])

#list in built methods..
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

d.append(100)
d.append(10)
print (d)

#d.clear()
#print (d)

print (d.count(10))
d.extend([90,80,70])
print (d)

print (d.index(10))

d.insert(2, "perl")
print (d)

d.pop()
print (d)

d.pop()
print (d)

d.remove('python')
print (d)

d.reverse()
print (d)

d.remove("perl")

d.sort()
print (d)














