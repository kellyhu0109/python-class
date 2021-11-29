# import sys
# q = sys.stdin.read()

q = '''1
3'''

q_list = q.splitlines()
num = q[0]

temp_list = []
square = 0
sqr_list = []

for i in range(1, len(q_list)):
    # square = int(q_list[i]) ** 2
    temp_list = [x for x in q_list[i]]

    # print(temp_list)

    if len(temp_list) == 1:
        # print("here")
        square = int(temp_list[0]) ** 2
        temp_list = [x for x in str(square)]

    while(len(temp_list) != 1):
        temp_list = [int(x) ** 2 for x in temp_list]
        sqr_list = sum(temp_list)
        temp_list = [x for x in str(sqr_list)]
    #
    # if temp_list[0] == 1:
    #     print('T')
    # else:
    #     print('F')

    #     print(sqr_list, temp_list)
    # print('-'*20)

    if temp_list[0] == '1':
        print('T')
    else:
        print('F')
