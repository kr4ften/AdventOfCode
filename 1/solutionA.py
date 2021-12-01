import numpy as np

nIncreases = 0

data = np.loadtxt('input.txt')

#print(data[0])

for i in range(1, data.shape[0]):
    #print(data[i])
    if data[i-1] < data[i]:
        nIncreases += 1

print(nIncreases)