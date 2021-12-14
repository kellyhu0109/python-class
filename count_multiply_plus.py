import sys
q = sys.stdin.read()

# q = '4421'
q_list = [int(x) for x in q]
multiply = 1
plus = 0

for x in q_list:
    multiply *= x

for x in q_list:
    plus += x

print(multiply - plus)
