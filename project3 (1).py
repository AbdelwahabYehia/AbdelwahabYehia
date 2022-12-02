#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 20
b = 35
c = 15
def maximum (a , b , c):
    if a >= b and a >= c:
        print (a)
    
    elif b >= a and b >= c:
        print (b)
    
    else:
        print (c)
maximum(a,b,c)


# In[40]:


a= 40
b= 10
def cal(a,b):
    return a+b , a-b

cal(a,b)



# In[49]:


list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
list1 = []
list2 = []
for i in range(len(list0)):
    if i % 2 == 0:
        list1.append(list0[i])
    else:
        list2.append(list0[i])

def multi(h):
    result = 1
    for i in h:
        result *= i
    return result

def summ(h):
    result = 0
    for i in h:
        result += i
    return result

print(multi(list1),summ(list2))


# In[39]:


n=input("") 
l=n.split('-') 
l.sort() 
print('-'.join(l))


# In[ ]:




