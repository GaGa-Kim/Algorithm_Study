# 1912번
# n개의 정수로 이루어진 임의의 수열이 주어질 때, 
# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 구하기
# (수는 한 개 이상 선택한다.)


# 1 ≤ n ≤ 100,000
n = int(input())

# -1,000 <= 각 수 <= 1,000
num = list(map(int, input().split()))

for i in range(1, n):
    num[i] = max(num[i], num[i-1] + num[i])

print(max(num))