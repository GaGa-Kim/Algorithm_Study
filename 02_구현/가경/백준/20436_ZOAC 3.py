import sys
input = sys.stdin.readline

l, r = map(str, input().split())
words = list(input().rstrip())

# 자판
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
# 한글 모음 쪽 자판 (오른쪽 검지손가락만 가능)
vowels = 'yuiophjklbnm'

# 왼손 검지손가락과 오른손 검지손가락의 처음 위치
xl, yl, xr, yr = None, None, None, None
for i in range(len(keyboard)):
    if l in keyboard[i]:
        xl = i
        yl = keyboard[i].index(l)
    if r in keyboard[i]:
        xr = i
        yr = keyboard[i].index(r)

time = 0
for word in words:
    time += 1
    # 모음이라면 - 오른손 검지손가락
    if word in vowels:
        for i in range(len(keyboard)):
            # 글자의 위치
            if word in keyboard[i]:
                nx = i
                ny = keyboard[i].index(word)

                # 걸리는 시간과 손가락 위치 변경
                time += abs(nx - xr) + abs(ny - yr)
                xr = nx
                yr = ny
                break
    # 자음이라면 - 왼손 검지손가락
    else:
        for i in range(len(keyboard)):
            # 글자 위치
            if word in keyboard[i]:
                nx = i
                ny = keyboard[i].index(word)

                # 걸리는 시간과 손가락 위치 변경
                time += abs(nx - xl) + abs(ny - yl)
                xl = nx
                yl = ny
                break
print(time)