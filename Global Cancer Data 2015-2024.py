#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[3]:


df= pd.read_csv(r"C:\Users\HP\Desktop\special\MY DATASETS\global_cancer_patients_2015_2024.csv")
df.head(20)


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


import seaborn as sns


# In[7]:


import matplotlib.pyplot as plt


# In[9]:


df.describe().T


# In[12]:


plt.figure(figsize=(15,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()


# In[31]:


plt.figure(figsize=(10, 6))
sns.lineplot(df['Year'], df['Target_Severity_Score'], marker='o')

plt.title('Trend of Cancer Severity')
plt.xlabel('Year')
plt.ylabel('Target_Severity_Score')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[13]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler


# In[16]:


X = df[['Age','Smoking','Genetic_Risk','Air_Pollution','Alcohol_Use','Obesity_Level']]
y = df['Target_Severity_Score']


# In[17]:


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)


# In[20]:


ln = LinearRegression()


# In[21]:


ln.fit(X_train, y_train)


# In[23]:


Cdf = pd.DataFrame(ln.coef_,X.columns, columns = ['Coefficients'])
print(Cdf)


# In[24]:


predictions = ln.predict(X_test)


# In[26]:


sns.scatterplot(predictions, y_test)
plt.xlabel("Predictions")
plt.title("Evaluation of Linear Regression Model")


# In[27]:


print("Mean Absolute Error:", mean_absolute_error(y_test,predictions))
print("Mean Squared Error:", mean_squared_error(y_test,predictions))
print("R2 Score:", r2_score(y_test,predictions))


# In[28]:


residuals = y_test - predictions


# In[30]:


sns.displot(residuals, bins = 30, kde = True)


# In[39]:


X = df['Year'].values.reshape(-1, 1)
y = df['Target_Severity_Score'].values

model = LinearRegression()
model.fit(X, y)

future_years = np.arange(df['Year'].min(), df['Year'].max() + 6).reshape(-1, 1)
predictions = model.predict(future_years)

plt.figure(figsize=(10,6))
sns.lineplot(x=df['Year'], y=df['Target_Severity_Score'], marker='o', label='Observed')
plt.plot(future_years, predictions, linestyle='--', color='red', label='Forecast')
plt.xlabel('Year')
plt.ylabel('Target Severity Score')
plt.title('Observed and Forecasted Cancer Severity Score')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




