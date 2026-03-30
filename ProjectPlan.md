# IS 477 Milestone 2: Project Plan 📝

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

1. How does agricultural production relate to economic development across countries? 

2. Do countries with higher cereal production tend to have higher GDP per capita? 

3. Has agricultural production growth contributed to economic growth over time?

### 📊 Dataset Description
Our first dataset comes from the World Bank and contains GDP per capita (in USD) for all countries around the world. This dataset provides yearly economic data for countries around the world and is commonly used as a measure of economic development and average income levels. It includes variables such as country name, year, and GDP per capita. This dataset will allow us to compare economic development levels across countries and examine how they change over time.
Our second dataset comes from the FAO’s FAOSTAT database and contains cereal production quantity data for crops such as wheat, maize, rice, barley, and other cereals. This dataset reports the amount of cereal production in metric tons for each country and year, from 1961 to 2024. It provides us insight into agricultural productivity and food production levels across countries.
These two datasets complement each other because they provide different but related types of information. While the World Bank dataset measures worldwide economic development through GDP growth, while the FAO dataset measures worldwide agricultural production. Both datasets include the common variables of country and year, which allows us to later integrate them into a single dataset for analysis.
By linking the datasets using country and year as shared variables, we will be able to analyze how agricultural production relates to economic development across countries throughout the years. This new and integrated dataset will allow us to analyze whether countries with higher cereal production tend to have higher GDP per capita and whether increases in agricultural production over time are associated with economic growth.


### 🗓️ Timeline
The project will follow the data lifecycle model, beginning with data acquisition and progressing through storage, integration, cleaning, analysis, and documentation. 
#### Week 1 – Project Setup and Planning
In this week, our task was  Project planning and repository setup. 

#### Week 2 - Data Collection and Acquisition
Our task was to download the GDP per capita dataset from the World Bank and cereal production data from the Food and Agriculture Organization FAOSTAT portal. Document dataset sources, formats, and access methods.

Part 2 of this week's deliverable was outline a clear, structured project plan.

#### Week 3 - Data Storage and Organization
Task: Organize and document file storage
 Description: Implement a structured storage system for datasets and scripts. Define naming conventions and folder organization to ensure clarity and reproducibility.
 Responsible: Both team members
Organization approach:
Tabular CSV files for raw data
Processed datasets stored separately
Python scripts for data processing 

#### Week 4 -  Data Integration
Task: Combine datasets into a unified dataset
 Description: Use Python and Pandas to integrate the two datasets using shared attributes. The datasets will be merged based on country and year identifiers.
 Responsible:
Member 1: Data merging implementation
Member 2: Verification and testing


Deliverables:
Integrated dataset committed 

#### Week 5 – Data Quality Assessment and Cleaning
Task: Evaluate and clean data
Description: Assess dataset quality and address issues such as missing values, inconsistent country names, or formatting differences. Cleaning methods may include handling null values, removing duplicates, and editing column names.
 Responsible: Both team members
Deliverables:
Cleaned dataset
Documentation of data quality issues and fixes

#### Week 6 – Analysis and Workflow Automation
Task: Perform analysis and automate workflow
Description: Conduct analysis to explore relationships between cereal production and GDP per capita. Create an automated workflow using Python scripts so the data processing steps can be executed from raw data to final dataset.
Responsible:
Member 1: Analysis scripts
Member 2: Workflow automation
Deliverables:
Python scripts for analysis
Automated data processing workflow

#### Week 7 - Documentation, Metadata, and Reproducibility
Task: Final documentation and metadata creation
Description: Write metadata and documentation explaining the datasets, processing steps, and analysis methods. Ensure that another user can reproduce the workflow using the provided instructions and code.
Responsible: Both team members
Deliverables:
Final project report in Markdown
Metadata describing datasets and variables
Reproducibility instructions outlined

#### Week 8 – Final Review and Submission
Task: Final project completion and submission
Description: Review the repository, verify that all documentation is complete, and ensure the workflow runs correctly from raw data to final results.
Responsible: Both team members
Deliverables:
Final GitHub repository
Complete documentation and code
Final project report + presentation!


