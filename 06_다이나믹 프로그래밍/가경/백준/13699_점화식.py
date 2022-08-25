n = int(input())

d = [0] * 36
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    t = 0
    # 짝수일 때 
    if i % 2:
        for j in range(i // 2):
            t += 2 * d[j] * d[i - j - 1]
        d[i] = t + d[i // 2] ** 2
    # 홀수일 때
    else:
        for j in range(i // 2):
            t += 2 * d[j] * d[i - j - 1]
        d[i] = t
print(d[n])