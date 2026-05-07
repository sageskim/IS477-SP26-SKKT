#!/usr/bin/env python
# coding: utf-8

# # Data Profiling
# **Team:** Sage Kim & Kyna Tyagi

# ## 0. SHA-256 Checksum Verification

# In[14]:


import hashlib

def get_sha256(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

fao_hash = get_sha256('data/raw/faostat_cereal_raw.csv')
wb_hash  = get_sha256('data/raw/worldbank_gdp_raw.csv')

print('faostat_cereal_raw.csv :', fao_hash)
print('worldbank_gdp_raw.csv  :', wb_hash)

with open('data/raw/checksums.txt', 'w') as f:
    f.write(f'{fao_hash}  faostat_cereal_raw.csv\n')
    f.write(f'{wb_hash}  worldbank_gdp_raw.csv\n')


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

fao = pd.read_csv('data/raw/faostat_cereal_raw.csv')
wb  = pd.read_csv('data/raw/worldbank_gdp_raw.csv', skiprows=4)


# ---
# ## 1. FAO Dataset

# In[16]:


# Basic structure
print('FAO shape:', fao.shape)
print(fao.columns.tolist())
print(fao.dtypes)
fao.head()


# In[17]:


# Coverage
print('Num of Countries:', fao['Area'].nunique())
print('Year range:', fao['Year'].min(), '~', fao['Year'].max())


# In[18]:


# Missing Values
print(fao.isnull().sum())


# In[19]:


# Duplicates
print(fao.duplicated().sum())


# In[20]:


# Production Value Distribution (Outliers)
print(fao['Value'].describe().round(2))


# In[21]:


# Country Names
print((fao['Area'].unique()))


# ---
# ## 2. World Bank Dataset

# In[22]:


# Basic structure
print('World Bank shape:', wb.shape)
print(wb.columns.tolist())
print(wb.dtypes[:8])
wb.head()


# In[23]:


# Coverage
print('Num of Countries:', wb['Country Name'].nunique())
print('Num of Country Codes:', wb['Country Code'].nunique())
print('Year range: 1960 ~ 2025')


# In[24]:


# Missing values
print(wb.isnull().sum())


# In[25]:


# Duplicates
print(wb.duplicated().sum())


# In[26]:


# GDP Distribution by year
print(wb.describe())

