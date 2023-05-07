import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
# 원형이므로 초밥을 이어줌
sushi.extend(sushi)

start = 0 # 시작점
end = 0 # 끝점
sushi_dict = defaultdict(int) # 먹은 초밥 종류
answer = 0

sushi_dict[c] += 1 # 쿠폰으로 무조건 먹음
# 시작점을 차례대로 증가시키며 반복
for end in range(len(sushi)):
    sushi_dict[sushi[end]] += 1
    # k보다 클 경우부터 회전
    if end >= k - 1:
        answer = max(answer, len(sushi_dict))
        # 오른쪽으로 회전 (맨 왼쪽 초밥 제거, 오른쪽에 초밥 추가)
        sushi_dict[sushi[start]] -= 1
        if sushi_dict[sushi[start]] == 0:
            del sushi_dict[sushi[start]]
        start += 1
print(answer)