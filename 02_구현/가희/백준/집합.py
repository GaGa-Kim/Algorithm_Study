# 11723번
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램

# 1 <= x <= 20
# 1. add x: S에 x를 추가 , 이미 있으면 무시
# 2. remove x: S에서 x 제거, 이미 없으면 무시
# 3. check x: S에 x가 있으면 1, 없으면 0 출력
# 4. toggle x: S에 x가 있으면 x 제거, 없으면 추가
# 5. all: S를 {1, 2, ..., 20}으로 바꿈
# 6. empty: S를 공집합으로 바꿈

#----------------시간 초과-------------------------
# 수행해야 하는 연산 수 M (1 <= M <= 3,000,000)
m = int(input())

s =  set()
# 수행해야 하는 연산
for _ in range(m):
    tmp = input().split()
    
    if len(tmp) > 1:
        op, num = tmp[0], int(tmp[1])
    else:
        op = tmp[0]
    
    if op == 'add':
        s.add(num)
    elif op == 'remove':
        s.discard(num)
    elif op == 'check':
        # check 연산 주어질 때마다 결과 출력
        if num in s:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif op == 'all':
        s = set([i for i in range(1,21)])
    elif op == 'empty':
        s.clear() 


#--------------통과 코드----------------
import sys
input = sys.stdin.readline

# 수행해야 하는 연산 수 M (1 <= M <= 3,000,000)
m = int(input())

s =  set()
# 수행해야 하는 연산
for _ in range(m):
    tmp = input().split()
    
    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1,21)]) 
        else:
            s.clear()
        continue

    op, num = tmp[0], int(tmp[1])
    
    if op == 'add':
        s.add(num)
    elif op == 'remove':
        s.discard(num)
    elif op == 'check':
        # check 연산 주어질 때마다 결과 출력
        if num in s:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)