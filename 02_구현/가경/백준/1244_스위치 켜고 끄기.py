import sys
input = sys.stdin.readline

# 스위치 상태 변경
def change(num):
    if switches[num] == 0:
        switches[num] = 1
    else:
        switches[num] = 0
    return

n = int(input())
# 0번 스위치 + 주어진 각 스위치의 상태
switches = [-1] + list(map(int, input().split()))

m = int(input())
for _ in range(m):
    gender, num = map(int, input().split())
    # 남자
    if gender == 1:
        # n + 1 범위 안에서 num의 배수 스위치의 상태 바꾸기
        for i in range(num, n + 1, num):
            change(i)
    # 여자
    else:
        change(num)
        for i in range(n // 2):
            if num + i > n or num - i < 1:
                break
            # 좌우 대칭인 스위치의 상태 바꾸기 
            if switches[num + i] == switches[num - i]:
                change(num + i)
                change(num - i)
            else:
                break

for i in range(1, n + 1):
    print(switches[i], end=' ')
    if i % 20 == 0: # 한 줄에 20개씩 출력
        print()
