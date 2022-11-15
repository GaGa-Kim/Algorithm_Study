import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left, right = 0, n - 1 # 투 포인터
result = 2e+9+1 # 최대 용액 합은 1000000000 + 100000000 = 2000000001
results = []
while left < right:
    solutions_left = solutions[left]
    solutions_right = solutions[right]
    solutions_total = solutions_left + solutions_right

    # 두 용액의 합 비교
    if abs(solutions_total) < result:
        result = abs(solutions_total)
        results = [solutions_left, solutions_right]

    # 두 용액의 합이 0보다 작다면, 합을 늘리기 위해 left 포인터 증가
    if solutions_total < 0:
        left += 1
    # 두 용액의 합이 0보다 크다면, 합을 줄이기 위해 right 포인터 감소
    else:
        right -= 1
print(results[0], results[1])