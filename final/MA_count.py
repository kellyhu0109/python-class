import math
import sys
q = sys.stdin.read()

# q = '11 12 13 14 14 13 12 11'

q = q.split(' ')
q = [int(x) for x in q]
# print(q)

ma2 = []
ma3 = []
ma5 = []

# MA2
for x in range(len(q)):
    try:
        # print(q[x], q[x+1])
        avg = math.ceil((q[x] + q[x+1]) / 2)
        ma2.append(avg)
    except IndexError:
        pass

# print(ma2)
# print('-'*20)

# MA3
for x in range(len(q)):
    try:
        # print(q[x], q[x+1], q[x+2])
        avg = math.ceil((q[x] + q[x+1] + q[x+2]) / 3)
        ma3.append(avg)
    except IndexError:
        pass

# print(ma3)
# print('-'*20)

# MA5
for x in range(len(q)):
    try:
        # print(q[x], q[x+1], q[x+2], q[x+3], q[x+4])
        avg = math.ceil((q[x] + q[x+1] + q[x+2] + q[x+3] + q[x+4]) / 5)
        ma5.append(avg)
    except IndexError:
        pass

# print(ma5)

ma2 = [str(x) for x in ma2]
ma3 = [str(x) for x in ma3]
ma5 = [str(x) for x in ma5]

ma2 = ' '.join(ma2)
ma3 = ' '.join(ma3)
ma5 = ' '.join(ma5)

print(ma2)
print(ma3)
print(ma5)
