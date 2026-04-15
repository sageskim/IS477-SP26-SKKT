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
![Workflow Diagram](docs/Workflow.png)
https://www.figma.com/board/R1xUgZgl0UOdnXB0rTz2XI/Workflow--Copy-?node-id=0-1&t=HXxbMVBX9XDEFLjD-1

#### Week 4 - Data Integration (In Progress)
Currently, during Week 4, we are merging the FAOSTAT and World Bank datasets using Python and Pandas. We are matching the datasets based on shared country and year identifiers while resolving inconsistencies in formatting and naming conventions.


### 📅 Timeline Status
We have been working on tasks during Weeks 1-3 of our project. Week 1 was the project setup, which included project planning, initializing the repository, and defining team roles. Week 2 was downloading our datasets for the project, which are the World Bank GDP data and FAOSTAT cereal datasets. We also drafted and edited our project plan according to our personal schedules and ongoing priorities. Week 3 consisted of establishing folder format within the repository, as well as implementing CSV naming conventions and storage scripts. This week, Week 4, we are working on Merging the FAOSTAT and World Bank datasets using Python and Pandas. Our remaining timeline is for Weeks 5-8. For Week 5, we plan to focus on data cleaning, which will include handling null and duplicate values, as well as columns in the datasets not related to oue analysis. During Week 6, our goal is to get into the actual analysis part of the project. This will be running different models to test correlations between cereal production and GDP and generate valuable insights/conclusions from the analysis. In Week 7, we will work on the documentation and Metadata of our project. For this, we will finalize Markdown reports, technical metadata, and reproducibility instructions. Finally, Week 8 will be our final submission week, where we will work on repository cleanup, final presentation preparations, and project submission. The project will be finalized and submitted by May 3rd.

### 🔄 Project Plan Changes

### ⚠️ Challenges & Problems

#### Challenge 1. 

Originally, we planned to join two datasets using a country code. However, we found that these two datasets using different types of country codes; FAO uses numeric code (e.g. Argentina = 32) which is also called Area Code (M49), and World Band uses ISO 3166-1 alpha-3 code (e.g. Argentina = ARG). Since these are two completely different standard, we were not able to join datasets using them. Therefore, we change our method to use country name and year to join these datasets, because both datasets have Country Name and Year data. 

#### Challenge 2. 

When we tried to join them using country name, we noticed that they have different numbers of countries in their datasets. While the FAO dataset contains only 71 countries, the World Bank dataset contains 266 countries. This is because the World Bank dataset includes non-country values such as “Africa Eastern and Southern” or “Low & middle income” under Country Name columns. Furthermore, we found that some countries are listed under different names in the two datasets. For example, while Bolivia is listed as “Bolivia” in World Bank Dataset, it is listed as “Bolivia (Plurinational State of)” in FAO datasets. Therefore, before joining them, we planned to identify different country names across the two datasets and change the values in the FAO dataset to match the country names in the World Bank dataset. After that, we will filter the World Bank dataset to only include countries that exist in the FAO dataset (so that non-country values and unmatched countries are automatically dropped), and finally join these datasets.


### 👥 Team Contributions
