import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid
        if total > m:
            break
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
