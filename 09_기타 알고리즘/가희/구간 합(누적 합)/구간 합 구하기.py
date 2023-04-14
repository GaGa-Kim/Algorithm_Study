# 백준 11659번

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

temp = 0
s = [0]
for i in a:
    temp += i
    s.append(temp)
    
    
for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i-1])
    