import sys, heapq
input = sys.stdin.readline

n = int(input())
max_h = [] # 최대힙 우선순위 큐
min_h = [] # 최소힙 우선순위 큐
id = [False] * 100001 # 이중 우선순위 큐 동기화를 위한 리스트 
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(max_h, (-l, -p))
    heapq.heappush(min_h, (l, p))
    id[p] = True # 동기화를 위해 해당 정수가 큐 안에 있음을 명시

m = int(input())
for _ in range(m):
    command = input().split() 
    # 출력 연산
    if command[0] == 'recommend':
        if command[1] == '1':
            # 최대힙과 최소힙 동기화
            while not id[-max_h[0][1]]:
                heapq.heappop(max_h)
            # 최댓값 출력
            print(-max_h[0][1])
        else:
            # 최대힙과 최소힙 동기화
            while not id[min_h[0][1]]:
                heapq.heappop(min_h)
            # 최솟값 출력
            print(min_h[0][1])
    # 제거 연산
    elif command[0] == 'solved':
        id[int(command[1])] = False # 동기화를 위해 해당 정수가 큐 안에 없음을 명시
    # 삽입 연산
    else:
        p = int(command[1])
        l = int(command[2])
        # 최대힙과 최소힙 동기화
        while not id[-max_h[0][1]]:
            heapq.heappop(max_h)
        while not id[min_h[0][1]]:
            heapq.heappop(min_h)
        id[p] = True # 동기화를 위해 해당 정수가 큐 안에 있음을 명시
        heapq.heappush(max_h, (-l, -p))
        heapq.heappush(min_h, (l, p))