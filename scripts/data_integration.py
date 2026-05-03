#!/usr/bin/env python
# coding: utf-8

# # Data Integration
# **Team:** Sage Kim & Kyna Tyagi

# ## 0. Load Libraries & Data

# In[26]:


import pandas as pd
import numpy as np

fao = pd.read_csv('../data/processed/faostat-cereal-cleaned.csv')
wb  = pd.read_csv('../data/raw/worldbank_gdp_raw.csv', skiprows=4)


# ## 1. Explore Dataset

# In[27]:


print(fao.shape)
print(fao.dtypes)
fao.head()


# In[28]:


print(wb.shape)
print(wb.dtypes)
wb.head()


# ## 2. Country Name Mapping

# In[29]:


print('Countries:', wb['Country Name'].nunique())
print('Countries:', fao['Area'].nunique())


# In[30]:


print(wb['Country Name'].unique())


# In[31]:


print(fao['Area'].unique())


# In[32]:


for name in fao['Area'].unique():
    if name not in wb['Country Name'].values:
        print(name)


# In[33]:


fao[fao['Area'] == 'China']


# In[34]:


fao[fao['Area'] == 'China, mainland'].head()


# In[35]:


fao[fao['Area'] == 'China, Taiwan Province of']


# In[36]:


wb[wb['Country Name'] == 'China']


# In[37]:


country_name_map = {
    'Bolivia (Plurinational State of)': 'Bolivia',
    'China, mainland':                  'China',
    'Congo':                            'Congo, Rep.',
    'Gambia':                           'Gambia, The',
    'Palestine':                        'West Bank and Gaza',
    'Republic of Korea':                'Korea, Rep.',
    'Slovakia':                         'Slovak Republic',
    'United Republic of Tanzania':      'Tanzania',
}


# ## 3. Clean FAO Dataset

# In[38]:


drop_countries = ['China', 'China, Taiwan Province of', 'Czechoslovakia', 'Ethiopia PDR', 'USSR']
fao_clean = fao[~fao['Area'].isin(drop_countries)].copy()

fao_clean['Area'] = fao_clean['Area'].replace(country_name_map)

fao_clean = fao_clean[['Area', 'Year', 'Value', 'Flag', 'Flag Description']].copy()
fao_clean.columns = ['Country', 'Year', 'Cereal_Production_Value', 'Flag', 'Flag Description']

fao_clean


# ## 4. Reshape World Bank Dataset (Wide -> Long)

# In[39]:


year_cols = [c for c in wb.columns if c.isdigit()]

wb_long = wb.melt(
    id_vars=['Country Name', 'Country Code'],
    value_vars=year_cols,
    var_name='Year',
    value_name='GDP_per_capita_USD'
)

wb_long.columns = ['Country', 'Country_Code', 'Year', 'GDP_per_capita_USD']
wb_long['Year'] = wb_long['Year'].astype(int)

print(wb_long.shape)
wb_long


# ## 5. Merge Datasets

# In[40]:


merged = pd.merge(
    fao_clean,
    wb_long[['Country', 'Year', 'GDP_per_capita_USD']],
    on=['Country', 'Year'],
    how='inner'
)

print('Shape:', merged.shape)
print('Num of Countries:', merged['Country'].nunique())
print('Year range:', merged['Year'].min(), '~', merged['Year'].max())
merged


# ## 6. Check Merged Dataset

# In[41]:


print('Missing values:')
print(merged.isnull().sum())

print('\nDuplicate rows:', merged.duplicated().sum())

print('\nCountries in merged dataset:')
print((merged['Country'].unique()))


# ## 7. Save Merged Dataset

# In[42]:


merged.to_csv('../data/processed/merged_cereal_gdp.csv', index=False)

