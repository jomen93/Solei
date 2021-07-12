#  ===========================================================================
#  @file:   reading.py
#  @brief:  Reading images from source
#  @author: Johan Mendez
#  @date:   11/07/2021
#  @email:  johan.mendez@databiz.co
#  @status: Debug
#  @detail: version 1.0
#  ===========================================================================
import os
import cv2
import pytesseract
import keras_ocr
import numpy as np
from pytesseract import Output 

img_size = 800
# Cut images for speed up
speed_view = False


def Reading_jpg(datadir, categories):
	
	training_data = []
	labels        = []

	for category in categories:
		path      = os.path.join(datadir, category)
		class_num = categories.index(category)

		for i in os.listdir(path):
			if i != ".DS_Store":
				aux_path  = os.path.join(path, i)
				img_array = cv2.imread(aux_path, cv2.IMREAD_GRAYSCALE)

				try:
					if img_array == None:
						print("Can't read file !!")

				except:
					img_array = cv2.resize(img_array, (img_size, img_size))
					img_array = cv2.normalize(img_array, 
											  None, 
											  alpha=0, 
											  beta=1, 
											  norm_type=cv2.NORM_MINMAX, 
											  dtype=cv2.CV_32F)
					# print("Ready file {0:>5}".format(aux_path).replace(path, ""))
					training_data.append(img_array)
					labels.append(class_num)

	# standarize data

	return training_data, labels

def read_files_tesseract():
	
	datadir = "train"
	categories = ["TERMINACION_CONTRATO/", "LLAMADO_ATENCION/"]

	files = []

	for category in categories:
		path = os.path.join(datadir, category)
		class_num = categories.index(category)
		for i in os.listdir(path):
			if i != ".DS_Store":
				aux_path = os.path.join(path, i)
				print(aux_path.replace(path,""))
				files.append(aux_path)
	print("")
	return files

def pre_process_image(img, skip_dilate=False):
	"""Uses a blurring function, adaptive thresholding and dilation to expose the main features of an image."""

	# Gaussian blur with a kernal size (height, width) of 9.
	# Note that kernal sizes must be positive and odd and the kernel must be square.
	proc = cv2.GaussianBlur(img.copy(), (9, 9), 0)

	# Adaptive threshold using 11 nearest neighbour pixels
	proc = cv2.adaptiveThreshold(proc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

	# Invert colours, so gridlines have non-zero pixel values.
	# Necessary to dilate the image, otherwise will look like erosion instead.
	proc = cv2.bitwise_not(proc, proc)

	if not skip_dilate:
		# Dilate the image to increase the size of the grid lines.
		kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]],np.uint8)
		proc = cv2.dilate(proc, kernel)

	return proc 

def read_words_tesseract(file):
	# custom_config = r'-l spa --psm 3'
	custom_config = r"--psm 6 oem 0"
	img = cv2.imread(file)
	if speed_view == True:
		height, width = img.shape[:2]
		img = img[0: int(height/4) , int(width/2):-1]
	x = pytesseract.image_to_string(img, config=custom_config)
	x = x.split()
	return x 

def read_words_keras(file):
	pipeline = keras_ocr.pipeline.Pipeline(scale=4)
	img = [keras_ocr.tools.read(file)]
	x = pipeline.recognize(img)
	x = [a_tuple[0] for a_tuple in x[0]]
	return x

def get_boxes(file, CC):
	# custom_config = r'-l spa --psm 3'
	custom_config = r"--psm 6 oem 0"
	

	img = cv2.imread(file)
	if speed_view == True:
		height, width = img.shape[:2]
		img = img[0: int(height/4) , int(width/2):-1]
	d = pytesseract.image_to_data(img, config=custom_config,output_type=Output.DICT)
	n_boxes = len(d['level'])
	for i in range(n_boxes):
		if(d['text'][i] != ""):
			(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

	cv2.imwrite(str(CC)+".jpg", img)

def get_from_section(file):
	img = cv2.imread(file)
	height, width = img.shape[:2]
	
	region = img[0: int(height/4) , int(width/2):-1]
	cv2.imshow("img", region)
	cv2.waitKey(0)



