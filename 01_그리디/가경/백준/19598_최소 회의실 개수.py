import sys, heapq
input = sys.stdin.readline

n = int(input())

meeting_list = []
for _ in range(n):
    meeting_list.append(list(map(int, input().split())))
# 끝나는 시간 오름차순으로 정렬
meeting_list.sort()

room = []
# 첫 번째 회의 끝나는 시간 저장
heapq.heappush(room, meeting_list[0][1])
for i in range(1, n):
    # 앞의 회의가 끝나는 시간보다 시작 시간이 느리거나 같을 경우
    if meeting_list[i][0] >= room[0]:
        # 이전에 사용한 회의실 사용 가능
        heapq.heappop(room)
    heapq.heappush(room, meeting_list[i][1])

print(len(room))