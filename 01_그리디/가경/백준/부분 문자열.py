while True:
    try:
        s, t = input().split()

        i = 0
        target = 0
        # 하나씩 비교하면서 같을 경우만
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                # 부분 문자열이 있을 경우 (문자열의 길이가 다 채워진 경우)
                if i == len(s):
                    target = 1
                    break
        
        if target == 1:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break