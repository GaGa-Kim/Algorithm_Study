import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
d = [[0 for _ in range(2 * len(a))] for _ in range(2 * len(a) - 1)]

for i in range(len(a)):
    # 짝수 칸에 a 이름
    d[0][i * 2] = alphabet[ord(a[i]) - 65]
for j in range(1, len(b) + 1):
    # 홀수 칸에 b 이름
    d[0][j * 2 - 1] = alphabet[ord(b[j - 1]) - 65]

for i in range(1, 2 * len(a) - 1):
    for j in range(2 * len(a) - 1):
        # 10을 넘을 경우 마지막 글자만 나오게
        d[i][j] = int(str(d[i - 1][j] + d[i - 1][j + 1])[-1])

print(str(d[-1][0]) + str(d[-1][1]))