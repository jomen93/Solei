import os
import uuid
import sys 

from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings
from azure.storage.filedatalake import DataLakeServiceClient

account_name = "datalakeocr"
account_key  = "Rrw9bv8GAkK+NvJYQMd+ZdVZe/HUKLFwgeKE2/8P5N2R4FbaYgN3aqXzphDIuDCrR/cbYN0c5u7vNBNMMHWLNw=="
connection_string = "DefaultEndpointsProtocol=https;AccountName=datalakeocr;AccountKey=Rrw9bv8GAkK+NvJYQMd+ZdVZe/HUKLFwgeKE2/8P5N2R4FbaYgN3aqXzphDIuDCrR/cbYN0c5u7vNBNMMHWLNw==;EndpointSuffix=core.windows.net"


make_container = True
make_directory = True

# function to account conection
def initialize_storage_account(account_name, account_key):
	try:
		global service_client

		service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", account_name), credential=account_key)
	except Exception as e:

		print(e)

# function to Make a container
def create_file_system(container_name):
	try:
		global file_system_client
		file_system_client = service_client.create_file_system(file_system=container_name)
	except Exception as e:
		print(e)

# function to create a folder
def create_directory(directory, container_name):
	file_system_client = service_client.get_file_system_client(file_system=container_name)
	try:
		file_system_client.create_directory(directory)
	except Exception as e:
		print(e)

# function to upload images to repository in datakake 
def upload_file_to_directory(container_name, directory, filename):
	try:

		file_system_client = service_client.get_file_system_client(file_system=container_name)

		directory_client = file_system_client.get_directory_client(directory)

		file_client = directory_client.create_file(filename)
		


		with open("train/"+filename,'rb') as f:
			file_contents = f.read()

		#file_contents = local_file.read()

		file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

		file_client.flush_data(len(file_contents))

	except Exception as e:
		print(e)		




# # Make the conection
initialize_storage_account(account_name, account_key)
print("Connection successful")

# Create a container 
container_images = "images1"
create_file_system(container_images)
print("Create a "+container_images+" container")

# Create a repository
repository_name = "train"
create_directory(repository_name, container_images)
print("Create a "+repository_name+" repository")

# Upload images
images_names = os.listdir("train")
if ".DS_Store" in images_names:
	images_names.remove(".DS_Store")
	
for i in range(len(images_names)):
	upload_file_to_directory(container_images, repository_name, images_names[i])
	print("Upload "+images_names[i]+" done!")






