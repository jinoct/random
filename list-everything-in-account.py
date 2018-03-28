# Author : Jino Thomas
#
#
import boto3

access_key = input("Enter AWS_ACCESS_KEY_ID: ")
secret_key = input("Enter AWS_SECRET_ACCESS_KEY: ")
session_token = input('Enter AWS_SESSION_TOKEN: ')
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, aws_session_token=session_token)
# Information on all the s3 buckets
print("S3 Information")
print("-----------------------------------------------------------------------------------------------------")
s3 = session.client('s3')
responsesets3 = s3.list_buckets()
for item in responsesets3['Buckets']:
    print([item][0]['Name'])
print('-----------------------------------------------------------------------------------------------------')
ec2 = session.client('ec2', region_name='us-west-2')
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
for region in regions:
    print("Region: {}".format(region))
# Information on all VPCs
    print("VPC Information")
    print("--------------------------------------------------------------------------------------------------")
    ec2 = session.client('ec2', region_name=region)
    responseset = ec2.describe_vpcs()
    for item in responseset['Vpcs']:
        print([item][0]['VpcId'], [item][0]['CidrBlock'])
# Information on all Dynamo DB Tables
    print("Dynamo DB information")
    print("--------------------------------------------------------------------------------------------------")
    ddb = session.client('dynamodb', region_name=region)
    responsesetddb = ddb.list_tables()
    for item in responsesetddb['TableNames']:
        print([item][0])
# Information on all RDS Instances
    print("RDS Information")
    print("--------------------------------------------------------------------------------------------------")
    rdsdb = session.client('rds',region_name=region)
    responsesetrds = rdsdb.describe_db_instances()
    for item in responsesetrds['DBInstances']:
        print([item][0]['DBInstanceIdentifier'])
#Information on all EMR clusters
    print("EMR Information")
    print("--------------------------------------------------------------------------------------------------")
    emrc = session.client('emr', region_name=region)
    responsesetemr = emrc.list_clusters()
    for item in responsesetemr['Clusters']:
        print([item][0]['Id'], [item][0]['Name'])