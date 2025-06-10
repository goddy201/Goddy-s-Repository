#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"C:\Users\HP\Downloads\Customer Call List.xlsx")
df


# In[4]:


df = df.drop_duplicates()


# In[5]:


df


# In[10]:


df


# In[12]:


#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip(".../_")
df


# In[16]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])


# In[17]:


df["Phone_Number"]


# In[18]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[19]:


df[["Street_Address","State","Zip_code"]] = df["Address"].str.split(',',2,expand=True)
df


# In[20]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[22]:


df = df.replace('N/a','')
df


# In[25]:


df = df.fillna('')
df


# In[26]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

df


# In[30]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)

#df
#df= df.dropna(subset ="Phone_Number"), inplace = True
df


# In[28]:


df = df.reset_index(drop=True)
df


# In[ ]:




