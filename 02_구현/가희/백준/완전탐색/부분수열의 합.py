# 1182번
# n개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램

# 부분수열) 전체 수열에서 몇 개의 수를 제거해서 만든 수열
#           => 반드시 연속된 수를 뽑는 것이 아님

# 배열에서 뽑을 수 있는 모든 조합 구하기 위해 사용
from itertools import combinations

# 1 <= n <= 20, |S| <= 1,000,000
n, s = map(int, input().split())
# |정수| <= 100,000
integer = list(map(int, input().split()))

result = 0
# 정수 리스트 돌면서
for i in range(1, n+1):
    comb = list(combinations(integer, i))
    for j in comb:
        if sum(j) == s:
            result += 1

print(result)    
            
        
