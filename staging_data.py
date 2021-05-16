import boto3
import psycopg2
import boto3
import configparser
import os

config = configparser.ConfigParser()
config.read_file(open('dl.cfg'))

os.environ['AWS_ACCESS_KEY_ID'] = config.get('AWS', 'AWS_ACCESS_KEY_ID')
os.environ['AWS_SECRET_ACCESS_KEY'] = config.get(
    'AWS', 'AWS_SECRET_ACCESS_KEY')


s3 = boto3.client('s3')


def redshift(file_name):

    conn = psycopg2.connect(dbname='dev', host='redshift-cluster-1.colq4z94wwwe.eu-west-1.redshift.amazonaws.com:5439/dev',
                            port='5439', user='admin', password='SNOlimit#45')
    cur = conn.cursor()

    # Begin your transaction
    cur.execute("begin;")

    cur.execute("copy world_population_raw from '{}' credentials 'aws_access_key_id=AKIAVCRUEIGJFOD45EMK;aws_secret_access_key=u37ABJ6awN1rvJapP3PoEDVWNha7KBgBHaAvKxOF' delimiter ',' csv region 'eu-west-1';".format(
        file_name))
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
    file_name = access_files('world-population-data/')
    redshift(file_name)
