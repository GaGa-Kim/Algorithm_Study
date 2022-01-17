# N개의 동전을 이용해 만들 수 없는 
# 양의 정수 금액 중 최솟값을 구하는 프로그램 작성

# 양의 정수, 1 <= N <= 1,000
n = int(input())

# N개의 화폐 단위(1,000,000 이하의 자연수)
coin_type = list(map(int, input().split()))
# 오름차순 정렬
coin_type.sort()

# 1원을 만들 수 있는지 확인하기 위해 1로 설정
target = 1
for i in coin_type: 
    # 만들 수 있는 금액 찾았을 때 반복 종료
    if target < i: 
        break
    target += i 
    
print(target)

# 화폐 단위 오름차순 정렬 
# (!) 1부터 차례대로 특정한 금액을 만들 수 있는지 확인
# 1 ~ target-1까지의 모든 금액을 만들 수 있다고 가정,
# target 금액 또한 만들 수 있는지 확인하면 됨.
# 만약 만들 수 있다면 target값을 증가시켜 같은 방식 반복