word = list(input())
words = []

# 적어도 길이가 1이상이어야 하므로 1부터 시작하여 모든 경우의 수를 실행
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        words.append(''.join(a + b + c))

print(sorted(words)[0])