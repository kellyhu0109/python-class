import sys
q = sys.stdin.read()

# q = '1000002'
q = int(q)

if q % 2 == 0:
    print(q + 2)
else:
    print(q + 1)
