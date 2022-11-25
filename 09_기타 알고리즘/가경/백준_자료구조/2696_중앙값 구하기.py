import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    data = []
    # 원소는 한 줄에 10개씩 입력
    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, input().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, input().split())))

    big_h = [] # 중앙값보다 큰 수들의 우선순위 큐
    small_h = [] # 중앙값보다 작은 수들의 우선순위 큐
    middle = data[0] # 중앙값
    result = [middle] # 중앙값들
    for index, value in enumerate(data[1:], 1): # value는 data[1]부터, index는 1부터 시작
        # 입력값이 중앙값보다 크다면
        if value > middle:
            # big 큐에 추가
            heapq.heappush(big_h, value)
        # 입력값이 중앙값보다 작거나 같다면
        else:
            # small 큐에 추가
            heapq.heappush(small_h, -value)

        # 홀수번째 수일 때 (인덱스가 짝수일 때)
        if index % 2 == 0:
            # small 큐의 크기가 big 큐의 크기보다 작다면
            if len(small_h) < len(big_h):
                # 이전의 중앙값을 small 큐에 넣고
                heapq.heappush(small_h, -middle)
                # big 큐의 최솟값이 새로운 중앙값이 됨
                middle = heapq.heappop(big_h)
            # small 큐의 크기가 big 큐의 크기보다 크다면
            elif len(small_h) > len(big_h):
                # 이전의 중앙값을 big 큐에 넣고
                heapq.heappush(big_h, middle)
                # small 큐의 최댓값이 새로운 중앙값이 됨
                middle = -heapq.heappop(small_h)
            result.append(middle)

    print(len(result))
    # 한 줄에 10개씩 출력
    for i in range(len(result)):
        if i != 0 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()