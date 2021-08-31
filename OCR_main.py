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
print(images_folder)
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
		CC1 = reconigzed.get_cc(words)
		CC2 = reconigzed.regex(words)
		print("Extracting CC ...")
		print("Primer Metodo = ", CC1)
		print("Segundo Metodo = ", CC2)
		#print(reconigzed.regex(words))


