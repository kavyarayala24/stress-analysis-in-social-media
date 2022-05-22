#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd 
import numpy as np


# In[9]:


test = pd.read_csv (r"C:/Users/hp/Desktop/dreaddit-test.csv")# import dataset
test


# In[10]:


test.head() #first five rows


# In[35]:


train = pd.read_csv (r"C:/Users/hp/Desktop/dreaddit-train.csv")
train


# In[14]:


train.head()


# In[15]:



print(train.shape) # rows,columns


# In[16]:



print(test.shape)


# In[17]:


print(train.columns) #column name


# In[18]:


print(test.columns)


# In[19]:


train.tail()#showing last 5 rows


# In[20]:


test.tail()


# In[21]:


test.info()


# In[22]:


train.info()


# In[23]:


train.describe() 


# In[24]:


#catrgorical columns


# In[25]:


train.select_dtypes(include=['object']).columns.tolist()


# In[26]:


test.select_dtypes(include=['object']).columns.tolist()


# In[27]:


test.subreddit.value_counts() # it showing the all subreddit column name


# In[28]:


train.subreddit.value_counts() 


# In[29]:


train = train.drop(['subreddit', 'post_id', 'sentence_range'],axis = 1 ) #drop selected columns


# In[30]:


print(train.columns)


# In[31]:


test = test.drop(['text', 'id', 'label'],axis = 1 ) #drop selected columns


# In[32]:


print(test.columns)


# In[11]:


test.corr() #corelation


# In[ ]:





# In[21]:





# In[ ]:




