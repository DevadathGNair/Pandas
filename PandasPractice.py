#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[27]:


a = pd.Series(['Dev','CR7','Messi'])
a


# In[28]:


b = pd.DataFrame([[1,'Dev'],[2,'CR7']],columns=['age','name'])
b


# In[29]:


df = pd.read_csv('E:\\GUVI\\Guvi Course\\Day 7\\titanic.csv')
df


# In[30]:


df.head()


# In[31]:


df.tail()


# In[32]:


df.describe()


# In[33]:


df.info()


# In[34]:


df.isnull()


# In[35]:


df.isnull().sum()


# In[ ]:





# In[36]:


mean_df = df['Age'].mean()
mean_df


# In[37]:


df['Age'] = df['Age'].fillna(mean_df)


# In[38]:


a = df[['Age','Sex','PassengerId','Survived']]


# In[39]:


a


# In[41]:


a.to_csv('E:\\GUVI\\Guvi Course\\Day 7\\New.csv')


# In[42]:


df[df.index==7]


# In[43]:


df[df.index.isin(range(3,7))]


# In[44]:


df.loc[1]


# In[45]:


df.loc[10:15]


# In[46]:


df.loc[[10,34,56]]


# In[47]:


df.iloc[[100,120,140]]


# In[48]:


df.loc[10:15,['Age','Pclass','Survived']]


# In[49]:


df.query("Age>40")


# In[57]:


df_1 = df.query('(Age > 50) and (Sex == "female")')
df_1


# In[58]:


df.query('Pclass == 3')


# In[ ]:




