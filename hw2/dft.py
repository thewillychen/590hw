#Problem 2
#Discrete fourier transform
#k length message, n length code
import sys
import operators
import numpy as np

if __name__ == '__main__':
	lookups = operators.generateTables()
	expos = lookups[0]
	logs = lookups[1]
	inverse = lookups[2]
	fullTransform = generate255(expos)
	input1 = (10,20,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
	print dft(input1[0],input1[1],input1[2],fullTransform, expos, logs) 

	input2 = (26,100,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67])
	print dft(input2[0],input2[1],input2[2],fullTransform, expos, logs)

	input3 = (69,255,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67])
	print dft(input3[0],input3[1],input3[2],fullTransform, expos, logs)

def generate255(expos):
	t = np.empty([255,255])
	t.fill(1)
	for r in range(1,255): #should go from 1 to 254 for 255 elements in each row 0,254
		for c in range(1,255):
			t[r,c] = expos[(c*r)%255]
	return t

def generateTransform(n, t):
	return t[:n,:n]

def generateMessage(k, n, message):
	m = np.zeros((n,1))
	for idx, x in enumerate(message):
		m[idx,0] = x
	return m

def dft(k,n, message, fullTable, expos, logs):
	m = generateMessage(k,n,message)
	t = generateTransform(n,fullTable)
	code = np.zeros((n,1))
	for row in range(0,n):
		rowSum = 0
		for idx, val in enumerate(t[row]):
			product = operators.multiply(int(val), int(m[idx,0]), expos, logs)
			rowSum = operators.add(rowSum, product)
		code[row,0] = rowSum
	return code
