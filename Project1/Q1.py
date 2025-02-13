import random

random.seed(13)

data=[]

for i in range(16):
	d = random.random()

	if d > .5:
		data.append(1)
	else:
		data.append(0)

#[0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
print(data)