rule all:
    input:
        "data/raw/checksums.txt",
        "data/processed/merged_cereal_gdp.csv",
        "analysis/q1_scatter.png",
        "analysis/q2_bar.png",
        "analysis/q3_trend.png"

rule profiling:
    input:
        "data/raw/faostat_cereal_raw.csv",
        "data/raw/worldbank_gdp_raw.csv"
    output:
        "data/raw/checksums.txt"
    shell:
        "python scripts/data_profiling.py"

rule integration:
    input:
        "data/raw/faostat_cereal_raw.csv",
        "data/raw/worldbank_gdp_raw.csv"
        "data/raw/checksums.txt"
    output:
        "data/processed/merged_cereal_gdp.csv"
    shell:
        "python scripts/data_integration.py"

rule analysis:
    input:
        "data/processed/merged_cereal_gdp.csv"
    output:
        "analysis/q1_scatter.png",
        "analysis/q2_bar.png",
        "analysis/q3_trend.png"
    shell:
        "python scripts/data_analysis.py"
