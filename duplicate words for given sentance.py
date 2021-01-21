#!/usr/bin/env python
# coding: utf-8

# In[7]:


s="google is great and twitter is also great"
l= s.split()
k=[]
for i in l:
    if (s.count(i)>1 and (i not in k)or s.count(i)==1):
        k.append(i)
    print(' '.join(k))


# In[ ]:




