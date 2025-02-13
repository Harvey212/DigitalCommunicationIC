from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

dd = loadmat('HW5-3.mat')

dat=dd['GSMRx']
see = np.array(dat)
data=see[0]
#print(data)
#################################
#R-1 ~ N+L-1
#
#Z{R-1}  = h0 X{R-1} + h1 X{R-2} + ... + h{R-1} X0
#
#Z{N+L-1} = h0 X{N+L-1} +h1 X{n+l-2} +....+h{R-1}  X{N+L-R}
##############################
x=[1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1]
N=16

st=61
##########################################
res0=0

for i in range(4, 20):
	z0 = data[(i+st)]
	x0 = x[i]

	res0 += z0*x0

h0 = res0/N
##########################

res1=0

for i in range(5, 21):
	z1 = data[(i+st)]
	x1 = x[(i-1)]

	res1 += z1*x1

h1 = res1/N
################################

res2=0

for i in range(6, 22):
	z2 = data[(i+st)]
	x2 = x[(i-2)]

	res2 += z2*x2

h2 = res2/N
#################################

res3=0

for i in range(7, 23):
	z3 = data[(i+st)]
	x3 = x[(i-3)]

	res3 += z3*x3

h3 = res3/N
#######################################

res4=0

for i in range(8, 24):
	z4 = data[(i+st)]
	x4 = x[(i-4)]

	res4 += z4*x4

h4 = res4/N
#####################################


print("h0: {}".format(h0))
print("h1: {}".format(h1))
print("h2: {}".format(h2))
print("h3: {}".format(h3))
print("h4: {}".format(h4))


################################################3
