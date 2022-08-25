i = 1
while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break

    count = (v // p) * l
    count += min((v % p), l)
    print("Case %d: %d" %(i, count))
    i += 1