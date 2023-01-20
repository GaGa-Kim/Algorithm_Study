import sys
input = sys.stdin.readline

s = input().rstrip()
m = 0
max = ''
min = ''
for i in s:
    # M일 경우
    if i == 'M':
        m += 1
    # K일 경우
    else:
        # K 앞에 M이 있을 경우
        if m > 0:
            # 최댓값은 5 * (10 ** 앞에서 나온 M의 갯수)
            max += str(5 * (10 ** m))
            # 최솟값은 (10 ** 앞에서 나온 M의 갯수) + 5
            min += str(10 ** m + 5)
        # K 앞에 M이 없을 경우
        else:
            max += '5'
            min += '5'
        m = 0
# M으로 끝날 경우
if m > 0:
    max += '1' * m
    min += str(10 ** (m - 1))

print(max)
print(min)
