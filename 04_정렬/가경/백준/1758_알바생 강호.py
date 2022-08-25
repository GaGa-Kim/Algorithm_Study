import sys
input = sys.stdin.readline

n = int(input())
guest = []
for _ in range(n):
    guest.append(int(input().rstrip()))
# 강호에게 원래 주려고 생각했던 돈이 많은 손님부터 먼저 커피를 줌
guest = sorted(guest, reverse=True)

answer = 0
for i in range(n):
    money = guest[i] - ((i + 1) - 1)
    # 팁 값이 음수라면 팁을 받지 않음
    if (money < 0):
        continue
    answer += money
print(answer)