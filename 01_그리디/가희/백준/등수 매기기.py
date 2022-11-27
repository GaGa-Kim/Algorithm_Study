# 2012번
# n명의 사람들의 불만도 총합을 최소로 하는 프로그램

# 모든 학생들은 자신이 n명 중 몇 등을 할 것인지 예상 등수 적어서 제출
# 자신의 등수를 A등으로 예상했는데 실제 등수가 B등일 경우,
# 이 사람의 불만도는 |A-B|

import sys
input = sys.stdin.readline

# n (1 <= n <= 500,000)
n = int(input())

# 예상 등수 <= 500,000
prediction = [int(input()) for _ in range(n)]
prediction.sort()

# 불만도 합
result = 0 
for i in range(1, n+1):
    result += abs(i-prediction[i-1])

# 불만도 출력
print(result)


