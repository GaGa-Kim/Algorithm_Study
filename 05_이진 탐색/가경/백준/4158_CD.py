import sys
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    array1 = [int(sys.stdin.readline()) for _ in range(n)]
    array2 = [int(sys.stdin.readline()) for _ in range(m)]
    count = 0

    for cd in array2:
        start = 0
        end = n - 1
        # 이진 탐색 반복문
        while start <= end:
            mid = (start + end) // 2
            if array1[mid] == cd:
                count += 1
                break
            elif array1[mid] > cd:
                end = mid - 1
            else:
                start = mid + 1

    print(count)

