n = list(input())
n.sort(reverse=True)

if '0' not in n:
    print(-1)
else:
    max_num = int(''.join(n))
    if max_num % 3 != 0:
        print(-1)
    else:
        print(max_num)
