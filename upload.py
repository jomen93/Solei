import os
import uuid
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import __version__
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


try:
	print("Azure Blob Storage v"+__version__+" - Python sample")
except Exception as ex:
	print("Exception:")
	print(ex)


# Credentials
storage_account_name = "databizocr"
key1 = "bNJ+owRF8uB2y6yLYScq3WpM/rU4oDmsSQuNjhDAxFcz1DtqTHxgGR0fJglq+s/4m+XFDZkWk6hwH4bpY+oBkw=="
connect_str = "DefaultEndpointsProtocol=https;AccountName=databizocr;AccountKey=bNJ+owRF8uB2y6yLYScq3WpM/rU4oDmsSQuNjhDAxFcz1DtqTHxgGR0fJglq+s/4m+XFDZkWk6hwH4bpY+oBkw==;EndpointSuffix=core.windows.net"

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


