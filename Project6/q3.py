from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
from mpl_toolkits.mplot3d import Axes3D

indmap = dict()
indmap[3 + 3j] = 0
indmap[1 + 3j] = 1
indmap[-1 + 3j] = 2
indmap[-3 + 3j] = 3

indmap[3 + 1j] = 4
indmap[1 + 1j] = 5
indmap[-1 + 1j] = 6
indmap[-3 + 1j] = 7

indmap[3 -1j] = 8
indmap[1 -1j] = 9
indmap[-1 -1j] = 10
indmap[-3 -1j] = 11

indmap[3 - 3j] = 12
indmap[1 - 3j] = 13
indmap[-1 - 3j] = 14
indmap[-3 - 3j] = 15


##########################################################################################
#(3a)
#################################################################3
dd = loadmat('HW6-1b.mat')

dat=dd['Hmatrix']
dat2=dd['yprime']
H = np.array(dat)
Y = np.array(dat2)


##########################################3
xi=[-3,-1,1,3]
xq=[-3j, -1j, 1j, 3j]
xx=[]
for xii in xi:
	for xqq in xq:
		x=xii + xqq
		xx.append(x)
############################################
minn=1000000000
com=[]

ind =0
GS=[]
IND=[]

xaxis=[]
yaxis=[]
zaxis=[]

for x1 in xx:
	for x2 in xx:
		for x3 in xx:
			s = [x1, x2, x3]
			s2 =np.matmul(H, np.array(s).reshape(-1,1))

			gam= (abs(Y[0] -s2[0]))**2 + (abs(Y[1] -s2[1]))**2 + (abs(Y[2] -s2[2]))**2
			####################################
			if gam<minn:
				minn =gam
				com = s
			######################################
			GS.append(gam)
			xaxis.append(indmap[x1])
			yaxis.append(indmap[x2])
			zaxis.append(indmap[x3])

			IND.append(ind)
			ind+=1
###############################################3
print("(3a)")
print("G(X(ML)):")
print(minn)
print("X(ML):")
print(com)

############################################################
plt.plot(IND, GS, marker='o')

plt.xlabel("indexes of possible x vectors")
plt.ylabel("Gamma (x)")
plt.title("Gamma(x) v.s indexes of possible x vectors")

plt.show()
##########################################################
# Create a 3D plot
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# Scatter plot with color mapping
#sc = ax.scatter(xaxis, yaxis, zaxis, c=GS, cmap='viridis', s=50)

# Add a color bar to show the value scale
#plt.colorbar(sc, label='Value')

# Labels
#ax.set_xlabel('x1 index')
#ax.set_ylabel('x2 index')
#ax.set_zlabel('x3 index')
#plt.title('Gamma(x) v.s indexes of possible x vectors')

# Display the plot
#plt.show()
######################################################################




###############################################################
#(3b)

Q, R = np.linalg.qr(H)

print(R)

zz=np.matmul(np.conjugate(Q.T), Y)
print("(3b) z:")
print(zz)
##################################################
#(3c)
print("(3c)")
rounds=R.shape[0]
bestk=8

for i in range(rounds):
	myz = zz[(rounds -1 -i)]
	rr = (R[(rounds -1 -i), (rounds -1 -i):(rounds)]).reshape(1,-1)

	if i ==0:
		candy=[]
		cost=[]
		for xs in xx:
			myval=np.matmul(rr,np.array([xs]).reshape(-1,1))
			mycost=(abs((myz-myval)))**2
			cost.append(mycost[0][0])
			##################
			temp=[]
			temp.append(xs)
			candy.append(temp)
	else:
		sorted_pairs = sorted(zip(cost, candy))
		sorted_cost, sorted_candy = zip(*sorted_pairs)

		sorted_cost = list(sorted_cost)
		sorted_candy = list(sorted_candy)
		#############################################3
		bestcost=sorted_cost[:bestk]
		bestcandy=sorted_candy[:bestk]
		#
		candy=[]
		cost=[]

		for k in range(bestk):
			for q in range(len(xx)):
				tempcan = (bestcandy[k]).copy()
				tempcost = (bestcost[k]).copy()
				################################3
				tempcan.append(xx[q])
				candy.append(tempcan)

				rev = tempcan[::-1]
				##########################################################
				myval2=np.matmul(rr,np.array(rev).reshape(-1,1))
				mycost2=(abs((myz-myval2)))**2
				
				tempcost += mycost2[0][0]
				cost.append(tempcost)

##########################################################################3

sorted_pairs = sorted(zip(cost, candy))
sorted_cost, sorted_candy = zip(*sorted_pairs)

sorted_cost = list(sorted_cost)
sorted_candy = list(sorted_candy)

print("x8B ^ [x(1), x(2), x(3)]: ")
lastrev = (sorted_candy[0])[::-1]
print(lastrev)

print("minimum ED PHI(x8B ^): ")
print(sorted_cost[0])


symbols=[]
for t in range(len(sorted_candy)):
	#symbol=''
	#seee=sorted_candy[t]
	#symbol += indmap[seee[0]]
	#symbol += indmap[seee[1]]
	#symbol += indmap[seee[2]]

	#symbols.append(symbol)
	symbols.append(t)

plt.plot(symbols, sorted_cost, marker='o', color='green', linestyle='--', label='Values')

plt.xlabel("x8B vectors index")
plt.ylabel("T(1) + T(2) + T(3)")
plt.title("T(1) + T(2) + T(3) v.s x8B vectors index")

plt.legend()
plt.show()

#########################################################
