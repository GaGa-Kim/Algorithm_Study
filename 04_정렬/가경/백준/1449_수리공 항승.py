import sys
input = sys.stdin.readline

n, l = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()

# 테이프 시작점과 끝점
start = hole[0]
end = hole[0] + l 
count = 1
for i in range(n):
    # 현재 테이프 시작점과 끝점 사이에 물구멍이 있다면
    if start <= hole[i] < end:
        continue
    # 현재 테이프 시작점과 끝점 사이에 물구멍이 없다면
    else:
        # 테이프 시작점과 끝점 변경
        start = hole[i]
        end = hole[i] + l
        count += 1
print(count)
