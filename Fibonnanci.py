a = 0
b = 1
next = a + b
n = int(input("Enter a number greater that 2: "))

while (n > 2):
    print(next, end = " ")
    a, b = b, next
    next = a + b
    n-=1