### ⚠️ Constraints

One of the constraints of these datasets is the difficulty of joining them together. At first, our plan was to join them using the country code column that both datasets have. However, after skimming through the datasets, we found that one dataset uses numeric codes while the other uses alphabet codes. Therefore, an alternative way to join them is by using the country name. However, this approach might not be very smooth either. While both datasets list country names in rows, there are some inconsistent country names. For example, the crop production dataset refers to the U.S. as “United States of America,” while the World Bank dataset calls it “United States.” 

Furthermore, both datasets have some issues with country entities. For example, the crop production dataset includes two types of names for Mainland China which are “China” and “China, Mainland,” with different numeric area codes, which can be very confusing. Additionally, the World Bank dataset includes some non-country entities in the same column as the list of countries, such as “Africa Eastern and Southern,” “Low & middle income,” and “Not classified.” This dataset also contains many N/A values, which might affect our future analysis. In these ways, the datasets we plan to use are not complete or clean and require some manual cleaning before they can be used.

### 🕳️ Gaps

The main gap of this project is that we might need additional indicators to explain a country’s economic growth, since crop production (or more specifically, cereal production) does not always impact it significantly. Even though we would be able to find some relationship between cereal production and economic development, it might be not enough to explain economic growth by itself. Other factors such as population or country’s socio-economic background might be needed to better understand this phenomenon. In addition, even if we observe a relationship between cereal production and GDP, it is difficult to judge whether it is a causation or merely correlation. These are the main gap of this project. 

Furthermore, the definition of “cereals” is quite broad and vague. The FAO dataset that we plan to use does not include cereals as a single category, but instead separates them into different types of cereals such as rice, oats, wheat, buckwheat, and so on. Therefore, we still need to conduct some additional research to confirm which types of cereals are included in this dataset and which crops we should consider as “cereals” in this project. Another gap is that this dataset might not fully reflect all cereal production during this period across the world.

### 🗒️ References

- Food and Agriculture Organization. (2024). FAOSTAT Crops and livestock products dataset.
https://www.fao.org/faostat/en/#data/QCL?countries=2,3,4,7,8,9,1,10,11,52,12,13,16,14,57,255,15,23,53,18,19,80,20,21,26,27,233,29,35,115,32,33,37,39,40,351,96,128,214,41,44,45,46,47,48,98,49,50,167,51,107,116,250,54,72,55,56,58,59,60,61,178,63,209,238,62,64,66,67,68,69,70,74,75,73,79,81,84,86,87,89,90,175,91,93,95,97,99,100,101,102,103,104,105,106,109,110,112,108,114,83,118,113,120,119,121,122,123,124,126,256,129,130,131,132,133,134,127,135,136,137,138,145,141,273,143,144,28,147,148,149,150,153,156,157,158,159,160,154,162,221,165,299,166,168,169,170,171,173,174,177,179,117,146,183,185,184,182,188,189,191,244,193,194,195,272,186,196,197,200,199,198,25,201,202,277,203,38,276,206,207,210,211,212,208,216,176,217,219,220,222,213,227,223,228,226,230,225,229,215,231,234,235,155,236,237,249,248,251,181&elements=2510&items=108&years=1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024&output_type=table&file_type=csv&submit=true

- Hoover, M., & Lucy, L. (2024). How agriculture supports the American economy and Main Street businesses. U.S. Chamber of Commerce. https://www.uschamber.com/security/agriculture-regulations/how-agriculture-supports-the-american-economy-and-main-street-businesses

- United States Department of Agriculture. (n.d.). Sustainable agricultural productivity growth: What, why, and how. https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/sustainability/sustainable-productivity-growth-coalition/sustainable-agricultural-productivity-growth-what-why-and-how#:~:text=“Continuing%20to%20make%20improvements%20to,Achieving%20Zero%20Hunger%20by%202030

- World Bank. (2024). GDP per capita (current US$).
https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
