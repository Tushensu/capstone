import os
import boto3
from botocore.retries import bucket
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
s3 = boto3.client('s3')
data_bucket = 'capstone-test-sine'


def transform_co2_file(filename='co2_emission_data.json'):

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
            data_sub = {key: x[key]
                        for key in x.keys() & {'year', 'country_name', 'co2'}}
            new_data.append(data_sub)

        with open(str(co2_demissions_data) + '/' + i + '.json', 'w') as country_file:
            json.dump(new_data, country_file)


# Define file upload function
def upload_files_to_s3(s3_bucket, folder, ext1, ex2=''):
    for filename in os.listdir(folder):
        file_path = str(folder) + '/' + filename
        data = open(file_path, 'rb')
        s3_path = s3_bucket + '/' + str(folder.relative_to(home_path))
        s3.Bucket(
            s3_bucket + '/temperature-data').put_object(Key=filename, Body=data)


if __name__ == "__main__":
    transform_co2_file()

    print('Uploading temperature data files to s3')
    for filename in os.listdir(temperature_data_path):
        if filename.endswith('.csv') and filename.find('State') == -1 and filename.find('City') == -1:
            file_path = str(temperature_data_path) + '/' + filename
            data = open(file_path, 'rb')
            s3_path = data_bucket
            s3.put_object(Body=data, Bucket=s3_path,
                          Key='temperature-data/' + filename)
    print('Successfully uploaded temperature data')

    print('Uploading co2 emission data files to s3')
    for filename in os.listdir(co2_demissions_data):
        if filename.endswith('.json'):
            file_path = str(co2_demissions_data) + '/' + filename
            data = open(file_path, 'rb')
            s3_path = data_bucket
            s3.put_object(Body=data, Bucket=s3_path,
                          Key='co2-emissions-data/' + filename)
    print('Successfully uploaded co2_emissions data')

    print('Uploading country data files to s3')
    for filename in os.listdir(country_data):
        if filename.endswith('.csv') and filename.find('data') == -1:
            file_path = str(country_data) + '/' + filename
            data = open(file_path, 'rb')
            s3_path = data_bucket
            s3.put_object(Body=data, Bucket=s3_path,
                          Key='country-data/' + filename)
    print('Successfully uploaded country data')

    print('Uploading world population data files to s3')
    for filename in os.listdir(country_data):
        if filename.endswith('.csv') and filename.find('codes') == -1:
            file_path = str(country_data) + '/' + filename
            data = open(file_path, 'rb')
            s3_path = data_bucket
            s3.put_object(Body=data, Bucket=s3_path,
                          Key='world-population-data/' + filename)
    print('Successfully uploaded world population data')
