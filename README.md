# Cereal Production and Economic Development: Exploring the Relationship Between Agricultural Output and GDP per Capita (1961–2024)

## Contributors
- Sage Kim
- Kyna Tyagi

## Summary

Introduction and Scope

Our project explores the historical and statistical relationship between cereal production and economic development across countries from 1961 to 2024. Agriculture has long been recognized as a foundational pillar of human civilization, playing a critical role in food security, employment, and international trade. Its economic significance remains undeniable. However, because "agriculture" is an incredibly broad category encompassing everything from timber to livestock, our study narrows its focus specifically to cereal production. Cereals, including wheat, rice, maize, and barley, are the primary staple foods for the majority of the global population and represent the largest sector of global agricultural output.

Motivation and Research Objectives

The core motivation for this study was to investigate whether agricultural productivity acts as a cause for economic advancement or if it remains a characteristic of developing economies. Many lower-income nations rely heavily on farming as their primary economic sector, while high-income nations are typically defined by industrial and service-oriented economies. We sought to understand if countries with high cereal output also tend to have higher GDP per capita, and whether growth in this sector consistently leads to broader national wealth over time.

To explore these themes, we structured our analysis around three central research questions:

1. How does cereal production correlate with economic development across different nations?
2. Do countries with higher cereal production volumes typically exhibit higher GDP per capita?
3. Has the growth of agricultural production contributed significantly to economic growth on a longitudinal basis?

Data Integration and Methodology

Answering these questions required the integration of two large datasets: the FAOSTAT “Crops and Livestock Products” dataset from the Food and Agriculture Organization and the World Bank “GDP per capita (current US$)” dataset. Combining these sources was a significant technical undertaking that demanded rigorous data cleaning and standardization.

The primary challenge lay in the different data architectures used by each organization. The FAO dataset utilized M49 numeric area codes and a "long" format, while the World Bank used ISO alpha-3 country codes and a "wide" format with yearly columns. To resolve this, we reshaped the World Bank data using "melting" techniques to create a longitudinal structure. Furthermore, we had to reconcile inconsistent naming conventions, such as standardizing "Bolivia (Plurinational State of)" to "Bolivia", and handle complex cases like China, where the FAO provided multiple sub-entities that did not exist in the World Bank data. We also filtered out non-country entities, such as regional aggregates (e.g., "Low & middle income"), to ensure our analysis remained focused on individual sovereign states.

Key Findings and Conclusions

The results of our analysis were surprising and challenged our initial assumptions. We discovered that the relationship between cereal production and GDP per capita is significantly weaker than expected. The overall correlation coefficient was approximately -0.057, indicating almost no linear relationship between a country's cereal output and its relative wealth.
In fact, our findings showed that countries categorized as "high cereal producers" often had a lower average GDP per capita than those with lower production levels. This suggests that while cereal production is vital for food security and domestic stability, it is not a standalone predictor of high economic development. Wealthier nations often transition away from primary agricultural production toward high-value sectors like technology, finance, and manufacturing. Ultimately, this project demonstrates that while agriculture is the backbone of survival, economic growth is influenced by a much more complex web of social, political, and industrial factors. It also emphasizes that in the age of big data, the ability to clean, standardize, and critically interpret disparate datasets is essential for uncovering the reality behind economic trends.



## Data profile

Our project examines the relationship between agricultural production and economic development across countries over time. Specifically, we focus on cereal production data from the Food and Agriculture Organization (FAO) and GDP per capita data from the World Bank to investigate whether countries with higher agricultural production also tend to have stronger economic performance. 
The project uses two primary datasets stored in the repository under the /data/raw/ directory. The first dataset is faostat_cereal_raw.csv, located at /data/raw/faostat_cereal_raw.csv. This dataset was downloaded from the FAOSTAT database and contains cereal production statistics for 71 countries between 1961 and 2024. The dataset originally contains 3,008 rows and 15 columns. Key columns include Area, Year, Value, Flag, and Flag Description. The Value column represents cereal production quantities measured in tonnes, while the Flag columns describe the quality or status of each observation, such as whether a value is official, estimated, or imputed. Additional metadata columns include item codes, domain descriptions, and country identifiers using the M49 numeric coding standard. During preprocessing, we removed rows flagged with "M" because those represented missing values and retained only the columns relevant to our analysis. We also standardized country names and cleaned whitespace issues using documented OpenRefine transformations stored in /docs/openrefine-history.json.

