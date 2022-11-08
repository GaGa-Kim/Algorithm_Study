import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort()

result = []
# 운동기구 갯수가 홀수라면 하루는 가장 큰 근손실의 운동기구 하나만 사용
if (n % 2 == 1):
    result.append(t[-1])
    # 운동기구에서 제외
    t = t[:-1]
# 나머지 운동기구를 가지고 하루에 두 개씩 사용
for i in range(len(t) // 2):
    result.append(t[i] + t[len(t) - 1 - i])
# 한 번 받을 때의 근손실 정도 중 가장 큰 근손실의 합을 출력
print(max(result))
