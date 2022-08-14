# 백준 14501번
# 상담을 적절히 했을 때, 얻을 수 있는 최대 수익 구하는 프로그램

# 오늘부터 n+1일째 되는 날 퇴사하기 위해 
# 남은 n일 동안 최대한 많은 상담을 할 예정 (1 <= n <= 15)

# 상담은 하루에 하나씩 서로 다른 사람
# Ti ~ 상담을 완료하는 데 걸리는 기간 (1 <= Ti <= 5)
# Pi ~ 상담했을 때 받을 수 있는 금액 (1 <= Pi <= 1,000)


n = int(input())

t = [] # 각 상담 완료하는 데 걸리는 기간
p = [] # 각 상담 완료했을 때 받을 수 있는 금액

dp = [0] * (n+1)
max_value= 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
# 리스트 뒤에서부터 확인
for i in range(n-1, -1, -1):
    time = t[i] + i 
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간 벗어나는 경우
    else:
        dp[i] = max_value
        
print(max_value)