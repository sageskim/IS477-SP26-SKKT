# IS 477 Milestone 3: Status Report 📝

### 📋 Task Updates

#### Week 1 - Project Setup and Planning
During Week 1, we completed the initial setup of the project. This included establishing the GitHub repository, outlining the project scope, assigning team roles, discussing about the project topic.

Artifacts:
- `/README.md`

#### Week 2 - Data Collection and Acquisition
During Week 2, we downloaded the datasets used for our project, including the World Bank GDP per capita dataset and the FAOSTAT cereal production dataset. We also reviewed dataset formatting, developed our project plan, and documented it in ProjectPlan.md.

Artifacts:
- `/data/raw/worldbank_gpd_raw.csv`
- `/data/raw/foastat_cereal_raw.csv`
- `/ProjectPlan.md`

#### Week 3 - Data Storage and Organization 
During Week 3, we organized the repository structure by creating designated folders for raw data, processed data, notebooks, and documentation. We also implemented CSV naming conventions and standardized file storage organization for clarity and reproducibility.

Artifacts:
- GitHub Repository Structure
```text
project-repo/
│
├── data/
│   ├── raw/              # Original untouched datasets
│   └── processed/        # Cleaned/merged datasets
│
├── notebooks/            # Jupyter notebooks
│
├── docs/                 # Reports / workflow diagrams / screenshots
│
├── analysis/             # Exported visuals / final graphs / findings
│
├── README.md
├── ProjectPlan.md
└── StatusReport.md
```
- Workflow Diagram
![Workflow Diagram](docs/Workflow.png)
https://www.figma.com/board/R1xUgZgl0UOdnXB0rTz2XI/Workflow--Copy-?node-id=0-1&t=HXxbMVBX9XDEFLjD-1
- `/notebooks/data_integration.ipynb`
  
#### Week 4 - Data Integration (In Progress)
Currently, during Week 4, we are merging the FAOSTAT and World Bank datasets using Python and Pandas. We are matching the datasets based on shared country and year identifiers while resolving inconsistencies in formatting and naming conventions.


### 📅 Timeline Status
We have been working on tasks during Weeks 1-3 of our project. Week 1 was the project setup, which included project planning, initializing the repository, and defining team roles. Week 2 was downloading our datasets for the project, which are the World Bank GDP data and FAOSTAT cereal datasets. We also drafted and edited our project plan according to our personal schedules and ongoing priorities. Week 3 consisted of establishing folder format within the repository, as well as implementing CSV naming conventions and storage scripts. This week, Week 4, we are working on Merging the FAOSTAT and World Bank datasets using Python and Pandas. Our remaining timeline is for Weeks 5-8. For Week 5, we plan to focus on data cleaning, which will include handling null and duplicate values, as well as columns in the datasets not related to oue analysis. During Week 6, our goal is to get into the actual analysis part of the project. This will be running different models to test correlations between cereal production and GDP and generate valuable insights/conclusions from the analysis. In Week 7, we will work on the documentation and Metadata of our project. For this, we will finalize Markdown reports, technical metadata, and reproducibility instructions. Finally, Week 8 will be our final submission week, where we will work on repository cleanup, final presentation preparations, and project submission. The project will be finalized and submitted by May 3rd.

