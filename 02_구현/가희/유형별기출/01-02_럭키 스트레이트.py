# # 백준 18406번

# 교재 예시 코드(좀 더 느리지만 이렇게도 코드를 짤 수 있구나 해서^^..)

# 점수 N을 자릿수를 기준으로 반으로 나누어
# 왼쪽 부분의 각 자릿수 합 == 오른쪽 부분의 각 자릿수 합 ~> 럭스
# 럭스를 사용할 수 있는 상태 여부를 알려주는 프로그램
# N의 자릿수는 늘 짝수

import sys
input = sys.stdin.readline

# 점수 N, 정수, 10 <= N <= 99,999,999
n = input().rstrip('\n')
length = len(n)
sum = 0

# 왼쪽 부분 자릿수 합 더하기
for i in range(length//2):
    sum += int(n[i])

# 오른쪽 부분 자릿수 합 더하기
for i in range(length//2, length):
    sum -= int(n[i])
    
# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if sum == 0:
    print("LUCKY")
else:
    print("READY")
    