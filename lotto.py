import sys
q = sys.stdin.read()
# q = '1 3 5 10 11,2 4 5 10 11'
q = q.split(',')
q = [x.split(' ') for x in q]
cnt = 0
for x in q[0]:
    if x in q[1]:
        cnt += 1

if cnt in (0, 1, 2):
    print(0)
elif cnt == 3:
    print(100)
elif cnt == 4:
    print(1000)
elif cnt == 5:
    print(10000)
