n, m = map(int, input().split())
j = int(input())

distance = 0
start = 1 # 바구니 시작 위치
end = m # 바구니 끝 위치

for _ in range(j):
    i = int(input())
    if i < start: # 바구니 왼쪽에 사과
        distance += (start - i)
        start = i
        end = i + m - 1
    elif i > end: # 바구니 오른쪽에 사과
        distance += (i - end)
        start = i - m + 1
        end = i
print(distance)