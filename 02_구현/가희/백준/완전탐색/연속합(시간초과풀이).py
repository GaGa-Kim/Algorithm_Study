# 1912번 (완전탐색으로는 시간 초과)
# n개의 정수로 이루어진 임의의 수열이 주어질 때, 
# 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 구하는 프로그램
# (단, 수는 한 개 이상 선택해야 함)

# 1 <= n <= 100,000
n = int(input())
# -1,000 <= 각 수 <= 1,000
num = list(map(int, input().split()))

maxSum = num[0]
for i in range(n):
    tmp = num[i]
    for j in range(i+1, n):  
        tmp += num[j]
        maxSum = max(maxSum, tmp)

print(maxSum)