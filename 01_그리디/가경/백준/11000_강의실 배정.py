import sys, heapq
input = sys.stdin.readline

n = int(input())

schedule_list = []
for _ in range(n):
    schedule_list.append(list(map(int, input().split())))
# 끝나는 시간 오름차순으로 정렬
schedule_list.sort()

room = []
# 첫 번째 수업 끝나는 시간 저장
heapq.heappush(room, schedule_list[0][1])
for i in range(1, n):
    # 앞의 수업의 끝나는 시간보다 시작 시간이 느리거나 같을 경우
    if schedule_list[i][0] >= room[0]:
        # 이전에 사용한 강의실 사용 가능
        heapq.heappop(room)
    heapq.heappush(room, schedule_list[i][1])

print(len(room))