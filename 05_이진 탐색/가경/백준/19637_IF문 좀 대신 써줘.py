import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nameList = []
powerList = []
for _ in range(n):
    name, power = input().split()
    power = int(power)
    if powerList and powerList[-1] == power:
        continue
    nameList.append(name)
    powerList.append(power)

for _ in range(m):
    power = int(input())
    start = 0
    end = len(powerList) - 1
    while (start <= end):
        mid = (start + end) // 2
        if power > powerList[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(nameList[end + 1])