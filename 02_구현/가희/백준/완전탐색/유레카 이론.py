# 10448번
# 자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 판단하는 프로그램
# (단, 3개의 삼각수가 모두 달라야 할 필요는 없음)
# 삼각수 Tn = n(n+1)/2

# 1. 미리 1,000 이하의 모든 유레카 수를 구한다.
# 2. k가 미리 구한 수 중 하나인지 확인한다.

triangleNum = [n*(n+1)//2 for n in range(1, 46)]
answer = [0] * 1001

for i in triangleNum:
    for j in triangleNum:
        for k in triangleNum:
            if i + j + k <= 1000:
                # 3개의 삼각수로 표현 가능하면 1
                answer[i+j+k] = 1

t = int(input())
for _ in range(t):
    # 3 <= k <= 1,000
    k = int(input())
    print(answer[k])
    
