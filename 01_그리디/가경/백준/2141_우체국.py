import sys
input = sys.stdin.readline

n = int(input())

village = []
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    village.append([x, a])
    people += a

village.sort(key= lambda x: x[0])

count = 0
for i in range(n):
    count += village[i][1]
    # 누적된 인구 수가 전체 인구수의 절반이 넘어가는 마을에 우체국 설치
    if count >= people/2:
        print(village[i][0])
        break
