a, b = map(int, input().split())
n = int(input())
favorite = []
for _ in range(n):
    favorite.append(int(input()))
    
# 1MHz씩 이동
sum1 = abs(b - a) 

# 즐겨찾기에서 이동할 경우
for i in range(n):
    favorite[i] = abs(b - favorite[i])
sum2 = min(favorite)

print(min(sum1, sum2 + 1))