import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0 # 투 포인터

# 숫자 빈도 리스트
counter = [0] * (max(numbers) + 1)
result = 0
while right < n:
    # 숫자 빈도가 k번 미만이라면 right 포인터 증가
    if counter[numbers[right]] < k:
        counter[numbers[right]] += 1
        right += 1
    # 숫자 빈도가 k번 이상이라면 left 포인터 증가
    else:
        counter[numbers[left]] -= 1
        left += 1
    result = max(result, right - left)
print(result)