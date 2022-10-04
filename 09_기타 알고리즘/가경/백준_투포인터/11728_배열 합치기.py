import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
a_pointer, b_pointer = 0, 0
while a_pointer != len(a) or b_pointer != len(b):
    # 배열 a를 모두 넣었다면 남은 배열 b를 넣음
    if a_pointer == len(a):
        answer.append(b[b_pointer])
        b_pointer += 1
    # 배열 b를 모두 넣었다면 남은 배열 a를 넣음
    elif b_pointer == len(b):
        answer.append(a[a_pointer])
        a_pointer += 1
    # 더 작은 것을 먼저 넣음
    else:
        if a[a_pointer] < b[b_pointer]:
            answer.append(a[a_pointer])
            a_pointer += 1
        else:
            answer.append(b[b_pointer])
            b_pointer += 1
print(*answer)