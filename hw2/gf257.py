import numpy as np

def generate257(k, rows):
	full = np.empty([256,256])
	full.fill(1)
	for r in range(1,256): #should go from 1 to 254 for 255 elements in each row 0,254
		for c in range(1,256):
			full[r,c] = (3**((c*r)%257))%257
	t = np.array([]).reshape(0,256)
	for row in rows:
		t = np.vstack((t, full[row]))
	return t[:k,:k]	