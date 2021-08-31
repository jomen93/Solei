import numpy as np 
import re

f = open("image10.txt", "r")
words = f.read()
words = words.split()

def get_cc(x):
	numbers=[]
	for i in range(len(x)):
		for j in x[i].split():
			try:
				if len(j) > 6 and len(j) <=10:
					numbers.append(int(j))
			except:
				pass
			
	numbers = np.array(numbers)
	u, c = np.unique(numbers, return_counts=True)
	if len(c) == 1 and c[0] == 1:
		return u
	else:
		return u[c>1]

def get_max(x):
	x = np.array(list(map(int, x)))
	return np.max(x)


def regex(word):
	save_options = []
	for iterator in range(len(word)):
		len_find = len(re.findall(r'[0-9]+', word[iterator]))
		words_find = re.findall(r'[0-9]+', word[iterator])
		#words_find = re.sub(r'(?<=\d)[,\.]','',words_find)
		if len_find != 0:
			#print(words_find)
			for j in words_find:
				if len(j) > 6 and len(j) <=10:
					if j not in save_options:
						save_options.append(j)
					else:
						pass
	# Remove mobile numbers 
	for k in range(len(save_options)):
		if(save_options[k][0] == "3" and len(save_options[k]) == 10):
			save_options.remove(save_options[k])

	if len(save_options) != 0:
		return get_max(save_options)
	else:
		return "Not found !"
	
	
	# return word
		
# Data to put conditionals about ID
# https://www.datosmundial.com/america/colombia/crecimiento-poblacional.php

