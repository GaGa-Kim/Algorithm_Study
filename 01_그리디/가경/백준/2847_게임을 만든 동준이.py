import sys
input = sys.stdin.readline

n = int(input())
score = []
for i in range(n):
    score.append(int(input().rstrip()))

count = 0
# 맨 마지막부터 앞으로 (n - 2 부터 -1 숫자만큼의 간격으로 0 까지의 점수 범위를 반환)
for i in range(n - 2, -1, -1):
    if score[i] >= score[i + 1]:
        count += score[i] - score[i + 1] + 1
        score[i] = score[i + 1] - 1
print(count) 
