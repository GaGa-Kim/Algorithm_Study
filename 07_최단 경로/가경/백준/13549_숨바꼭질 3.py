import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
distance = [INF] * (100001)

def dijkstra(start, end):
    if end <= start:
        print(start - end)
        return

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for i in [now + 1, now - 1, now * 2]:
            if 0 <= i <= 100000:
                # 순간이동 (0초 후)
                if i == now * 2 and distance[i] == INF:
                    distance[i] = dist
                    heapq.heappush(q, (dist, i))
                # 걷기 (1초 후)
                elif distance[i] == INF:
                    distance[i] = dist + 1
                    heapq.heappush(q, (dist + 1, i))
    print(distance[end])

dijkstra(n, k)