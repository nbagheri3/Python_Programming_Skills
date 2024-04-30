a = [10, 20, 30, 40]
b = [0] * 10

a_size = len(a)
b_size = len(b)
index = 0
for i in range(b_size):
    if index >= a_size:
       index = 0
    b[i] = a[index]
    index += 1

print(b)