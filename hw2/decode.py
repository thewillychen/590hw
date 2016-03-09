import numpy as np
import operators
import dft

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

def generate257(k):
	t = np.empty([256,256])
	t.fill(1)
	for r in range(1,256): #should go from 1 to 254 for 255 elements in each row 0,254
		for c in range(1,256):
			t[r,c] = (3**((c*r)%257))%257
	return t[:k,:k]

def decode(k, codewords, gf):
	a = getCodewords(k, codewords)
	c = a[0]
	rows = a[1]
	#print c
	if gf == 256:
		full = dft.generate255(operators.generateExponentials())
		print full.shape
		t = np.array([]).reshape(0,255)
		for row in rows:
			t = np.vstack((t, full[row]))
		t=t[:k,:k]
	else:
		t = generate257(k)
	#print t
	array = np.concatenate((t,c), axis=1)
	#print array
	return gauss28(array)

def multiply28(a,b):
	expos = operators.generateExponentials()
	logs = operators.generateLogarithms()
	return operators.multiply(int(a),int(b),expos,logs)

def inverse28(a):
	inv = operators.generateInverses()
	return operators.inverse(int(a),inv)

def add28(a,b):
	return operators.add(int(a),int(b))

def gauss28(A):
	n = len(A)

	for i in range(0, n):# Search for maximum in this column
		maxEl = abs(A[i][i])
		maxRow = i
		for k in range(i+1, n):
			if abs(A[k][i]) > maxEl:
				maxEl = abs(A[k][i])
				maxRow = k

		# Swap maximum row with current row (column by column)
		for k in range(i, n+1):
			tmp = A[maxRow][k]
			A[maxRow][k] = A[i][k]
			A[i][k] = tmp

		# Make all rows below this one 0 in current column
		for k in range(i+1, n):
			c = multiply28(A[k][i],inverse28(A[i][i]))
			#c = -A[k][i]/A[i][i]
			for j in range(i, n+1):
				if i == j:
					A[k][j] = 0
				else:
					A[k][j] = add28(A[k][j], multiply28(c, A[i][j]))
					#A[k][j] += c * A[i][j]

	# Solve equation Ax=b for an upper triangular matrix A
	x = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		x[i] = multiply28(A[i][n], inverse28(A[i][i]))
		# x[i] = A[i][n]/A[i][i]
		for k in range(i-1, -1, -1):
			A[k][n] = add28(A[k][n], multiply28(A[k][i],x[i]))
			# A[k][n] -= A[k][i] * x[i]
	return x

if __name__ == '__main__':
	code1 = [0, 180, 253, 87, 23, 236, 165, 202, 14, 244, 13, 93, 231, 54, 117, 97, 84, 225, 86, 51]
	k1 = 10
	print decode(k1,code1,256)

	code2 = [-1, 180, -1, 87, 23, -1, 165, 202, -1, 244, -1, 93, -1, 54, -1, 97, 84, 225, 86, 51]
	k2 = 10
	print decode(k2,code2,256)

	code3 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 233, -1, 8, 135, 81, 196, 212, 33, 109, 63, 38, 226, 217, 19, 108, 89, 96, 27, 51, 207, 198, 215, 250, 82, 105, 189, 231, 185, 202, 186, 196, 128, 232, 201, 33, 102, 227, 201, 96, 180, 101, 246, 53, 118, 138, 239, 143, 252, 131, 121, 242, 180, 91, 234, 148, 3, 191, 95, 133, 4, 135, 90, 176, 103, 135, 226, 134, 226, 3, 8, 68, 173, 1, 4, 221, 154, 160, 185, 231, 44, 83, 250, 239, 187, 48, 140, 24, 19, 198, 157]	
	k3 = 26
	print decode(k3,code3,256)