### 🔄 Project Plan Changes
Since submitting our project plan, our group has moved from the planning stage into the execution of the data analysis. We have encountered two main challenges that needed a revision of our original plan. Additionally, we have updated our data cleaning method to address the feedback we received on our project plan on missing values and data consistency.
Our main changed happened this week, Week 4 (Data Integration) due to two major challenges:
Challenge 1 was incompatible identifiers as initially, we planned to join the datasets using country codes. However, we discovered a mismatch, as the FAO dataset utilizes M49 numeric codes , while the World Bank utilizes ISO 3166-1 alpha-3 codes, which we only found out when encountering errors and then doing research on different types of data storing codes. Because these standards are not directly compatible, we have updated our plan to use a combined key of Country Name and Year to join the datasets.
Challenge 2 was entity mismatches, as the datasets vary significantly in scale, with the FAO dataset covering 71 specific countries, and the World Bank includes 266 entities, many of which are general regions. Furthermore, naming conventions for the datasets are different, resulting in semantic errors. To solve this, we have added a pre-processing Step: we will programmatically rename FAO values to match the World Bank's structure. We will then perform an inner join, filtering the World Bank dataset to include only the validated countries present in the FAO data, which removes non countries automatically.
Based on Milestone 2 feedback, we expanded our scope to address the "missingness" of data across the 1961–2024 period. To apply lecture teachings, we are implementing the following:
Discussion of Gaps: We have added a dedicated section to our final report to discuss how missing data points impact our findings. We will analyze whether these gaps are Missing Completely at Random, or if they represent a systematic bias, such as lower reporting in developing nations.
Course Alignment: By addressing these gaps, we are applying the course concept of Critical Data Studies, acknowledging that a "zero" or a "null" in cereal production might mean lack of infrastructure rather than a lack of farming.

### ⚠️ Challenges & Problems

#### Challenge 1. 

Originally, we planned to join two datasets using a country code. However, we found that these two datasets using different types of country codes; FAO uses numeric code (e.g. Argentina = 32) which is also called Area Code (M49), and World Band uses ISO 3166-1 alpha-3 code (e.g. Argentina = ARG). Since these are two completely different standard, we were not able to join datasets using them. Therefore, we change our method to use country name and year to join these datasets, because both datasets have Country Name and Year data. 

#### Challenge 2. 

When we tried to join them using country name, we noticed that they have different numbers of countries in their datasets. While the FAO dataset contains only 71 countries, the World Bank dataset contains 266 countries. This is because the World Bank dataset includes non-country values such as “Africa Eastern and Southern” or “Low & middle income” under Country Name columns. Furthermore, we found that some countries are listed under different names in the two datasets. For example, while Bolivia is listed as “Bolivia” in World Bank Dataset, it is listed as “Bolivia (Plurinational State of)” in FAO datasets. Therefore, before joining them, we planned to identify different country names across the two datasets and change the values in the FAO dataset to match the country names in the World Bank dataset. After that, we will filter the World Bank dataset to only include countries that exist in the FAO dataset (so that non-country values and unmatched countries are automatically dropped), and finally join these datasets.

#### Challenge 3. 
The third challenge we faced is the difference between data formats. While FAO dataset has a long format which has a country, year, and (Production) Value in a one row, World Bank dataset has a wide format which contains all year’s (1960, 1961, …, 2025)  GDP in a row. Therefore, it is impossible to simply join these two datasets, and we need to do “melting,” which converts the World Bank dataset from wide format to long format so that each row can represent one country and only one year.

#### Challenge 4. 
Another challenge is China. While World Bank Dataset only contains one type of China which is listed as “China,” FAO dataset contains three types of China: “China,” “China, mainland,” and “China, Taiwan Province of.” Since the meanings of these categories were very vague, we conducted a quick exploration, and found that World Bank Dataset’s China means Mainland China, and FAO dataset’s “China” showed basically the same data as Taiwan in the past, but later became the aggregated data of “China, mainland” and “China, Taiwan Province of.” Therefore, we decided not to use “China”  and “China, Taiwan Province of” data since these do not exist in world bank dataset, and map “China, mainland” as “China.”


### 👥 Team Contributions

Sage -  I developed and organized the GitHub repository structure, creating designated folders for raw data, processed data, notebooks, etc. I also created the project workflow diagram using Figma to visually present our processes and provide clear explanation about our sequences. Furthermore, I conducted initial exploration of both datasets to understand their structures and formats, and identify potential issues and challenges before the actual integration and analysis. For the StatusReport, I covered Task Updates and Challenges & Problems sections.

Kyna - I managed the data acquisition and dataset preparation process, finding the datasets while documenting their respective sources and access methods. To address the integration issues we faced, I developed the logic for our country-name mapping dictionary, specifically changing the M49 numeric codes and inconsistent naming conventions like those found for Bolivia and the United States. I also reacted to the response of our project plan feedback, changing our data quality strategy to address missing values and  gaps from 1961 to 2024. 
