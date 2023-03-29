# 1181번
# 알파벳 소문자로 이루어진 n개의 단어가 들어오면 아래 조건에 따라 정렬
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순
# (단, 중복된 단어는 하나만 남기고 제거)

import sys
# strip() ~ 개행 문자 제거
input = sys.stdin.readline

# 1 ≤ n ≤ 20,000
n = int(input())
data = [input().strip() for _ in range(n)]
data = list(set(data))

data.sort(key = lambda x : (len(x), x))

# 여기서 set(data)하면 안 되는 이유 ~ set은 순서x
for i in data:
    print(i)