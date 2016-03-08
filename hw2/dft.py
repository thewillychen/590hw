#Problem 2
#Discrete fourier transform
#k length message, n length code
import sys
import operators
import numpy as np

def init():
	lookups = operators.generateTables()
	expos = lookups[0]
	logs = lookups[1]
	inverse = lookups[2]
	print generate255(expos)

def generate255(expos):
	t = np.empty([255,255])
	t.fill(1)
	for r in range(1,255): #should go from 1 to 254 for 255 elements in each row 0,254
		for c in range(1,255):
			t[r,c] = expos[(c*r)%255]
	return t

#def generateTransform(n):
init()