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

### 1. Data Acquisition
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

**Integrity Check**
Run `notebooks/data_profiling.ipynb` to verify file checksums stored in `data/raw/checksums.txt`

---

### 2. Run Notebooks in Order
1. `notebooks/data_profiling.ipynb` — SHA-256 checksum verification and data quality assessment
2. `notebooks/data_integration.ipynb` — Data cleaning and integration → outputs `data/processed/merged_cereal_gdp.csv`
3. `notebooks/data_analysis.ipynb` — Analysis and visualizations → outputs saved to `analysis/`

---

### 3. Software Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

## References

Formatted citations for any papers, datasets, or software used in your project.
