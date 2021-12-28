# import sys
# q = sys.stdin.read()
#
# # q = '''4
# # 1024 235 450 245'''
#
# q = q.splitlines()
# q = q[1].split(' ')
# q = [int(x) for x in q]
# # print(q)
#
# div = []
# prime = []
# cnt = 0
#
# for x in q:
#     for n in range(2, x):
#         if x % n == 0:
#             div.append(n)
#     # print(div)
#     # for y in div:
#     #     for m in range(2, y):
#     #         if y % m == 0:
#     #             break
#     #         else:
#     #             prime.append(m)
#     #     print(prime)
#     # prime = []
#
#     for y in div:
#         for m in range(2, y):
#             if y % m == 0:
#                 # print('*', y)
#                 break
#             elif y % 3 == 0:
#                 break
#             elif y % 5 == 0:
#                 break
#             else:
#                 # print(y, m)
#                 # print(y)
#                 prime.append(y)
#
#     if set(prime):
#         # print(set(prime))
#         print(False)
#     else:
#         print(True)
#
#     prime = []
#     div = []
#     # print('-'*20)
#
# # if set():
# #     print('hi')
# # else:
# #     print('uu')

# 2================================================

# import sys
# q = sys.stdin.read()

q = '''4
1024 235 450 245'''

q = q.splitlines()
q = q[1].split(' ')
q = [int(x) for x in q]
# print(q)

div = []
prime = []
cnt = 0

for x in q:
    for n in range(2, x):
        if x % n == 0:
            for m in range(2, n):
                if n % m == 0:
                    # print(m)
                    break
                else:
                    if n % 5 == 0:
                        break
                    elif n % 3 == 0:
                        break
                    else:
                        # print('*', m)
                        div.append(n)
                        break

    # print(div)

    if div:
        print(False)
    else:
        print(True)

    # print(div)
    div = []
