basic = 0.033
rate = 0.01
max = 1
temp = basic * rate
print(temp)

while(basic<max):
    basic += 0.033
    temp = (temp + basic) * rate
    print(temp)
