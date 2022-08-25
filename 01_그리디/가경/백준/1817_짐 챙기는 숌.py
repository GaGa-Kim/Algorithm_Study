n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    book = list(map(int, input().split()))

    weight = 0
    count = 1
    for i in book:
        weight += i
        if weight > m: 
            count += 1
            weight = i
    
    print(count)
