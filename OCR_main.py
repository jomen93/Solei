#  ===========================================================================
#  @file:   data_clean.py
#  @brief:  Main to consume API azure in computer vision 
#  @author: Johan Mendez
#  @date:   20/08/2021
#  @email:  johan.mendez@databiz.co
#  @status: Debug
#  @detail: version 1.0
#  ===========================================================================


import os
import uuid
import reconigzed

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import __version__
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

from msrest.authentication import CognitiveServicesCredentials

from PIL import Image
import sys 
import time 
import numpy as np



# Computer vision credentials
key1 = "7ab4b4c5cb484f038a506ed0a8eadc16"
key2 = "5b6b63738e9d497182b5fe356c48f4f4"
endpoint = "https://cveficacia.cognitiveservices.azure.com/"

# Authenticate the client
cv_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key1))

# get images
path = "train"
images = os.listdir(path)[10:]

images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), path)

for i in range(len(images)):
	print("reading "+images[i]+"...")
	if images[i] != ".DS_Store":
		read_image_path = os.path.join(images_folder, images[i])

		read_image = open(read_image_path, "rb")
		read_response = cv_client.read_in_stream(read_image, raw=True)
		read_operation_location = read_response.headers["Operation-Location"]
		operation_id = read_operation_location.split("/")[-1]

		# Call the "GET" API and wait for the retrieval of the results
		while True:
		    read_result = cv_client.get_read_result(operation_id)
		    if read_result.status.lower () not in ['notstarted', 'running']:
		        break
		    print ('Waiting for result...')
		    time.sleep(10)
		
		words = list()
		box = list()
		# Print results, line by line
		if read_result.status == OperationStatusCodes.succeeded:
		    for text_result in read_result.analyze_result.read_results:
		        for line in text_result.lines:
		        	words.append(line.text)
		        	box.append(line.bounding_box)
		        	#print(line.text)
		            #print(line.bounding_box)
		#f=open("image"+str(i)+".txt",'w')
		#for ele in words:
		#	f.write(ele+",")
		#f.close()
		np.savetxt("image"+str(i)+".txt", words, delimiter=',', fmt='%s')
		CC = reconigzed.get_cc(words)
		print("Extracting CC ...")
		print(CC)


azure = False

if azure == True:
	# Call the read API 
	# Read file using API, exctraction text
	print("Reading file ...")
	# get an image with text
	read_image_url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg"
	# Call API with URL and raw response
	read_response = cv_client.read(read_image_url, raw=True)

	# Get the operation location (URL with an ID at the end) from the response
	read_operation_location = read_response.headers["Operation-Location"]
	# Grab the ID from the URL
	operation_id = read_operation_location.split("/")[-1]

	# Call the "GET" API and wait for it to retrieve the results 
	while True:
	    read_result = cv_client.get_read_result(operation_id)
	    if read_result.status not in ['notStarted', 'running']:
	        break
	    time.sleep(1)

	# Print the detected text, line by line
	if read_result.status == OperationStatusCodes.succeeded:
	    for text_result in read_result.analyze_result.read_results:
	        for line in text_result.lines:
	            print(line.text)
	            print(line.bounding_box)
	print()





# Azure 
# Credentials
# storage_account_name = "databizocr"
# key1 = "bNJ+owRF8uB2y6yLYScq3WpM/rU4oDmsSQuNjhDAxFcz1DtqTHxgGR0fJglq+s/4m+XFDZkWk6hwH4bpY+oBkw=="
# connect_str = "DefaultEndpointsProtocol=https;AccountName=databizocr;AccountKey=bNJ+owRF8uB2y6yLYScq3WpM/rU4oDmsSQuNjhDAxFcz1DtqTHxgGR0fJglq+s/4m+XFDZkWk6hwH4bpY+oBkw==;EndpointSuffix=core.windows.net"

# Create the BlobServiceClient object which will be used to create a container client

# blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# # Create a unique name for the container
# container_name = str(uuid.uuid4())

# # Create the container
# container_client = blob_service_client.create_container(container_name)

# # Create a local directory to hold blob data
# local_path = "blob/data"
# # os.mkdir(local_path)

# # Create a file in the local data directory to upload and download
# local_file_name = str(uuid.uuid4()) + ".txt"
# upload_file_path = os.path.join(local_path, local_file_name)

# # Write text to the file
# file = open(upload_file_path, 'w')
# file.write("Hello, Worldo!")
# file.close()

# # # Create a blob client using the local file name as the name for the blob
# blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

# print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# # Upload the created file
# with open(upload_file_path, "rb") as data:
#     blob_client.upload_blob(data)


