import numpy as np
import math

pdb=[0,-3,-4,-8,-15]
D=[0,10,40,80,100]
#######################################
Gammas=[]
for i in range(len(pdb)):
	mean = 0
	variance = 0.5
	std_dev = np.sqrt(variance)
	X = np.random.normal(mean, std_dev)
	Y = np.random.normal(mean, std_dev)

	Z = X+ Y*1J

	Gammas.append(Z)

#print(Gammas)
###############################################
#path gain: beta =alpha{i}
#P(tou,t) = summ_r[ beta_r(t)^2   * delta(tou -tou_r)]
#because tou is time inveriant
#for a single known tou value, only when tou_r =tou, RHS has value
#for a given tou, P(tou) = beta_r ^2
#############################################################

################################

pval=[]
betas=[]
for i in range(len(pdb)):
	s=(pdb[i]/10)
	ss=pow(10,s)
	pval.append(ss)
	betas.append(math.sqrt(ss))
###############################
#print(pval)
#print(betas)
##########################################################
Gis=[]
SU=0
for i in range(len(pdb)):
	gi= betas[i]*Gammas[i]
	#print(gi)
	Gis.append(gi)
	SU += pow(abs(gi),2)
#######################################################

K = math.sqrt( 1/(SU) )


Hs=[]
for i in range(len(pdb)):
	Hs.append(K* Gis[i])
######################################################

print("h0: {}".format(Hs[0]))
print("h1: {}".format(Hs[1]))
print("h2: {}".format(Hs[2]))
print("h3: {}".format(Hs[3]))
print("h4: {}".format(Hs[4]))
