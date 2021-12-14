import sys
q = sys.stdin.read()


def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for z in range(len(matrix[i][j])):
                if matrix[i][j][z] == element:
                    return (i, j, z)


# q = '''2
# 2,3,3,4
# 1 2 9999
# 0 -4 1
# 3 1 0 2
# -1 2 5 0
# 0 -2 2 1
# 1 -1 16 5
# 4 -10 -18 1
# 4,3,3,5
# 2 4 1
# 3 6 2
# 2 5 0
# 1 2 3
# 2 6 2 0 2
# 9999 1 1 1 2
# 4 2 2 0 1
# 20 18 10 4 13
# 32 28 16 6 20
# 19 17 9 5 14
# 20 14 10 2 9'''

# q = '''2
# 2,3,3,2
# 1 1 9999
# 1 1 1
# 1 1
# 1 1
# 1 1
# 3 3
# 3 3
# 2,2,2,2
# 1 1
# 1 0
# -1 -1
# -1 9999
# -2 -2
# -1 -1'''

q_list = q.splitlines()
num = int(q_list[0])
matrix_index = []
matrix_size = []
temp = []
matrix_a = []
matrix_b = []
matrix_c = []
ans_matrix = []
ans_matrixes = []
count = 0
false_value = []
temp_x = 0

for x in q_list:
    if ',' in x:
        matrix_index.append(q_list.index(x))

for x in matrix_index:
    for y in q_list[x].split(','):
        temp.append(int(y))
    matrix_size.append(temp)
    temp = []

# print(matrix_size)

# get matrix_a and matrix_b
for n in range(0, len(matrix_index)):
    a = matrix_size[n][0]
    b = matrix_size[n][2]

    matrix_a.append(q_list[matrix_index[n]+1:matrix_index[n]+1+a])
    matrix_b.append(q_list[matrix_index[n]+1+a:matrix_index[n]+1+a+b])
    matrix_c.append(q_list[matrix_index[n]+1+a+b:matrix_index[n]+1+a+b+matrix_size[n][0]])

    # print(matrix_size[n], a, b)
# print(matrix_a)
# print(matrix_b)
# print(matrix_c)

# split matrix with space
for i, a in enumerate(matrix_a):
    # print(i, a)
    for x in range(len(a)):
        matrix_a[i][x] = matrix_a[i][x].split(' ')
        # print(x, a[x])
    # print('-'*20)

for i, a in enumerate(matrix_b):
    # print(i, a)
    for x in range(len(a)):
        matrix_b[i][x] = matrix_b[i][x].split(' ')
        # print(x, a[x])
    # print('-'*20)

for i, a in enumerate(matrix_c):
    # print(i, a)
    for x in range(len(a)):
        matrix_c[i][x] = matrix_c[i][x].split(' ')
        # print(x, a[x])
    # print('-'*20)

# matrix str to int
for x, m in enumerate(matrix_a):
    for y in range(len(m)):
        # print(x, y)
        matrix_a[x][y] = list(map(int, matrix_a[x][y]))

for x, m in enumerate(matrix_b):
    for y in range(len(m)):
        # print(x, y)
        matrix_b[x][y] = list(map(int, matrix_b[x][y]))

for x, m in enumerate(matrix_c):
    for y in range(len(m)):
        # print(x, y)
        matrix_c[x][y] = list(map(int, matrix_c[x][y]))

# print(matrix_a)
# print(matrix_b)
# print(matrix_c)

false_value.append(find(9999, matrix_a))
false_value.append(find(9999, matrix_b))
# print(false_value)

for fv in false_value:
    a = fv[0]
    b = fv[1]
    c = fv[2]

    if a == 0:
        # print(matrix_a[a][b][c])  # 錯誤值
        # print(matrix_b[a][c][1])  # 與錯誤值相乘之值
        # print(matrix_c[a][a][1])  # 計算出之正確值

        for x in range(len(matrix_a[a][0])):
            if matrix_a[a][b][x] != 9999:
                # print(matrix_c[a][b][1], matrix_a[a][b][x], (matrix_b[a][x][1]))
                matrix_c[a][b][1] -= matrix_a[a][b][x] * int(matrix_b[a][x][1])

            if matrix_a[a][b][x] == 9999:
                temp_x = x

        # print(matrix_c[a][a][1], matrix_b[a][temp_x][1])
        print(int(matrix_c[a][b][1]/matrix_b[a][temp_x][1]))
        # print(matrix_c[a][a][1])

    # print('-'*20)

    if a == 1:
        # print(matrix_a[a][0][b])  # 與錯誤值相乘之值
        # print(matrix_b[a][b][c])  # 錯誤值
        # print(matrix_c[a][0][0])  # 計算出之正確值

        for x in range(len(matrix_a[a][0])):
            if matrix_b[a][x][c] != 9999:
                # print(matrix_c[a][b][1], matrix_b[a][a][x], (matrix_b[a][x][1]))
                # print(matrix_c[a][0][c], matrix_a[a][0][x], matrix_b[a][x][c])
                matrix_c[a][0][c] -= matrix_a[a][0][x] * int(matrix_b[a][x][c])

            if matrix_b[a][x][c] == 9999:
                temp_x = x

        # print(matrix_c[a][0][c], matrix_a[a][0][temp_x])
        print(int(matrix_c[a][0][c]/matrix_a[a][0][temp_x]))
        # print(matrix_c[a][a][1])

# calculate matrix
# --------------------
'''
for n in range(len(matrix_index)):
    for x in range(len(matrix_a[n])):
        # for y in range(len(matrix_a[0][0])):
        #     # print(matrix_a[0][x][y])
        #     t = y
        for z in range(len(matrix_b[n][0])):
            # print(z)
            for r in range(len(matrix_b[n])):
                # print(x, r, matrix_a[0][x][r], '|', r, z, matrix_b[0][r][z])
                # print(matrix_a[n][x][r], matrix_b[n][r][z])
                count += matrix_a[n][x][r] * int(matrix_b[n][r][z])
            ans_matrix.append(count)
            count = 0
            #     t += 1
            # t = y
        # print('-'*9)
    ans_matrixes.append(ans_matrix)
    ans_matrix = []
'''
# --------------------

# for x in range(len(matrix_a[0])):
#     for y in range(len(matrix_a[0][0])):
#         print(x, y)

# print(len(matrix_b[1][0]))
