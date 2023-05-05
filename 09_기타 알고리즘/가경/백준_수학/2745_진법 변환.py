n, b = input().rstrip().split()
n = n[::-1]
b = int(b)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = 0
for i in range(len(n)):
    answer += number.index(n[i]) * (int(b) ** i)
print(answer)