n = int(input())

d = [0] * 117
d[1] = 1
d[2] = 1
d[3] = 1

def fibo(x):
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 3)
    return d[x]
print(fibo(n))

