import boto3
import psycopg2
import boto3


s3 = boto3.client('s3')
all_objects = s3.list_objects_v2(
    Bucket='capstone-test-sine', Prefix='country-data/')
print(all_objects)


def redshift(bucket_name):

    conn = psycopg2.connect(dbname='dev', host='capstone.colq4z94wwwe.eu-west-1.redshift.amazonaws.com',
                            port='5439', user='admin', password='SNOlimit#45')
    cur = conn.cursor()

    # Begin your transaction
    cur.execute("begin;")

    cur.execute("copy kpi_kpireport from 's3://clab-migration/kpi.csv' credentials 'aws_access_key_id=ID;aws_secret_access_key=KEY/KEY/pL/KEY' csv;")
    # Commit your transaction
    cur.execute("commit;")
    print("Copy executed fine!")


# redshift()
