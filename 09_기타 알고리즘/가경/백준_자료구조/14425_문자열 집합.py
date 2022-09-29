import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(n):
    string = input().rstrip()
    s.add(string)

count = 0
for _ in range(m):
    question = input().rstrip()
    if question in s:
        count += 1
print(count)