#!/usr/bin/env python
# coding: utf-8

# # Data Profiling
# **Team:** Sage Kim & Kyna Tyagi

# ## 0. SHA-256 Checksum Verification

# In[7]:


import hashlib

def get_sha256(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

fao_hash = get_sha256('../data/raw/faostat_cereal_raw.csv')
wb_hash  = get_sha256('../data/raw/worldbank_gdp_raw.csv')

print('faostat_cereal_raw.csv :', fao_hash)
print('worldbank_gdp_raw.csv  :', wb_hash)

# Save checksums to file
with open('../data/raw/checksums.txt', 'w') as f:
    f.write(f'{fao_hash}  faostat_cereal_raw.csv\n')
    f.write(f'{wb_hash}  worldbank_gdp_raw.csv\n')

print('\nSaved to data/raw/checksums.txt')


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Load raw datasets
fao = pd.read_csv('../data/raw/faostat_cereal_raw.csv')
wb  = pd.read_csv('../data/raw/worldbank_gdp_raw.csv', skiprows=4)


# ---
# ## 1. FAO Dataset

# In[53]:


# Basic structure
print('FAO shape:', fao.shape)
print(fao.columns.tolist())
print(fao.dtypes)
fao.head()


# In[56]:


# Coverage
print('Num of Countries:', fao['Area'].nunique())
print('Year range:', fao['Year'].min(), '~', fao['Year'].max())


# In[ ]:


# Missing Values
print(fao.isnull().sum())


# In[40]:


# Duplicates
print(fao.duplicated().sum())


# In[ ]:


# Production Value Distribution (Outliers)
print(fao['Value'].describe().round(2))


# In[ ]:


# Country Names
print((fao['Area'].unique()))


# ---
# ## 2. World Bank Dataset

# In[55]:


# Basic structure
print('World Bank shape:', wb.shape)
print(wb.columns.tolist())
print(wb.dtypes[:8])
wb.head()


# In[59]:


# Coverage
print('Num of Countries:', wb['Country Name'].nunique())
print('Num of Country Codes:', wb['Country Code'].nunique())
print('Year range: 1960 ~ 2025')


# In[65]:


# Missing values
print(wb.isnull().sum())


# In[66]:


# Duplicates
print(wb.duplicated().sum())


# In[70]:


# GDP Distribution by year
print(wb.describe())