The FAO dataset has several important characteristics that affect our analysis. First, the dataset uses a long format where each row represents a single country-year observation. Second, the data contains substantial variation in cereal production values, ranging from 0 to over 6 million tonnes, producing a highly skewed distribution with large outliers. Third, the dataset includes estimated and imputed values, meaning that not all observations have the same reliability. Finally, some historical geopolitical entities such as the USSR and Czechoslovakia appear in the dataset, requiring additional cleaning decisions before integration with the World Bank data.

The second dataset is worldbank_gdp_raw.csv, located at /data/raw/worldbank_gdp_raw.csv. This dataset was downloaded from the World Bank Open Data portal and contains GDP per capita values in current U.S. dollars for 266 entities between 1960 and 2025. The dataset contains 266 rows and 71 columns. Unlike the FAO dataset, the World Bank dataset uses a wide format where each row represents a country and each year is stored as a separate column. Important columns include Country Name, Country Code, Indicator Name, and yearly GDP columns from 1960–2025. The Country Code column uses ISO 3166-1 alpha-3 country codes rather than the M49 numeric codes used by FAO.

The World Bank dataset also has characteristics that influenced our methodology. Many entries are not individual countries but rather aggregate regions or economic groups such as “Europe & Central Asia” or “Low income.” In addition, missing values increase in more recent years, particularly for 2024 and 2025. Because the dataset is stored in wide format, we reshaped it into long format using the Pandas melt() function before merging it with the FAO data.

The processed and integrated dataset produced from these sources is stored at /data/processed/merged_cereal_gdp.csv. This merged dataset contains 2,393 rows and 66 countries spanning 1961–2024. The merge was performed using country names and year values after country-name harmonization and filtering. We documented the data integration process in /notebooks/data_integration.ipynb.
There are relatively few legal restrictions associated with these datasets because both FAO and World Bank data are publicly available for research and educational use. However, ethical considerations, like we learned through lectures, still exist. Missing data and estimated values may disproportionately affect developing countries with weaker reporting infrastructure, potentially introducing systematic bias into the analysis. Additionally, aggregate economic indicators such as GDP per capita do not fully capture inequality, quality of life, or local agricultural conditions. We therefore treat our findings as exploratory correlations rather than definitive causal conclusions.

These datasets directly support our research questions by allowing us to compare agricultural production and economic indicators across countries and across time. The FAO data measures agricultural output, while the World Bank data measures economic development. Combining them enables us to investigate whether cereal production correlates with GDP per capita and whether agricultural growth trends align with broader economic growth patterns over the 1961–2024 period.


## Data quality

Our project included a detailed quality assessment of both the FAOSTAT cereal production dataset and the World Bank GDP per capita dataset before integrating them into a single analysis ready dataset. The goal of the quality assessment was to evaluate completeness, consistency, formatting, duplication, and potential biases that could affect the reliability of our findings. We documented these checks in /notebooks/data_profiling.ipynb and used the results to guide our preprocessing and cleaning decisions.
The first step of the quality assessment involved verifying dataset integrity using SHA-256 checksums. We generated hashes for both raw datasets and stored them in /data/raw/checksums.txt. This ensured that the raw files remained unchanged throughout the project workflow and improved reproducibility. The checksum verification confirmed that the exact same source files could be validated and reproduced later if needed.

For the FAOSTAT dataset (faostat_cereal_raw.csv), we first examined the dataset structure, dimensions, data types, and overall coverage. The dataset originally contained 3,008 rows and 15 columns representing cereal production observations for 71 countries between 1961 and 2024. Important variables included country names, M49 country codes, years, cereal production values, and metadata flags describing data quality. The profiling process showed that most columns contained no missing values, but the Value column contained 392 missing entries. Additionally, the Note column was mostly empty, containing 2,888 missing values. Because the Note column was not essential to the research questions and contained little usable information, it was excluded from later analysis.

