import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
array = set()
for _ in range(n):
    array.add(tuple(map(int, input().split())))
    
count = 0
# i를 기준으로 가로 길이와 세로 길이에 맞는 평행한 직사각형을 만들 수 있는 점이 있는지 확인
for i in array:
    if (i[0] + a, i[1]) in array and (i[0], i[1] + b) in array and (i[0] + a, i[1] + b) in array:
        count += 1
print(count)

