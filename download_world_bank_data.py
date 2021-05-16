import world_bank_data as wb
import pandas as pd

# Get World Population Data
pop_data = wb.get_series('SP.POP.TOTL', id_or_value='id')

# Convert to dataframe and save file locally
df = pop_data.to_frame()
pop_data_csv = 'country_population/world-population-data.csv'
df.to_csv(pop_data_csv)