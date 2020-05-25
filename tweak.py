#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[22]:


file=open("model.py","r")


# In[23]:


list=file.readlines()


# In[24]:


list


# In[25]:


var1=list[19]
a=len(var1)
var1


# In[26]:


var2=int(var1[2:a-1]) +1


# In[27]:


var2


# In[28]:


var1


# In[29]:


list[19]=var1[0:2]+str(var2)+var1[a-1:]


# In[30]:


list[19]


# In[31]:


list


# In[34]:


file2=open("model.py","w")


# In[35]:


file2.writelines(list)


# In[36]:


file.close()
file2.close()


# In[ ]:




