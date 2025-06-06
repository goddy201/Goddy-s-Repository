#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\HP\Downloads\world_population.csv")


# In[4]:


df


# In[6]:


pd.set_option('display.float_format', lambda x:'%.2f' %x)


# In[8]:


df.info()


# In[9]:


df.describe()


# In[11]:


df.isnull().sum()


# In[12]:


df.nunique()


# In[16]:


df.sort_values(by= "2022 Population").head(10)


# In[17]:


df.sort_values(by= "2022 Population", ascending = False).head(10)


# In[18]:


df.sort_values(by= "World Population Percentage", ascending = False).head(10)


# In[19]:


df.corr()


# In[21]:


sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (20,7)

plt.show()


# In[24]:


df.groupby("Continent").mean().sort_values(by = "2022 Population", ascending = False)


# In[23]:


df[df['Continent'].str.contains('Oceania')]


# In[29]:


df.groupby("Continent").mean().sort_values(by = "2022 Population", ascending = False)


# In[37]:


df2 = df.groupby("Continent")[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by = "2022 Population", ascending = False)
df2


# In[35]:


df.columns


# In[38]:


df3 = df2.transpose()


# In[39]:


df3


# In[40]:


df3.plot()


# In[ ]:




