for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    start = 0
    count = 0
    for i in range(n):
        while True:
            # a가 b보다 같거나 작아질 때까지 가장 큰 인덱스를 찾아서 그 인덱스까지의 갯수를 모두 더해줌
            if start == m or a[i] <= b[start]:
                count += start
                break
            else:
                start += 1
    print(count)
