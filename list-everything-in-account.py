# Author : Jino Thomas
#
#
import boto3

access_key = input("Enter AWS_ACCESS_KEY_ID: ")
secret_key = input("Enter AWS_SECRET_ACCESS_KEY: ")
session_token = input('Enter AWS_SESSION_TOKEN: ')
session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, aws_session_token=session_token)

ec2 = session.client('ec2', region_name='us-west-2')
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
for region in regions:
    print("Region: {}".format(region))
    ec2 = session.client('ec2', region_name=region)
    responseset = ec2.describe_vpcs()
    for item in responseset['Vpcs']:
        print([item][0]['VpcId'], [item][0]['CidrBlock'])
