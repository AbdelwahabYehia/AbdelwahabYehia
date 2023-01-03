#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests

page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

print(page.status_code)

print(page.content)


# In[ ]:




