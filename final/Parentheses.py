import sys
q = sys.stdin.read()

# q = '(1+(2*3)+((8)/4))+1'
q = [x for x in q]
# print(q)

find = ['(', ')']
st = []
temp = 0
cnt = 0

for x in range(len(q)):
    # print(q[x])
    if q[x] in find:
        st.append(q[x])

# print(st)

try:
    while (st[-1] == ')'):
        st.pop(-1)
except IndexError:
    pass

# print(st)

for x in range(len(st)):
    if st[x] == '(':
        cnt += 1
    else:
        cnt -= 1

print(cnt)
