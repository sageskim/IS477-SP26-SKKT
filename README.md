# Cereal Production and Economic Development: Exploring the Relationship Between Agricultural Output and GDP per Capita (1961–2024)

## Contributors
- Sage Kim
- Kyna Tyagi

## Summary

[500-600 words] Description of your project, motivation, research question(s), and any findings.

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


