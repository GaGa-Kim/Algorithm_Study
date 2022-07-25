# 7568번
# 각 사람의 덩치 등수를 계산하여 출력

# 덩치 ~ (몸무게, 키)
# n명의 집단에서 각 사람의 덩치 등수
# = 자신보다 더 큰 덩치의 사람의 수

# 전체 사람의 수 n (2 <= n <= 50)
n = int(input())

list = []
# (몸무게, 키) ~ (x, y) (10 <= x,y <=200)
for i in range(n):
    x, y = map(int, input().split())
    list.append((x,y))
    
for i in list:
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
    