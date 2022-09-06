from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

# 산술평균
print(round(sum(numbers) / n))

# 중앙값
print(numbers[n // 2])

# 최빈값
count = Counter(numbers).most_common(2) 
if len(numbers) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

# 범위
print(numbers[-1] - numbers[0])