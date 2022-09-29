import sys
input = sys.stdin.readline

n, m = map(int, input().split())
int_dict = {}
name_dict = {}
for i in range(1, 1 + n):
    name = input().rstrip()
    int_dict[i] = name
    name_dict[name] = i

for j in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(int_dict[int(question)])
    else:
        print(name_dict[question])
