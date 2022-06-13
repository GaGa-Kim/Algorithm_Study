n, s, r = map(int, input().split())
team1 = list(map(int, input().split())) # 손상된 팀 번호
team2 = list(map(int, input().split())) # 카약을 하나 더 가져온 팀 번호

count = s

# 카약을 하나 더 가져온 팀의 카약이 손상된 경우
for i in team2: 
    if i in team1:
        team1.remove(i)
        team2.remove(i)
        count -= 1

# 카약을 다음이나 전에 경기하는 팀에게만 빌리는 경우
for i in team1:
    for j in team2:
        if j - 1 <= i <= j + 1:
            team2.remove(j)
            count -= 1
            break
        elif j + 1 < i:
            break
    
print(count)