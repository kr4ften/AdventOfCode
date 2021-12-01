import numpy as np

nIncreases = 0
data = np.loadtxt('input.txt')

print(data[0:3])

for i in range(0, data.shape[0]):
    try:
        test = data[i + 1: i + 4]
    except:
        break
    if np.sum(data[i:i+3]) < np.sum(data[i + 1: i + 4]):
        nIncreases += 1

print(nIncreases)