We also checked for duplicate rows in the FAOSTAT dataset and found none. This indicated that each observation represented a unique country-year combination. We then explored the statistical distribution of cereal production values using descriptive statistics. The results revealed a highly skewed distribution with substantial outliers. Production values ranged from 0 to over 6 million tonnes, while the median value was only about 5,495 tonnes. This suggested that a small number of countries with extremely high production heavily influenced the mean. Recognizing this imbalance was important because it could weaken correlation analyses and visualizations by compressing smaller countries into a narrow range.

Another major quality issue in the FAOSTAT data involved country naming consistency and geopolitical entities. Several countries used names that did not directly match the World Bank dataset, including “Bolivia (Plurinational State of),” “Republic of Korea,” and “United Republic of Tanzania.” Historical entities such as “USSR,” “Czechoslovakia,” and “Ethiopia PDR” also appeared. In addition, the dataset contained multiple China-related categories (“China,” “China, mainland,” and “China, Taiwan Province of”), creating ambiguity during integration. To resolve these inconsistencies, we created a country-name mapping dictionary and removed entities that could not be accurately matched to the World Bank dataset. This standardization process was necessary to ensure a valid merge between datasets.

For the World Bank GDP dataset (worldbank_gdp_raw.csv), we conducted similar profiling steps. The dataset contained 266 rows and 71 columns, with yearly GDP per capita values stored in a wide format. Unlike the FAOSTAT dataset, the World Bank dataset included not only countries but also regional and economic aggregates such as “Europe & Central Asia,” “Low income,” and “World.” Because these aggregate entities did not correspond to the country-level agricultural data in FAOSTAT, they introduced inconsistency into the merge process. We addressed this issue by performing an inner join after filtering to countries that existed in the FAOSTAT dataset.
The World Bank dataset also contained increasing amounts of missing data in later years, especially for 2024 and 2025. The entire 2025 column contained only missing values, and the extra column Unnamed: 70 was completely empty. These columns were effectively irrelevant to the analysis. The missing values reflected the reality that more recent economic data is still being updated or reported by countries. Similar to the FAOSTAT dataset, no duplicate rows were found.

One of the largest structural quality issues involved differences in dataset format and identifier systems. The World Bank dataset used ISO 3166-1 alpha-3 country codes and stored years in separate columns, while the FAOSTAT dataset used M49 numeric codes and stored data in long format. Because these formats were incompatible, we reshaped the World Bank dataset into long format using Pandas melt() and relied on country names and years as merge keys after standardization. Although using country names introduces some risk of semantic mismatch, it was the most practical and reliable solution after extensive validation.

After cleaning and integration, the merged dataset contained 2,393 observations across 66 countries from 1961–2024. The final quality checks showed no duplicate rows and no missing values in the cereal production column, although 91 GDP per capita values remained missing. These remaining missing values reflect incomplete reporting in the original World Bank data rather than errors introduced during processing.

Overall, the quality assessment revealed that both datasets were generally reliable but required substantial preprocessing and integration before we could analyze it. The major issues involved inconsistent country identifiers, missing values, historical geopolitical entities, and structural differences between datasets. These were also identified from the feedback we got through our Project Plan. Addressing these challenges, improved the consistency, reproducibility, and validity of our final integrated dataset and allowed us to conduct meaningful analysis related to agricultural production and economic development.


## Data cleaning

Our data cleaning process focused on improving consistency, completeness, reproducibility, and compatibility between the FAOSTAT cereal production dataset and the World Bank GDP per capita dataset. All cleaning operations were documented in `/notebooks/data_integration.ipynb`, while manual transformations performed in OpenRefine were exported and preserved in `/docs/openrefine-history.json` to support transparency and reproducibility. The cleaned and merged dataset generated from these operations was saved as `/data/processed/merged_cereal_gdp.csv`.

