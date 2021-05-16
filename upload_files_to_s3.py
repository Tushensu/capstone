import os
import boto3
import pandas as pd
from pathlib import *
import datetime
import json
import glob

# Set useful data paths
home_path = Path.cwd()
temperature_data_path = home_path / 'climate-change-dataset'
co2_demissions_data = home_path / 'co2_emission_data'
country_data = home_path / 'country_population_data'

# Create amazon S3 resource
s3 = boto3.resource('s3')
data_bucket = 'capstone-sine-demo'

def transform_co2_file(co2_demissions_data, filename='co2_emission_data.json'):
    
    # Load file to JSON
    co2_file = open(filename,)
    co2_emissions = json.load(co2_file)

    # # Create JSON File for each country
    for i in co2_emissions:
        temp = co2_emissions[i]
        data = temp['data']
        new_data = []
        for x in data:
            x['country_name'] = i
            data_sub = {key: x[key] for key in x.keys() & {'year', 'country_name', 'co2'}}
            new_data.append(data_sub)

        with open(co2_demissions_data +'/' + i + '.json', 'w') as country_file:
            json.dump(new_data, country_file)


# Define file upload function
def upload_files_to_s3(s3_bucket, folder, ext1, ex2=''):
    for filename in os.listdir(folder):
        file_path = str(folder) + '/' + filename
        data = open(filename, 'rb')
        s3_path = s3_bucket + '/' + folder.relative_to(home_dir)
        s3.Bucket(s3_bucket + '/temperature-data').put_object(Key=filename, Body=data)


# Upload Temperature Data
upload_files_to_s3(data_bucket, temperature_data_path, '.csv')
upload_files_to_s3(data_bucket, co2_demissions_data, '.json')
upload_files_to_s3(data_bucket, country_data, '.csv')

# print('Uploading temperature data files to s3')
# for filename in os.listdir(temperature_data_path):
#     if filename.endswith('.csv') and filename.find('State') == -1 and filename.find('City') == -1:
#         file_path = str(temperature_data_path) + '/' + filename
#         s3_path = data_bucket + '/temperature-data'
#         upload_files_to_s3(s3_path, file_path)
# print('Successfully uploaded temperature data')


# for filename in os.listdir(co2_demissions_data):
#     if filename.endswith('.json'):
#         file_path = str(temperature_data_path) + '/' + filename
#         s3_path = data_bucket + '/co2-emissions-data'
#         upload_files_to_s3(s3_path, file_path)
# print('Successfully uploaded co2_emissions data')


# for filename in os.listdir(home_path):
#     if filename.endswith('.csv'):
#         file_path = str(temperature_data_path) + '/' + filename
#         s3_path = data_bucket
#         upload_files_to_s3(s3_path, file_path)

# print('Uploading co2 emission data file to s3')
# filename = 'co2_emission_data.json'
# data = open(str(filename, 'rb')
# s3.Bucket(data_bucket + '/co2-emission-data').put_object(Key=filename, Body=data)
# print('Successfully uploaded co2 emission data')
            
            
# print('Uploading world bank data file to s3')
# filename = 'world-population-data.csv'
# data = open(str(filename, 'rb')
# s3.Bucket(data_bucket + '/wb-population-data').put_object(Key=filename, Body=data)
# print('Successfully uploaded world bank data')
            
# print('Uploading world bank data file to s3')
# filename = 'world-population-data.csv'
# data = open(str(filename, 'rb')
# s3.Bucket(data_bucket + '/wb-population-data').put_object(Key=filename, Body=data)
# print('Successfully uploaded world bank data')