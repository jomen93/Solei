import numpy as np 



def get_cc(x):
	numbers=[]
	for i in range(len(x)):
		try:
			if len(x[i]) > 6:
				numbers.append(int(x[i]))
		except:
			pass
			
	numbers = np.array(numbers)
	u, c = np.unique(numbers, return_counts=True)
	if len(c) == 1 and c[0] == 1:
		return u
	else:
		return u[c>1]

