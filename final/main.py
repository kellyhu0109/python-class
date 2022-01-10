import sys
q = sys.stdin.read()

# q = '''4
# 1024 235 450 245'''

q = q.splitlines()
q = q[1].split(' ')
q = [int(x) for x in q]
# print(q)

p = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

div = []
prime = []
cnt = 0

# for x in q:
#     for n in range(2, x):
#         if x % n == 0:
#             for m in range(2, n):
#                 if n % m == 0:
#                     # print(m)
#                     break
#                 else:
#                     if n % 5 == 0:
#                         break
#                     elif n % 3 == 0:
#                         break
#                     else:
#                         # print('*', m)
#                         div.append(n)
#                         break
#
#     # print(div)
#
#     if div:
#         print(False)
#     else:
#         print(True)
#
#     # print(div)
#     div = []
# --------------------------------------------
# for x in q:
#     f = True
#     for n in range(2, x):
#         if x % n == 0:
#             div.append(n)
#
#     for y in div:
#         if y in p:
#             f = False
#
#     print(f)
#
#     # if div:
#     #     print(False)
#     # else:
#     #     print(True)
#
#     # print(div)
#     div = []
# --------------------------------------------
for x in q:
    f = True
    for n in p:
        if x % n == 0:
            # div.append(n)
            f = False

    # for y in div:
    #     if y in p:
    #         f = False

    print(f)

    # if div:
    #     print(False)
    # else:
    #     print(True)

    # print(div)
    div = []

# p = []
#
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
#             return False
#     return True     # 都沒有人能整除，所以 n 是質數。
#
# n = int(input('Input a number: '))  # 得到輸入值 n。
#
# for i in range(2, n + 1):   # 產生 2 到 n 的數字。
#     i_is_prime = is_prime(i)    # 判斷 i 是否為質數。
#     if i_is_prime:              # 如果是，印出來。
#         p.append(i)
#
# print(p)
