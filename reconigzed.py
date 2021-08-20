import numpy as np 



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



# img = 48
# for k in range(img):

# 	with open("image"+str(k)+".txt") as f:
# 	    lines = f.readlines()

# 	numbers = []
# 	for i in range(len(lines)):
# 		for j in lines[i].split():
# 			try:
# 				if len(j) > 6 and len(j) <= 10:
# 					numbers.append(int(j))
# 			except:
# 				pass

# 	numbers = np.array(numbers)
# 	u, c = np.unique(numbers, return_counts=True)
# 	if len(c) == 1 and c[0] == 1:
# 		print(u)
# 	else:
# 		print(u[c>1])


