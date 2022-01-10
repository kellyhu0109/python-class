def matrix_find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return [i, j]


q = '''2
4,3,3,5
2 4 1
3 6 2
2 5 0
1 2 3
2 6 2 0 2
3 1 1 1 2
9999 2 2 0 1
20 18 10 4 13
32 28 16 6 20
19 17 9 5 14
20 14 10 2 9
4,3,3,5
2 4 1
3 6 2
2 5 0
1 2 3
2 6 2 0 2
3 1 1 1 2
9999 2 2 0 1
20 18 10 4 13
32 28 16 6 20
19 17 9 5 14
20 14 10 2 9'''

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

print(matrix_a)
# print(matrix_find(9999, matrix_a[0]))
print(matrix_b)
print(matrix_c)
