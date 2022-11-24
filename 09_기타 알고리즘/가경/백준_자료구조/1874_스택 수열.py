import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
count = 1
flag = False
for i in range(n):
    number = int(input())
    # 입력한 수를 만날 때까지 오름차순으로 push
    while count <= number: 
        stack.append(count)
        answer.append('+')
        count += 1
    # stack의 Top가 입력한 숫자와 같다면 꺼내서 수열로 만들어줌
    if stack[-1] == number:
        stack.pop()
        answer.append('-')
    # 아니라면 수열을 만들 수 없음
    else:
        print('NO')
        flag = True
        break

if flag == False:
    for i in answer:
        print(i)