The first cleaning operation involved verifying the integrity of the raw datasets using SHA-256 checksum validation. We generated checksums for both `faostat_cereal_raw.csv` and `worldbank_gdp_raw.csv` and stored them in `/data/raw/checksums.txt`. This ensured that the raw files remained unchanged throughout the workflow and allowed future users to verify that the same source files were used. This step directly supports reproducibility and transparency because anyone rerunning the project can confirm the authenticity of the datasets before executing the cleaning pipeline.

Next, we removed rows with missing production values from the FAOSTAT dataset. Specifically, we filtered out rows where the `Flag` column contained `"M"`, which represented missing values in the FAO reporting system. This operation reduced the dataset from 3,008 rows to 2,616 rows. Removing these rows addressed completeness issues by preventing null production values from interfering with analysis and visualizations. We preserved the remaining `Flag` and `Flag Description` columns because they provide important metadata regarding whether values are official, estimated, or imputed. Keeping these fields improves transparency by documenting the reliability of individual observations rather than silently discarding quality information.

We also cleaned formatting inconsistencies in the FAOSTAT dataset by trimming whitespace from the `Area` column using OpenRefine. Country-name inconsistencies can cause failed joins or duplicate categories during integration, so standardizing text formatting improved merge accuracy. We then reduced the FAO dataset to only the columns relevant for analysis: country identifiers, year, production value, and metadata flags. Removing unnecessary columns simplified the dataset structure and improved readability without losing information needed for the research questions.

One of the most important cleaning tasks involved harmonizing country names between datasets. The FAOSTAT dataset used naming conventions that differed from the World Bank dataset, including entries such as “Bolivia (Plurinational State of),” “Republic of Korea,” and “United Republic of Tanzania.” To address this issue, we created a country-name mapping dictionary that programmatically renamed FAO country values to match the World Bank naming conventions. For example, “Republic of Korea” was mapped to “Korea, Rep.” and “Gambia” was mapped to “Gambia, The.” This operation solved semantic inconsistencies that would otherwise prevent valid dataset integration.

We also removed historical or incompatible geopolitical entities that could not be consistently matched across datasets. Specifically, we excluded “USSR,” “Czechoslovakia,” and “Ethiopia PDR” because these entities no longer exist in the World Bank dataset. Another major cleaning issue involved China-related records. The FAOSTAT dataset contained separate categories for “China,” “China, mainland,” and “China, Taiwan Province of,” while the World Bank dataset only included a single “China” category. After exploratory comparison, we determined that “China, mainland” aligned most closely with the World Bank data, while the other categories introduced ambiguity and overlap. Therefore, we removed “China” and “China, Taiwan Province of” from the FAO dataset and mapped “China, mainland” to “China.” This decision improved consistency and prevented duplicate or misleading records during integration.

Another major data quality issue involved incompatible dataset structures. The FAOSTAT dataset used a long format where each row represented one country-year observation, while the World Bank dataset used a wide format with years stored as separate columns. Because these structures could not be directly merged, we reshaped the World Bank dataset into long format using the Pandas `melt()` function. This transformation converted yearly GDP columns into a single `Year` column paired with `GDP_per_capita_USD` values. Converting the dataset into long format standardized the structure across datasets and enabled integration using country and year identifiers.

We also addressed entity mismatch problems caused by the World Bank dataset including non-country aggregates such as “World,” “Low income,” and “Europe & Central Asia.” These entities did not correspond to the country-level agricultural data in FAOSTAT. Rather than manually removing all aggregate categories, we used an inner join during integration so that only countries appearing in both datasets were retained automatically. This approach reduced noise, improved consistency, and ensured that the merged dataset only contained comparable country-level observations.

After merging the datasets, we performed final quality validation checks. We checked for duplicate rows and confirmed that none existed in the merged dataset. We also assessed remaining missing values and found that 91 GDP per capita observations were still null due to incomplete reporting in the original World Bank data. Rather than imputing or artificially filling these values, we preserved them to avoid introducing unsupported assumptions into the analysis. This decision supports transparency and data integrity.

