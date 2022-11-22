import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    max_h = [] # 최대힙 우선순위 큐
    min_h = [] # 최소힙 우선순위 큐
    id = [False] * 1000001 # 이중 우선순위 큐 동기화를 위한 리스트
    for i in range(k):
        cal, n = input().split()
        # 삽입 연산
        if cal == 'I':
            heapq.heappush(max_h, (-int(n), i))
            heapq.heappush(min_h, (int(n), i))
            id[i] = True # 동기화를 위해 해당 정수가 큐 안에 있음을 명시
        # 삭제 연산
        else:
            if n == '1':
                # 최대힙과 최소힙 동기화
                while max_h and not id[max_h[0][1]]:
                    heapq.heappop(max_h)
                # 최댓값 삭제
                if max_h:
                    id[max_h[0][1]] = False # 동기화를 위해 해당 정수가 큐 안에 없음을 명시
                    heapq.heappop(max_h)
            else:
                # 최대힙과 최소힙 동기화
                while min_h and not id[min_h[0][1]]:
                    heapq.heappop(min_h)
                # 최솟값 삭제
                if min_h:
                    id[min_h[0][1]] = False # 동기화를 위해 해당 정수가 큐 안에 없음을 명시
                    heapq.heappop(min_h)
    # 최대힙과 최소힙 동기화
    while max_h and not id[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not id[min_h[0][1]]:
        heapq.heappop(min_h)

    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')