import numpy as np
import operators
import dft

def generate28(k, rows):
	full = dft.generate255(operators.generateExponentials())
	t = np.array([]).reshape(0,255)
	for row in rows:
		t = np.vstack((t, full[row]))
	return t[:k,:k]	

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