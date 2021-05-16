import boto3
import psycopg2
import boto3


s3 = boto3.resource('s3')
bucketName = 'capstone-test-sine'
bucket = s3.Bucket(bucketName)
for obj in bucket.objects.all():
    print(obj.key)


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


{'ResponseMetadata': {'RequestId': 'N22EXTQQZ4MEGRMF', 'HostId': 'NjqPkz7mzL1789i0ljgmf7fS6buK1tf5DJwNNwalrHyMpynfeeBy8lwKoDmDh6fTUCLNbBrTUys=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'NjqPkz7mzL1789i0ljgmf7fS6buK1tf5DJwNNwalrHyMpynfeeBy8lwKoDmDh6fTUCLNbBrTUys=', 'x-amz-request-id': 'N22EXTQQZ4MEGRMF', 'date': 'Sun, 16 May 2021 19:12:42 GMT', 'x-amz-bucket-region': 'eu-west-1', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 1}, 'IsTruncated': False,
    'Contents': [{'Key': 'country-data/', 'LastModified': datetime.datetime(2021, 5, 16, 15, 19, 36, tzinfo=tzlocal()), 'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', 'Size': 0, 'StorageClass': 'STANDARD'}, {'Key': 'country-data/country_codes.csv', 'LastModified': datetime.datetime(2021, 5, 16, 18, 31, 54, tzinfo=tzlocal()), 'ETag': '"16db7de697dae70d81d14800b4e7b6e2"', 'Size': 129984, 'StorageClass': 'STANDARD'}], 'Name': 'capstone-test-sine', 'Prefix': 'country-data/', 'MaxKeys': 1000, 'EncodingType': 'url', 'KeyCount': 2}
