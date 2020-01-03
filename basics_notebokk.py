#!/usr/bin/env python
# coding: utf-8

# In[2]:


a =  10 #int
print (type(a))

b = 90.5 #float
print (type(b))


# In[4]:


c = "python"
c = 'python'
c = '''python'''
print (type(c))


# In[8]:


#Type casting..
#converting one datatype to another datatype..
a = 10 #int
b = 20.5 #float
print (type(a))
print (type(b))

b = int(b)
print (type(b))

a > b #10>20.5

b = float(b)
print (type(b))


# In[9]:


a = 10 #int
b = 20.5 #float
print (type(a))
print (type(b))

a > int(b)  

print (type(a))
print (type(b))


# In[14]:


#int to float --> yes
#float to int --> yes

#int to string --> yes
a = 10
a = str(a)
print (type(a))

#string to int --> yes/No
b = "10"
b = int(b)
print (type(b))

'''
c= "pytohn"
c = int(c)
'''


# In[20]:


#operators
a = 10
b = 20

print ("addition is",a+b)
print ("mul is",a*b)
print ("value of a {} and value of b {} is {}".format(a,b,a-b))
print (b/a)


# In[22]:


a = "$"*10
print (a)

b = "-"*10
print (b)

