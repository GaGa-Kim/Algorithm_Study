import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
count = 0
for i in coins: # 화폐의 종류만큼 반복
    count += k // i # 해당 화폐로 거슬러 줄 수 있는 개수 세기
    k %= i 

print(count)