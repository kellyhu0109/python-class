import sys
q = sys.stdin.read()

# q = '123456789ABc'
cnt_en = 0
cnt_num = 0

en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(q) < 10:
    print(False)
else:
    for x in range(len(q)):
        # print(x)
        if q[x] in en:
            cnt_en += 1
        if q[x] in num:
            cnt_num += 1

    if cnt_en == 0:
        print(False)
    else:
        if cnt_num == 0:
            print(False)
        else:
            print(True)
