import numpy as np
#where a = k in the message
def fft(a,w):
	if len(a) == 1:
		return a
	else:
		f_even = fft(a[::2], (w*w)%257)
		f_odd = fft(a[1::2], (w*w)%257)
		f = [0]*len(a)
		x = 1
		for i in range(0,len(a)/2):
			f[i] = (f_even[i] + ((x*f_odd[i])%257))%257
			f[i+len(a)/2] = (f_even[i] - ((x*f_odd[i])%257))%257
			x = (x * w)% 257
		return f

def pad(m):
	tm = [0]*256
	for idx, val in enumerate(m):
		tm[idx] = val
	return tm

if __name__ == '__main__':
	m1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	print fft(pad(m1), 3) 

	m2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67]
	print fft(pad(m2), 3)

	m3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67, 1, 1, 34, 45, 67, 23, 89, 53, 12, 54, 67]
	print fft(pad(m3), 3)
