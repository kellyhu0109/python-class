import math
import sys
q = sys.stdin.read()

# q = '''3
# 20,8,30
# 10,20,30
# 8,12'''

q_list = q.splitlines()
num = int(q_list[0])

for x in range(1, num+1):
    q_list_split = [int(x) for x in q_list[x].split(',')]

    temp = math.gcd(q_list_split[0], q_list_split[1])
    for y in range(2, len(q_list_split)):
        temp = math.gcd(temp, q_list_split[y])
    print(temp)
    # print(q_list_split[1])

# print(math.gcd(math.gcd(20, 8), 30))
