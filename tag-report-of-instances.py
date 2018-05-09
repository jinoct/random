#Script Info : Script to generate a report of the tags used for all EC2 instances in an account
#Input       : Access key, Secret Key & Session Token
#Author      : Jino Thomas


import boto3

access_key = input("Enter AWS_ACCESS_KEY_ID: ")
secret_key = input("Enter AWS_SECRET_ACCESS_KEY: ")

session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)

ec2 = session.client('ec2', region_name='us-west-2')
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

for region in regions:
	print()
	print("Region: {}".format(region))
	ec2 = session.client('ec2', region_name=region)
	responseset = ec2.describe_instances()
	for item in responseset['Reservations']:
		for instance in item['Instances']:
			print('-----------------------------------------------------------------------------------------------')
			print([instance][0]['InstanceId'])
			for tag in instance['Tags']:
				print([tag][0]['Key'],' : ', [tag][0]['Value'])
