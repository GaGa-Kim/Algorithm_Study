from itertools import combinations
import sys
input = sys.stdin.readline

words = list(input().rstrip())
stack = []
temp = []
result = set()

# 스택에 괄호만 넣어 괄호쌍 위치 구하기
for index, word in enumerate(words):
    if word == '(':
        stack.append(index)
    elif word == ')':
        start = stack.pop()
        end = index
        temp.append([start, end])

# 조합을 통해 괄호 제거
for i in range(1, len(temp) + 1):
    # 경우의 수 (temp 리스트에서 i개의 원소를 골라 나열)
    for combi in combinations(temp, i):
        target = list(words)
        # 괄호 제거
        for j in combi:
            target[j[0]] = ''
            target[j[1]] = ''
            result.add(''.join(target))

for i in sorted(list(result)):
    print(i)
