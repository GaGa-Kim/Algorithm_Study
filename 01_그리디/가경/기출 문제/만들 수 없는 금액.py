# 만들 수 없는 금액.py
n = int(input()) # 동전의 개수
data = list(map(int, input().split())) # 각 동전의 화폐 단위
data.sort() # 화폐 단위 기준으로 오름차순 정렬

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)