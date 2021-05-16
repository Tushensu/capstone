# Thsi sscript is responsible for downlaoding our 4 datasents 
# 1. Kaggle : Global Temperature
# 2. GitHub : CO2 Emissions
# 3. World Bank : Population data - via Python script
# 4. Datahub : Country Codes

# Download & unzip Kaggle dataset
kaggle datasets downlad -d
uzip climate-change-earth-surface-temperature-data.zip -d climate-change-dataset

# Download from GitHub
wget https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.json -O co2_emission_data.json

# Downlaod from World Bank
python3 download_world_bank_data.py

# Download from Datahub
wget https://datahub.io/core/country-codes/r/0.csv -O /country_population/country_codes.csv