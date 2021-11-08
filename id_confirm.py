import sys
q = sys.stdin.read()
# q = 'A123456781'
city = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20,
        'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
        'Y': 31, 'Z': 33}
city_num = int(str(city.get(q[0]))[0]) + int(str(city.get(q[0]))[1])*9
cnt = (sum([int(i)*int(n) for i, n in enumerate(q[-2:0:-1], 1)]) + int(q[-1]) + city_num) % 10

if cnt == 0:
    print('合法')
else:
    print('不合法')
