# # 백준 18406번

# 점수 N을 자릿수를 기준으로 반으로 나누어
# 왼쪽 부분의 각 자릿수 합 == 오른쪽 부분의 각 자릿수 합 ~> 럭스
# 럭스를 사용할 수 있는 상태 여부를 알려주는 프로그램
# N의 자릿수는 늘 짝수

import sys
input = sys.stdin.readline

# 점수 N, 정수, 10 <= N <= 99,999,999
n = input().rstrip('\n')
mid = len(n)//2

left = 0
right = 0
for i in range(mid):
    left += int(n[i])
    
for i in range(mid, len(n)):
    right += int(n[i])
        
if left == right:
    print('LUCKY')
else:
    print('READY')