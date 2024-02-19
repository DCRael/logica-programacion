a, b = 0, 1
for i in range(50):
    print(a)
    temp = a
    a = b
    b = temp + b
    