#!/usr/bin/env python
# coding: utf-8

# In[36]:


f = open("D:\interview\hello.txt")

print(f.read())


# In[37]:


f = open("D:\interview\hello.txt")

lines = f.readlines()

for i in lines[:1]:
    print(i,end=" ")


# In[39]:


f = open("D:\interview\hello.txt")

lines = f.readlines()

for i in lines[-2 :]:
    print(i,end=" ")


# In[42]:


f = open("D:\interview\hello.txt")

Data = f.read()

words = Data.split()
print(len(words))


# In[ ]:




