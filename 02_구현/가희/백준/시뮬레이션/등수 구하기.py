# 1205번
# 새로운 점수가 랭킹 리스트에서 몇 등인지 구하는 프로그램
# (만약 점수가 랭킹 리스트에 올라갈 수 없으면 -1 출력)
# 랭킹 리스트 꽉 차면 새 점수가 이전 점수보다 좋을 때만 올라감

# 리스트에 있는 점수 0 <= n <= p
# 새로운 점수 (0 <= 모든 점수 <= 2,000,000,000)
# 랭킹 리스트에 올라갈 수 있는 점수 개수 p <= 50
n, new, p = map(int, input().split())

if n == 0:
    print(1)
elif n > 0: # 현재 랭킹 리스트에 있는 점수(n > 0일 때만 주어짐)
    ranking = list(map(int, input().split()))
    
    # ranking[n-1]가 ranking[-1]보다 빠름
    if n == p and ranking[n-1] >= new:
        print(-1)
        
    else:
        rank = 1
        for i in range(n):
            if new < ranking[i]:
                rank += 1
        print(rank)

    