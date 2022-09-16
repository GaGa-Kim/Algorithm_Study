n, k = map(int, input().split())

count = 0
removed = [False] * (n + 1)
for i in range(2, len(removed) + 1):
    # i부터 +i씩 만큼 n + 1까지 (즉, i의 배수)
    for j in range(i, n + 1, i):
        if removed[j] == False:
            removed[j] = True
            count += 1
            if count == k:
                print(j)
                break