number = input()
count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in number:
    if i == '9':
        count[6] += 1
    else:
        count[int(i)] += 1

if count[6] % 2 == 0:
    count[6] = count[6] // 2
else:
    count[6] = count[6] // 2 + 1

print(max(count))