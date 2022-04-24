# 럭키 스트레이트.py
n = input() # 점수
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(len // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기 
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")