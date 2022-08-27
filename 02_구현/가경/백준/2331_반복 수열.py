a, p = map(int, input().split())
d = [a]
while True:
    i = 0
    for j in str(d[-1]):
        i += int(j) ** p
    # 여기부터는 반복되는 수이므로 break
    if i in d:
        break
    d.append(i)
print(d.index(i))