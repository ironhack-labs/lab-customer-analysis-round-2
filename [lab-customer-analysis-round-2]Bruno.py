#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np


# In[32]:


marketing_costumer = pd.read_csv(r"C:\Users\Utilizador\Desktop\Labround2\lab-customer-analysis-round-2\files_for_lab\csv_files\marketing_customer_analysis.csv")
marketing_costumer


# In[33]:


marketing_costumer.shape


# In[34]:


cols = []
for i in range(len(marketing_costumer.columns)): 
    cols.append(marketing_costumer.columns[i].lower().replace(' ', '_'))
marketing_costumer.columns = cols
marketing_costumer


# In[46]:


marketing_costumer.dtypes


# In[47]:


marketing_costumer.isna()


# In[48]:


marketing_costumer.isna().sum()


# In[49]:


condition = marketing_costumer.isnull().any(axis = 1)
marketing_costumer[condition]


# In[50]:


marketing_costumer.isna().sum().sum()


# In[51]:


marketing_costumer.isna().sum() / len(marketing_costumer)


# In[52]:


marketing_costumer


# In[53]:


marketing_costumer["effective_to_date"] = pd.to_datetime(marketing_costumer["effective_to_date"])


# In[54]:


marketing_costumer["month"] = marketing_costumer["effective_to_date"].dt.month


# In[55]:


filtered_marketing_costumer = marketing_costumer[marketing_costumer["month"].isin([1, 2, 3])]


# In[56]:


filtered_marketing_costumer


# In[71]:


def transform_marketing_data(marketing_costumer):

    cols = [col.lower().replace(' ', '_') 
            for col in marketing_customer.columns]
    marketing_customer.columns = cols


    marketing_customer['effective_to_date'] = pd.to_datetime(marketing_customer['effective_to_date'])


    marketing_customer['month'] = marketing_customer['effective_to_date'].dt.month


    filtered_marketing_customer = marketing_customer[marketing_customer['month'].isin([1, 2, 3])]

    return filtered_marketing_customer


# In[76]:


filtered_marketing_costumer


# In[ ]:




