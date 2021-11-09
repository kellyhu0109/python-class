# import sys
# q = sys.stdin.read()

q = '''1112223334444555566667777
3337777899922222222222222222'''

q_list = q.splitlines()
output = []

for n in range(len(q_list)):
    cnt = 1
    cnt_list = []
    for i in range(1, len(q_list[n])):
        if int(q_list[n][i-1]) <= int(q_list[n][i]):
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1

        if i == len(q_list[n])-1:
            cnt_list.append(cnt)

    output.append(max(cnt_list))

for x in output:
    print(x)
