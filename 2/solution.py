import numpy as np

data = np.genfromtxt('input.txt', dtype='str')

x = 0
y = 0

for row in data[:]:
    if row[0] == 'up':
        y -= int(row[1])
    elif row[0] == 'down':
        y += int(row[1])
    elif row[0] == 'forward':
        x += int(row[1])


print('Answer A: Product x * y = ' + str(x * y))

aim = 0
x, y = 0, 0

for row in data[:]:
    if row[0] == 'up':
        aim -= int(row[1])
    elif row[0] == 'down':
        aim += int(row[1])
    elif row[0] == 'forward':
        x += int(row[1])
        y += aim * int(row[1])

print('Answer B: Product x * y = ' + str(x * y))
