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

def multiply(a,b):
	return (a+b)%257

def inverse(a): #Need to do this function
	return operators.inverse(int(a),inv)

def add(a,b):
	return (a+b)%257

def gauss256(A):
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
			c = multiply(A[k][i],inverse(A[i][i]))
			#c = -A[k][i]/A[i][i]
			for j in range(i, n+1):
				if i == j:
					A[k][j] = 0
				else:
					A[k][j] = add(A[k][j], multiply(c, A[i][j]))
					#A[k][j] += c * A[i][j]

	# Solve equation Ax=b for an upper triangular matrix A
	x = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		x[i] = multiply(A[i][n], inverse(A[i][i]))
		# x[i] = A[i][n]/A[i][i]
		for k in range(i-1, -1, -1):
			A[k][n] = add(A[k][n], multiply(A[k][i],x[i]))
			# A[k][n] -= A[k][i] * x[i]
	return x