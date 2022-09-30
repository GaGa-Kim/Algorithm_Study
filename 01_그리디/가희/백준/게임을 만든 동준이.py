# 2847번
# n개의 레벨을 각각 클리어할 때 얻는 점수가 주어졌을 때, 
# 이 점수들이 오름차순이 되려면 몇 번 감소시키면 되는지 구하는 프로그램
# (정답이 여러 개인 경우 점수를 내리는 것을 최소한으로 하는 방법으로)

# 1 <= n <= 100
n = int(input())
# 각 레벨을 클리어하면 얻는 점수 (<= 20,000)
score = [int(input()) for _ in range(n)]

result = 0
for i in range(n-2, -1, -1):
    while score[i] >= score[i+1]:
        score[i] -= 1
        result += 1
        
print(result)

#--------------------------------------------------
# while 없애니 훨 빠름
# 1 <= n <= 100
n = int(input())
# 각 레벨을 클리어하면 얻는 점수 (<= 20,000)
score = [int(input()) for _ in range(n)]

result = 0
for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        result += (score[i] - score[i+1] + 1)
        score[i] -= (score[i] - score[i+1] + 1)
        
print(result)





