import sys
input = sys.stdin.readline

n = int(input())

count = 0
while n > 0:
    # 5의 배수이면 모두 5원으로 거슬러줌
    if n % 5 == 0:
        count += n // 5
        break
    # 5원으로 안 될때 2원 사용
    n -= 2
    count += 1

if n < 0:
    print(-1)
else:
    print(count)