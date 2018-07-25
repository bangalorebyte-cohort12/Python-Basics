
# coding: utf-8

# In[2]:


import scipy


# # Integer 

# In[6]:


a = 1+1
print(hex(id(a)))
print(a)
print(type(a))


# # Floating Points

# In[13]:


b = 1.5
print(type(b))


# # Complex Numbers

# In[3]:


c = 1.5 + 0.5j 
print(type(a))
e = 2
print(type(e))
f = 0.5j
print(type(f))


# In[16]:


print(c.real)


# In[17]:


print(c.imag)


# # Boolean

# In[18]:


3 > 4


# In[4]:


test = 3 < 4
print(test)
print(type(test))


# # Basic Mathematical Operations

# In[30]:


# addition, multiplication, division and modulus operators
a = 3 + 5
b = 3 + 5 * 3 #follows BODMAS rules
c = 3/5 
d = 3%2 # this modulus operators return the remainder, often very useful
print(b)
print(c)
print(d)


# In[33]:


#converting to different numeric types
a = -1.2
print(int(a))
print(bool(a)) # python always defaults to True
b = -3
print(float(b))


# In[9]:


# examples of all built-in math operators
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3) 
print(1//6) # floor division
print(7%3) # modulus operator
print(3/6)
print(3//6)
print(3%6)
print(2**100)


# # Built-in Collection Types

# In[6]:


# list operators
myList = [1,2,3,4]
another_list = [6,7,8]
print(myList + another_list)
A = myList
print(A)
print(myList)
myList[2]=45
print(A)
print(myList)
print("Size of list:",len(A))
print("Membership:",5 in A)


# In[1]:


myList = [1,2,3,4]
another_list = [6,7,8]
print(myList + another_list)


# In[11]:


print(myList[1:3])


# In[12]:


# List methods
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)


# In[17]:


# lists vs string mutability

my_list = [1, 3, True, 6.5]
my_list[0]=2**10

my_string = "Uday"
print(my_string.center(10000))
#my_string[2] = "x"

# to change the contents of a string it must be set to another variable
change_string = my_string.replace(my_string,"j") 
print(change_string)



# In[18]:


list_of_words = "Hello, Welcome to Byte"
print(list_of_words.split())


# In[28]:


# Tuple operations
my_tuple = (2,True,4.8)
print(len(my_tuple))
my_tuple[:2]



# In[24]:


# Set operations
yourSet = {99,3,100}
print(type(yourSet))
mySet = {3,6,"cat",4.5,False}
"""
print(mySet)
print(False in mySet)
print("dog" in mySet)
print(mySet | yourSet)

# Set Methods


print(mySet.union(yourSet,mySet)) # same as | operator
print(mySet.intersection(yourSet,newSet)) # same as & operator
print(mySet & yourSet)"""

print(mySet.difference(yourSet))
print(mySet - yourSet)
print({3,100}.issubset(yourSet))

print({3,100}<=yourSet)
mySet.add("house")
print(mySet)
mySet.remove(4.5)
print(mySet)
print(mySet.pop())

print(mySet)


# In[ ]:


# to search for values in a dict
for i in range(len(myDict)):
    if myDict[i] == "Keith":
        return i
    
    


# In[32]:


# operations on Dictionaries

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)


# In[29]:


# Dictionary Methods

phoneext={'david':1410,'brad':1137}
keys = (phoneext.keys())


print(list(phoneext.keys()))

print(phoneext.values())
print(type(phoneext.values()))

print(type(list(phoneext.values())))

print(phoneext.items())

print(list(phoneext.items()))

print(phoneext.get("kent","NO ENTRY"))


