import sys
input = sys.stdin.readline

n = int(input())
s = input()

color = {'B':0, 'R':0}
color[s[0]] += 1
for i in range(1, n):
    # 이전과 다른 색이 나올 경우 그 색의 횟수 증가
    if s[i] != s[i - 1]:
        color[s[i]] += 1

# 칠할 횟수가 더 많은 색으로 모두 칠한 후, 나머지 색을 칠함
result = min(color['B'], color['R']) + 1
print(result)