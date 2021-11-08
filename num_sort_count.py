# q = '3337777899922222222222222222'
q = '1112223334444555566667777'
cnt = 1
cnt_list = []

for i in range(1, len(q)):
    if int(q[i-1]) <= int(q[i]):
        cnt += 1
    else:
        cnt_list.append(cnt)
        cnt = 1

    if i == len(q)-1:
        cnt_list.append(cnt)

print(max(cnt_list))
