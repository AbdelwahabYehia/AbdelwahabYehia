#!/usr/bin/env python
# coding: utf-8

# In[1]:


from array import *
def array_list(array_num):
    num_list = array_num.tolist()
    print(num_list)


array_num = array('i', [45,34,67])
array_list(array_num)


# In[2]:


import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)


# In[3]:


import numpy as np
a = np.array([[1,2], [3,5]])
x = 2 
print("Original array: ")
print(a)
print("Values bigger than 2 =", a[a>2])
print("Their indices are ", np.nonzero(a > 2))


# In[4]:


import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b


# In[5]:


import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# In[ ]:




