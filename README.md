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
How does cereal production correlate with economic development across different nations?
Do countries with higher cereal production volumes typically exhibit higher GDP per capita?
Has the growth of agricultural production contributed significantly to economic growth on a longitudinal basis?
Data Integration and Methodology
Answering these questions required the integration of two large datasets: the FAOSTAT “Crops and Livestock Products” dataset from the Food and Agriculture Organization and the World Bank “GDP per capita (current US$)” dataset. Combining these sources was a significant technical undertaking that demanded rigorous data cleaning and standardization.
The primary challenge lay in the different data architectures used by each organization. The FAO dataset utilized M49 numeric area codes and a "long" format, while the World Bank used ISO alpha-3 country codes and a "wide" format with yearly columns. To resolve this, we reshaped the World Bank data using "melting" techniques to create a longitudinal structure. Furthermore, we had to reconcile inconsistent naming conventions, such as standardizing "Bolivia (Plurinational State of)" to "Bolivia", and handle complex cases like China, where the FAO provided multiple sub-entities that did not exist in the World Bank data. We also filtered out non-country entities, such as regional aggregates (e.g., "Low & middle income"), to ensure our analysis remained focused on individual sovereign states.
Key Findings and Conclusions
The results of our analysis were surprising and challenged our initial assumptions. We discovered that the relationship between cereal production and GDP per capita is significantly weaker than expected. The overall correlation coefficient was approximately -0.057, indicating almost no linear relationship between a country's cereal output and its relative wealth.
In fact, our findings showed that countries categorized as "high cereal producers" often had a lower average GDP per capita than those with lower production levels. This suggests that while cereal production is vital for food security and domestic stability, it is not a standalone predictor of high economic development. Wealthier nations often transition away from primary agricultural production toward high-value sectors like technology, finance, and manufacturing. Ultimately, this project demonstrates that while agriculture is the backbone of survival, economic growth is influenced by a much more complex web of social, political, and industrial factors. It also emphasizes that in the age of big data, the ability to clean, standardize, and critically interpret disparate datasets is essential for uncovering the reality behind economic trends.



## Data profile

[max 2000 words] For each dataset used, describe its structure, content, and characteristics. Specify the location of the dataset files in your project repository. Discuss any ethical or legal constraints associated with the data and explain how the datasets relate to your questions

## Data quality

[500-1000 words] Summary of the quality assessment.

## Data cleaning

[max 1000 words] Summarize the data cleaning operations you performed and explain how each operation addressed specific data quality issues in your datasets.

## Findings

[~500 words] Description of any findings including numeric results and/or visualizations.

## Future work

[~500-1000 words] Brief discussion of any lessons learned and potential future work.

## Challenges

[~500 words] Discuss the main challenges you encountered while working on the project.

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


