import numpy as np
import gf256
import gf257

def getCodewords(k, codewords):
	c = codewords
	kcol = np.zeros((k,1))
	rows = [0]*k
	idx = 0
	for indx, i in enumerate(c):
		if idx == k:
			break
		if i != -1:
			kcol[idx] = i
			rows[idx] = indx
			idx += 1
	return kcol, rows

def decode(k, codewords, gf):
	a = getCodewords(k, codewords)
	c = a[0]
	rows = a[1]
	#print c
	if gf == 256:
		t = gf256.generate256(k, rows)
	else:
		t = generate257(k, rows)
	#print t
	array = np.concatenate((t,c), axis=1)
	#print array
	return gf256.gauss256(array)

if __name__ == '__main__':
	code1 = [0, 180, 253, 87, 23, 236, 165, 202, 14, 244, 13, 93, 231, 54, 117, 97, 84, 225, 86, 51]
	k1 = 10
	print decode(k1,code1,256)

	code2 = [-1, 180, -1, 87, 23, -1, 165, 202, -1, 244, -1, 93, -1, 54, -1, 97, 84, 225, 86, 51]
	k2 = 10
	print decode(k2,code2,256)

	code3 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 233, -1, 8, 135, 81, 196, 212, 33, 109, 63, 38, 226, 217, 19, 108, 89, 96, 27, 51, 207, 198, 215, 250, 82, 105, 189, 231, 185, 202, 186, 196, 1256, 232, 201, 33, 102, 227, 201, 96, 180, 101, 246, 53, 118, 138, 239, 143, 252, 131, 121, 242, 180, 91, 234, 148, 3, 191, 95, 133, 4, 135, 90, 176, 103, 135, 226, 134, 226, 3, 8, 68, 173, 1, 4, 221, 154, 160, 185, 231, 44, 83, 250, 239, 187, 48, 140, 24, 19, 198, 157]	
	k3 = 26
	print decode(k3,code3,256)