birth = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    day, month, year = map(int, (day, month, year))
    birth.append((year, month, day, name))
birth.sort()
print(birth[-1][3])
print(birth[0][3])