import numpy as np

RMS= 25.60915740232992
Bc= 1/(5* RMS) *pow(10,9)

print("coherence bandwidth: {}".format(Bc))

num = 100000000/Bc
print("subcarriers number: {}".format(num))

