#!/usr/bin/env python
# coding: utf-8

# # Data Integration
# **Team:** Sage Kim & Kyna Tyagi
# 
# **Research Questions:**
# 1. How does agricultural production relate to economic development across countries?
# 2. Do countries with higher cereal production tend to have higher GDP per capita?
# 3. Has agricultural production growth contributed to economic growth over time?

# ## 0. Load Libraries & Data

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/processed/merged_cereal_gdp.csv')

print('Shape:', df.shape)
print('Countries:', df['Country'].nunique())
print('Year range:', df['Year'].min(), '~', df['Year'].max())
df.head()


# ## Q1. How does agricultural production relate to economic development across countries?

# In[2]:


df_q1 = df[['Cereal_Production_Value', 'GDP_per_capita_USD']].dropna()

corr = df_q1['Cereal_Production_Value'].corr(df_q1['GDP_per_capita_USD'])
print('Correlation between Cereal Production and GDP per capita:', round(corr, 4))


# In[3]:


plt.figure(figsize=(10, 6))
plt.scatter(df_q1['Cereal_Production_Value'], df_q1['GDP_per_capita_USD'], alpha=0.3, color='steelblue')
plt.xlabel('Cereal Production (tonnes)')
plt.ylabel('GDP per Capita (USD)')
plt.title('Cereal Production vs GDP per Capita (1961-2024)')
plt.tight_layout()
plt.savefig('../analysis/q1_scatter.png', dpi=150, bbox_inches='tight')
plt.show()


# ## Q2. Do countries with higher cereal production tend to have higher GDP per capita?

# In[4]:


country_avg = df.groupby('Country').agg(
    avg_production=('Cereal_Production_Value', 'mean'),
    avg_gdp=('GDP_per_capita_USD', 'mean')
).dropna()

median_production = country_avg['avg_production'].median()
country_avg['group'] = country_avg['avg_production'].apply(
    lambda x: 'High Production' if x >= median_production else 'Low Production'
)

group_gdp = country_avg.groupby('group')['avg_gdp'].mean()
print('Average GDP per capita by production group:')
group_gdp


# In[5]:


plt.figure(figsize=(7, 5))
group_gdp.plot(kind='bar', color=['steelblue', 'darkorange'], edgecolor='white')
plt.xlabel('Production Group')
plt.ylabel('Average GDP per Capita (USD)')
plt.title('Average GDP per Capita: High vs Low Cereal Production Countries')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../analysis/q2_bar.png', dpi=150, bbox_inches='tight')
plt.show()


# ## Q3. Has agricultural production growth contributed to economic growth over time?

# In[6]:


yearly = df.groupby('Year').agg(
    avg_production=('Cereal_Production_Value', 'mean'),
    avg_gdp=('GDP_per_capita_USD', 'mean')
).dropna()

yearly.head()


# In[7]:


fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(yearly.index, yearly['avg_production'], color='steelblue', label='Avg Cereal Production')
ax1.set_xlabel('Year')
ax1.set_ylabel('Avg Cereal Production (tonnes)', color='steelblue')

ax2 = ax1.twinx()
ax2.plot(yearly.index, yearly['avg_gdp'], color='darkorange', label='Avg GDP per Capita')
ax2.set_ylabel('Avg GDP per Capita (USD)', color='darkorange')

plt.title('Global Trends: Cereal Production and GDP per Capita (1961-2024)')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.tight_layout()
plt.savefig('../analysis/q3_trend.png', dpi=150, bbox_inches='tight')
plt.show()


# In[8]:


corr_time = df.groupby('Year').apply(
    lambda x: x['Cereal_Production_Value'].corr(x['GDP_per_capita_USD'])
).dropna()

plt.figure(figsize=(12, 5))
plt.plot(corr_time.index, corr_time.values, color='steelblue')
plt.axhline(y=0, color='gray', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.title('Yearly Correlation: Cereal Production vs GDP per Capita')
plt.tight_layout()
plt.show()