Overall, our cleaning workflow systematically addressed missing data, inconsistent identifiers, formatting issues, incompatible dataset structures, geopolitical ambiguities, and entity mismatches. All operations were documented through scripts, notebooks, and OpenRefine history files to ensure reproducibility and transparency. These cleaning steps produced a consistent and analysis-ready dataset that supports our research questions regarding the relationship between cereal production and economic development across countries over time.


## Findings

Our analysis focused on exploring the relationship between cereal production and economic development using the merged FAOSTAT and World Bank dataset. Specifically, we analyzed whether countries with higher cereal production tend to have higher GDP per capita and whether agricultural production growth appears related to economic growth over time. The final merged dataset contained 2,393 observations across 66 countries from 1961–2024.

For our first research question, we examined the overall relationship between cereal production and GDP per capita across all observations. Using Pandas correlation analysis, we calculated the correlation coefficient between Cereal_Production_Value and GDP_per_capita_USD. The result was approximately -0.0569, which indicates an extremely weak negative relationship between cereal production and GDP per capita. In other words, higher cereal production does not necessarily correspond to higher GDP per capita in our dataset. To visualize this relationship, we created a scatterplot showing cereal production on the x-axis and GDP per capita on the y-axis. The graph showed a very wide spread of points with no strong upward or downward trend, supporting the weak correlation result. The visualization also highlighted the presence of several extreme outliers where countries with very high cereal production did not always have high GDP per capita.

For our second research question, we grouped countries into “High Production” and “Low Production” categories based on whether their average cereal production was above or below the median production value. We then compared the average GDP per capita of each group. Surprisingly, the results showed that countries in the Low Production group actually had a higher average GDP per capita than countries in the High Production group. The average GDP per capita for high-production countries was about 11,492 USD, while the low-production countries averaged about 16,565 USD. This finding suggests that countries with stronger economies are not always the countries producing the largest amounts of cereal crops. One possible explanation is that many highly developed countries rely more heavily on service or industrial sectors rather than agriculture, while some large agricultural producers may still have lower average incomes. We visualized this comparison using a bar chart that clearly showed the GDP difference between the two production groups.

For our third research question, we explored trends over time by calculating yearly averages for cereal production and GDP per capita from 1961–2024. The trend analysis showed that both average cereal production and average GDP per capita generally increased over time, especially after the 1990s. This suggests that both agricultural output and economic development have grown globally during the observed period. However, the fact that both variables increased over time does not necessarily mean one directly caused the other. To better understand the relationship, we calculated yearly correlations between cereal production and GDP per capita for each year separately. These yearly correlations fluctuated around zero rather than showing a strong consistent positive trend. This indicates that the relationship between agricultural production and economic development changes over time and may depend on additional social, political, or economic factors not included in the dataset.

Overall, our findings suggest that cereal production alone is not a strong predictor of GDP per capita across countries. While agricultural production remains important, economic development appears to depend on many other factors beyond cereal output. The project also demonstrated the importance of data integration and cleaning because the analysis would not have been possible without resolving country-name inconsistencies, structural differences, and missing data issues between the two datasets.

## Future work

Throughout this project, we learned a lot about the challenges involved in working with real-world datasets, especially when integrating data from multiple sources. At the beginning of the project, we expected the process of combining the FAOSTAT cereal production dataset and the World Bank GDP dataset to be relatively straightforward. However, once we actually began the integration process, we discovered that there were many inconsistencies and structural differences that required additional cleaning, research, and planning before we could even begin the analysis phase.

One of the biggest lessons we learned was the importance of carefully exploring datasets before attempting integration or analysis. Early in the project, we originally planned to merge the datasets using country codes because that seemed like the most reliable method. However, after examining the data more closely, we realized that the FAOSTAT dataset used M49 numeric country codes while the World Bank dataset used ISO 3166-1 alpha-3 country codes. Since these coding systems were not directly compatible, our original integration plan failed. This taught us that even when two datasets appear related, their structures and standards may still differ significantly. Because of this issue, we had to redesign our integration strategy and instead merge the datasets using standardized country names and years.

