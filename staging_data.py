import boto3
import psycopg2
import boto3


s3 = boto3.client('s3')


def redshift(file_name):

    conn = psycopg2.connect(dbname='dev', host='capstone.colq4z94wwwe.eu-west-1.redshift.amazonaws.com',
                            port='5439', user='admin', password='SNOlimit#45')
    cur = conn.cursor()

    # Begin your transaction
    cur.execute("begin;")

    cur.execute("copy kpi_kpireport from 's3://clab-migration/kpi.csv' credentials 'aws_access_key_id=ID;aws_secret_access_key=KEY/KEY/pL/KEY' csv;")
    # Commit your transaction
    cur.execute("commit;")
    print("Copy executed fine!")


def access_files(folder_name):

    all_objects = s3.list_objects(
        Bucket='capstone-test-sine', Prefix=folder_name, )

    for object in all_objects['Contents']:
        file_name = object['Key']
        if file_name.endswith('.csv'):
            return 's3://capstone/' + folder_name + file_name


if __name__ == "__main__":
    print(access_files('country-data/'))
