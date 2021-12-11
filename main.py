import time
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running {} is {} seconds.".format(function.__name__, str(t1 - t0)))
        return result
    return function_timer


@fn_timer
def func():
    # TASK 1
    # --------------------
    # q = '1 3 5 10 11,2 4 5 10 11'
    # q = q.split(',')
    # q = [x.split(' ') for x in q]
    # cnt = 0
    # for x in q[0]:
    #     if x in q[1]:
    #         cnt += 1
    #
    # if cnt in (0, 1, 2):
    #     print(0)
    # elif cnt == 3:
    #     print(100)
    # elif cnt == 4:
    #     print(1000)
    # elif cnt == 5:
    #     print(10000)

    # TASK 2
    # --------------------
    # q = 'A123456789'
    # city = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20,
    #         'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
    #         'Y': 31, 'Z': 33}
    # city_num = int(str(city.get(q[0]))[0]) + int(str(city.get(q[0]))[1])*9
    # cnt = (sum([int(i)*int(n) for i, n in enumerate(q[-2:0:-1], 1)]) + int(q[-1]) + city_num) % 10
    #
    # if cnt == 0:
    #     print('合法')
    # else:
    #     print('不合法')

    # TASK 3
    # --------------------
    # # q = '3337777899922222222222222222'
    # q = '1112223334444555566667777'
    # cnt = 1
    # cnt_list = []
    #
    # for i in range(1, len(q)):
    #     if int(q[i-1]) <= int(q[i]):
    #         cnt += 1
    #     else:
    #         cnt_list.append(cnt)
    #         cnt = 1
    #
    #     # if i == len(q)-1:
    #     #     cnt_list.append(cnt)
    #
    # if not cnt_list:
    #     print(cnt)
    # else:
    #     print(max(cnt_list))
    #
    # # print(cnt_list)

    # TASK 5
    # --------------------
    q = '''2
2,3,3,4
1 2 9999
0 -4 1
3 1 0 2
-1 2 5 0
0 -2 2 1
1 -1 16 5
4 -10 -18 1
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

    for x in q_list:
        if ',' in x:
            matrix_index.append(q_list.index(x))

    for x in matrix_index:
        for y in q_list[x].split(','):
            temp.append(int(y))
        matrix_size.append(temp)
        temp = []

    # print(matrix_size)

    for n in range(0, len(matrix_index)):
        a = matrix_size[n][0]
        b = matrix_size[n][2]

        matrix_a.append(q_list[matrix_index[n]+1:matrix_index[n]+1+a])
        matrix_b.append(q_list[matrix_index[n]+1+a:matrix_index[n]+1+a+b])

        # print(matrix_size[n], a, b)
    # print(matrix_a)
    # print(matrix_b)

    for i, a in enumerate(matrix_a):
        # print(i, a)
        for x in range(len(a)):
            matrix_a[i][x] = matrix_a[i][x].split(' ')
            # print(x, a[x])
        # print('-'*20)

    for x in matrix_a:
        for y in range(len(x)):
            print(y)
    # print(matrix_a)


func()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
