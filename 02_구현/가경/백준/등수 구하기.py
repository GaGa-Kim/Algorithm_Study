n, t, p = map(int, input().split())

if n:
    points = list(map(int, input().split()))
    points.append(t)
    points.sort(reverse=True)
    rank = points.index(t) + 1
    
    if rank > p:
        print(-1)
    else:
        if n == p and t == points[-1]:
            print(-1)
        else:
            print(rank)
else:
    print(1)
