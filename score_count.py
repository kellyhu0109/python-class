import sys
q = sys.stdin.read()

q_list = q.splitlines()
lines = int(q_list[0])
q_list = q_list[1:]
count = 0
plus = 1

for i in range(lines):
    count_list = q_list[i].split('X')
    # print(count_list)
    for x in range(0, len(count_list)):
        # print(count_list[x])
        for o in range(0, len(count_list[x])):
            count += plus
            if plus != 0:
                plus += 1
        plus = 1
    print(count)
    count = 0
