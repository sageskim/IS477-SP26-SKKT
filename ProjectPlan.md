# IS 492 Milestone 2: Project Plan 📝

### 📋 Overview

This project is conducted for IS 477 Course Project by Sage Kim and Kyna Tyagi. It aims to explore the relationship between crop production, focusing on cereals, and countries’ GDP from 1961 to 2024. For a long time, agriculture has been considered one of the most important factors in economic growth across countries. According to the U.S. Department of Agriculture, the growth of agricultural total-factor productivity (TFP) has played an important role in economic development by helping reduce poverty and supporting farmers and rural communities. Furthermore, U.S. Chamber of Commerce states that “agriculture, food, and related industries contributed approximately $1.53 trillion to the U.S. economy, accounting for 5.6% of the total GDP” in 2023. In these ways, agriculture has significant impact on economics in both national and global ways. 

However, the agriculture industry includes many different items from animals to plants, and the major crops vary across countries. Therefore, we decided to narrow down our focus to cereals and explore their impact on economic development. Cereals, such as rice and wheat, are staple foods for many people around the world and have high levels of production and consumption. In addition, previous research found that cereal trade is positively related to urbanization. Therefore, we aim to explore the relationship between cereal production and GDP per capita over time using these datasets: the “Crops and livestock products” datasets which are total six datasets separated by continents provided by the Food and Agriculture Organization of the United Nations, and the “GDP per capita (current US$)” dataset provided by the World Bank Group.

### 👥 Team

#### Sage Kim

- Data cleaning and preprocessing
- Data matching and integration
- Visualization and exploratory analysis
- Documentation and report writing

#### Kyna Tyagi

- Data acquisition and dataset preparation
- Data restructuring and transformation (wide to long format) 
- Statistical analysis and interpretation
- Documentation and report writing

### 🔎 Research or Business Question(s)

### 📊 Datasets

### 🗓️ Timeline

### ⚠️ Constraints

One of the constraints of these datasets is the difficulty of joining them together. At first, our plan was to join them using the country code column that both datasets have. However, after skimming through the datasets, we found that one dataset uses numeric codes while the other uses alphabet codes. Therefore, an alternative way to join them is by using the country name. However, this approach might not be very smooth either. While both datasets list country names in rows, there are some inconsistent country names. For example, the crop production dataset refers to the U.S. as “United States of America,” while the World Bank dataset calls it “United States.” Furthermore, both datasets have some issues with country entities. For example, the crop production dataset includes two types of names for Mainland China which are “China” and “China, Mainland,” with different numeric area codes, which can be very confusing. Additionally, the World Bank dataset includes some non-country entities in the same column as the list of countries, such as “Africa Eastern and Southern,” “Low & middle income,” and “Not classified.” This dataset also contains many N/A values, which might affect our future analysis. In these ways, the datasets we plan to use are not complete or clean and require some manual cleaning before they can be used.

### 🕳️ Gaps