Another important lesson involved the complexity of country naming conventions and geopolitical entities. During the cleaning process, we found several mismatches such as “Republic of Korea” versus “Korea, Rep.” and “Bolivia (Plurinational State of)” versus “Bolivia.” We also had to make decisions about historical entities like the USSR and ambiguous categories involving China and Taiwan. This showed us that data cleaning is not only a technical process but also requires critical thinking and careful justification for decisions. We learned that documenting these decisions clearly is extremely important for transparency and reproducibility.

We also learned the importance of being specific and intentional with our data analysis methods. At first, some of our analysis ideas were too broad, and we realized we needed to define clearer research questions and measurable outputs. Instead of only saying we would “analyze the relationship” between agriculture and GDP, we became more specific by calculating correlation coefficients, grouping countries by production levels, and generating yearly trend analyses. We also learned that visualizations can reveal patterns that simple summary statistics may not show clearly. For example, while the overall correlation between cereal production and GDP per capita was close to zero, the scatterplot and yearly trend graphs helped us better understand the variability and limitations of that relationship.

Another major lesson from this project was the value of feedback and iteration. After receiving TA feedback on our earlier milestones, we realized that we needed to improve how we addressed missing data and data quality concerns. In response, we expanded our quality assessment process and added more detailed discussion about missingness, estimated values, and potential reporting bias. We also improved our documentation by saving OpenRefine histories, recording checksum verification, and explaining our cleaning decisions more clearly in the notebooks and reports. Listening carefully to feedback helped us make the project more reproducible, transparent, and aligned with course expectations.

In terms of technical skills, this project gave us much more experience using Python, Pandas, and data transformation methods. We learned how to reshape datasets using `melt()`, perform joins across datasets with inconsistent identifiers, detect duplicates and missing values, and generate visualizations using Matplotlib. We also became more comfortable organizing a reproducible repository structure with separate folders for raw data, processed data, notebooks, analysis outputs, and documentation.

There are also several areas where the project could be expanded in the future. One improvement would be to include more agricultural variables beyond cereal production, such as crop yield, livestock production, or land use data. This would allow for a more complete analysis of how agriculture relates to economic development. Another possible extension would be to include additional economic indicators besides GDP per capita, such as poverty rates, unemployment, trade data, or Human Development Index (HDI) values. These variables could provide a broader understanding of development beyond income alone.

We also believe future work could improve the statistical methods used in the analysis. Our current project mainly focused on correlations and descriptive trends, but future research could apply regression models, time-series analysis, or clustering methods to better understand relationships between agriculture and economic growth. In addition, some countries had missing GDP data for certain years, so future work could explore more advanced methods for handling missingness or compare how different imputation techniques affect results.

Overall, this project taught us that data analysis involves much more than simply running code or generating graphs. Real-world data requires extensive cleaning, validation, documentation, and interpretation before meaningful conclusions can be made. It also reinforced the importance of reproducibility, transparency, and responding to feedback throughout the research process.

## Challenges

One of the biggest challenges we encountered during this project was integrating two datasets that were structured very differently from each other. At the beginning of the project, we assumed that merging the FAOSTAT cereal production dataset with the World Bank GDP dataset would be straightforward because both datasets contained country and year information. However, once we started working with the raw data, we discovered several compatibility problems that required major cleaning and restructuring before analysis could begin.

The first major challenge involved country identifiers. Originally, we planned to merge the datasets using country codes because that seemed like the most reliable method. However, we later discovered that the FAOSTAT dataset used M49 numeric country codes while the World Bank dataset used ISO 3166-1 alpha-3 country codes. Since these coding systems are completely different, the datasets could not be directly joined. Because of this, we changed our integration strategy and instead merged the datasets using country names and years. Although this solved the technical issue, it created additional problems involving inconsistent country names.

