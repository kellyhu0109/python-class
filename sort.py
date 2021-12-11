import sys
q = sys.stdin.read()

# q = '''9
# 5 3 1 3 4
# 10 4 9 8 4 2
# 20 4 10 5 7 4
# 8 10 23 1 2 3 4 5 7
# 8 43 10 44 43 12 9 8 2
# 43 5 5 8 46 37 20
# 59 8 12 19 33 20 10 17 11 13
# 88 7 22 14 13 2 56 60 20
# 29 8 21 25 19 1 5 23 20 27'''

q_list = q.splitlines()
num = q_list[0]
num_list = [x.split(' ') for x in q_list[1:]]
max_list = []

for x in range(0, len(num_list)):
    # print(num_list[x])
    for y in range(0, len(num_list[x])):
        num_list[x][y] = int(num_list[x][y])
# print(num_list)

for i in range(0, len(num_list)):
    num_list[i].sort(reverse=True)
    print(num_list[i][0], num_list[i][1])
