# N명의 모험가
# 공포도가 X인 모험가는 반드시 X명 이상으로 그룹 구성
# 모든 모험가가 그룹에 포함될 필요는 x
# 여행을 떠날 수 있는 그룹 수의 최댓값 구하기

# 모험가의 수 N(1<= N <=100,000)
n = int(input())

# N명의 모험가들의 공포도
data = list(map(int, input().split()))
# 공포도 오름차순 정렬
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data:
    count += 1
    if count >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면
        result += 1 # 그룹 결성 완료
        count = 0 
        
print(result)