The second major challenge involved mismatched country names and geopolitical entities. Several countries had different names across the two datasets, such as “Republic of Korea” versus “Korea, Rep.” and “Bolivia (Plurinational State of)” versus “Bolivia.” The FAOSTAT dataset also included historical entities like “USSR” and “Czechoslovakia,” which no longer existed in the World Bank dataset. Another difficult issue involved China-related categories because the FAOSTAT dataset contained “China,” “China, mainland,” and “China, Taiwan Province of,” while the World Bank dataset only included one “China” category. To solve these problems, we created a country-name mapping dictionary and carefully decided which entities should be renamed, merged, or removed.

Another challenge involved differences in dataset structure. The FAOSTAT dataset used a long format where each row represented a single country-year observation, while the World Bank dataset used a wide format with separate columns for each year. Because of this mismatch, the datasets could not be merged directly. We had to reshape the World Bank dataset into long format using the Pandas `melt()` function before integration was possible.

Missing data and data quality issues were also challenging. The FAOSTAT dataset contained missing production values flagged with `"M"`, while the World Bank dataset had increasing amounts of missing GDP data in recent years. We had to decide carefully how to handle these missing values without introducing misleading assumptions into the analysis.

Another challenge was making the workflow reproducible and organized. Since the project involved multiple datasets, notebooks, scripts, and manual cleaning steps, we needed to document every operation clearly. This included saving OpenRefine histories, generating checksum verification files, organizing folders, and making sure scripts ran without errors. We also revised several parts of the project after receiving TA feedback, especially regarding missing data discussion and documentation quality.

Overall, the project showed us that real-world data analysis involves much more than just running code. Most of the work involved cleaning, validating, restructuring, and documenting the data before meaningful analysis could even begin.


## Reproducing

There are two ways to reproduce this project: 1. Running each notebook manually, or 2. using Snakemake to automate the entire workflow.

### Step 1: Data Acquisition (required for both methods)
Both datasets must be manually downloaded as programmatic access is not supported.

**FAO Cereal Production Dataset**
1. Visit: https://www.fao.org/faostat/en/#data/QCL
2. Select: Countries = All, Item = "Cereals n.e.c.", Element = "Production Quantity", Years = 1961–2024
3. Download as CSV
4. Save to `data/raw/faostat_cereal_raw.csv`

**World Bank GDP per Capita Dataset**
1. Visit: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
2. Download as CSV
3. Save to `data/raw/worldbank_gdp_raw.csv`

### Step 2: Install Required Software (required for both methods)
```bash
pip install -r requirements.txt
```

### Option A: Run Notebooks Manually
1. `notebooks/data_profiling.ipynb` — SHA-256 checksum verification and data quality assessment
2. `notebooks/data_integration.ipynb` — Data cleaning and integration
3. `notebooks/data_analysis.ipynb` — Analysis and visualizations

### Option B: Automated Workflow with Snakemake
```bash
pip install snakemake
snakemake --cores 1
```

## References

#### Datasets

- Food and Agriculture Organization. (2024). FAOSTAT Crops and livestock products dataset. https://www.fao.org/faostat/en/#data/QCL
- World Bank. (2024). GDP per capita (current US$). https://data.worldbank.org/indicator/NY.GDP.PCAP.CD

#### Papers / Software

- Anthropic. (2024). Claude (claude.ai). Used as an AI assistant to support code development and debugging. https://claude.ai
  
- Harris, C. R., et al. (2020). NumPy. https://numpy.org

- Hoover, M., & Lucy, L. (2024). How agriculture supports the American economy and Main Street businesses. U.S. Chamber of Commerce. https://www.uschamber.com/security/agriculture-regulations/how-agriculture-supports-the-american-economy-and-main-street-businesses

- Hunter, J. D. (2007). matplotlib. https://matplotlib.org

- McKinney, W. (2010). pandas. https://pandas.pydata.org

- OpenRefine. (2024). OpenRefine (3.x). https://openrefine.org

- Python Software Foundation. (2024). Python (3.x). https://www.python.org

- United States Department of Agriculture. (n.d.). Sustainable agricultural productivity growth: What, why, and how. https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/sustainability/sustainable-productivity-growth-coalition/sustainable-agricultural-productivity-growth-what-why-and-how


