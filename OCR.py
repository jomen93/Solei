#  ===========================================================================
#  @file:   data_clean.py
#  @brief:  Different Modules to clean data
#  @author: Johan Mendez
#  @date:   2/06/2021
#  @email:  johan.mendez@databiz.co
#  @status: Debug
#  @detail: version 1.0
#  ===========================================================================

# Program configuration
import reading
import reconigzed

import warnings
import os
import tensorflow.python.util.deprecation as deprecation
import numpy as np

datadir       = "train"
categories    = ["TERMINACION_CONTRATO/", "LLAMADO_ATENCION/"]



# debug flag
ignore_warnigs = True

# Active high Resolution
High_analysis = False

# Activate save boxed images
Save_boxes = True
# Garbage counter
G_flag = 0

# Ignore Warnings 
if ignore_warnigs == True:
	deprecation._PRINT_DEPRECATION_WARNINGS = False
	warnings.filterwarnings("ignore")

print("Reading files ...")
print(" ")

# Read files 
files = reading.read_files_tesseract()

# reading.get_from_section(files[0])

identified_docs = []
# creation garbage folder
if os.path.exists("Garbage") == False:
	os.makedirs("Garbage")
	print("Garbage Folder done ! ")



# for i in range(initial, len(files[:final+1])):
for i in range(len(files)):
	print("first level recognition ...")
	print("")
	# Character identification by the first method
	words = reading.read_words_tesseract(files[i])
	# ID extracted by the first method 
	CC    = reconigzed.get_cc(words)
	
	# When CC = 0 the first method don't work
	if len(CC) == 0:
		print(files[i]+" file is low resolution \U0001f630")
		if High_analysis == True:
			print("begins second level recognition ...")
			print("")
			# Character identification by the second method
			words = reading.read_words_keras(files[i])
			# ID extracted by the second method
			CC = reconigzed.get_cc(words)
				
	if os.path.exists(str(CC)) == False:
		if len(CC) != 0:
			os.makedirs(str(CC[0]))
			print("Folder "+str(CC[0])+" created")
			print("")
	
	# Se debe encontrar de que categoria es
	for j in range(len(categories)):
		if categories[j] in files[i]:
			if len(CC) != 0:
				final_path = files[i].replace(datadir+"/"+categories[j], str(CC[0])+"/")
			else:
				final_path = files[i].replace(datadir+"/"+categories[j], "Garbage/")

	print("Saving boxed image ...")
	if len(CC) != 0:
		reading.get_boxes(files[i], CC[0])
	else:
		reading.get_boxes(files[i], G_flag)
		G_flag += 1

	identified_docs.append(CC)
	os.rename(files[i], final_path)
	print("file "+files[i].replace(datadir,"")+" has ", CC)

	
	