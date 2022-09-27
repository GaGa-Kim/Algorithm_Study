# 2839번
# 최대한 적은 봉지로 설탕을 정확하게 n kg 배달해야 할 때, 
# 봉지를 몇 개 가져가면 되는지 구하는 프로그램
# 봉지는 3kg, 5kg으로만 구성되어 있다.

# 3 <= n <= 5,000
n = int(input())

result = 0
while True:
    if n % 5 == 0:
        result += n//5
        print(result)
        break
    n -= 3
    result += 1
    
    # 정확하게 n kg을 만들 수 없다면 -1 출력
    if n < 0:
        print(-1)
        break

