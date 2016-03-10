import numpy as np

def generate257(k, rows):
	full = np.empty([256,256])
	full.fill(1)
	for r in range(0,256): #should go from 1 to 254 for 255 elements in each row 0,254
		for c in range(0,256):
			full[r,c] = (3**((c*r)%257))%257
	t = np.array([]).reshape(0,256)
	for row in rows:
		t = np.vstack((t, full[row]))
	return t[:k,:k]	

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	if a < 0:
		a = 257 +a
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def multiply(a,b):
	return (a*b)%257

def inverse(a):
	return modinv(a,257)

def add(a,b):
	return (a+b)%257

def minus(a,b):
	c =(a-b)%257
	if c >= 0:
		return c
	return (257+c)%257

def myGauss257(m):
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
			print multiply(inverse(m[col][col]), m[col][col])
			r = [multiply(rowValue, minus(257, multiply(m[row][col], inverse(m[col][col])))) for rowValue in m[col]]
			m[row] = [add(pair[0],pair[1]) for pair in zip(m[row], r)]
    print m

 #    n = len(m)
 #    x = [0 for i in range(n)]
	# for i in range(n-1, -1, -1):
	# 	x[i] = multiply(A[i][n], inverse(A[i][i]))
	# 	# x[i] = A[i][n]/A[i][i]
	# 	for k in range(i-1, -1, -1):
	# 		A[k][n] = minus(A[k][n], multiply(A[k][i],x[i]))
	# 		# A[k][n] -= A[k][i] * x[i]
	# return x

    # #now backsolve by substitution
    # ans = []
    # m.reverse() #makes it easier to backsolve
    # for sol in range(len(m)):
    #         if sol == 0:
    #             ans.append(m[sol][-1] / m[sol][-2])
    #         else:
    #             inner = 0
    #             #substitute in all known coefficients
    #             for x in range(sol):
    #                 inner += (ans[x]*m[sol][-2-x])
    #             #the equation is now reduced to ax + b = c form
    #             #solve with (c - b) / a
    #             ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    # ans.reverse()
    # return ans

def gauss257(A):
	n = len(A)

	for i in range(0, n):# Search for maximum in this column
		#print A
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
			#c = minus(257, multiply(A[k][i],inverse(A[i][i])))
			#c = -A[k][i]/A[i][i]
			for j in range(i, n+1):
				if i == j:
					A[k][j] = 0
				else:
					A[k][j] = minus(A[k][j], multiply(c, A[i][j]))
					#A[k][j] += c * A[i][j]

	# Solve equation Ax=b for an upper triangular matrix A
	x = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		x[i] = multiply(A[i][n], inverse(A[i][i]))
		# x[i] = A[i][n]/A[i][i]
		for k in range(i-1, -1, -1):
			A[k][n] = minus(A[k][n], multiply(A[k][i],x[i]))
			# A[k][n] -= A[k][i] * x[i]
	return x