import sys
input = sys.stdin.readline

n = int(input())

answer = 0
while n >= 0:
    # 5의 배수일 경우 5킬로그램 봉지
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break
    # 5의 배수가 될 때까지는 3킬로그램 봉지
    n -= 3
    answer += 1
else:
    print(-1)
