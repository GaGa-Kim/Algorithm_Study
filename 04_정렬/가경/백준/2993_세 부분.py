word = input()
words = []

# 세 부분으로 나누어야 하므로 i는 맨 뒤에서 2번째까지, j는 1번째까지, k는 마지막까지
for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        for k in range(j + 1, len(word)):
            if len(word) == len(word[i:j] + word[j:k] + word[k:]):
                a = word[i:j]
                b = word[j:k]
                c = word[k:]
                words.append([a[::-1]+b[::-1]+c[::-1]])
words.sort()
print(''.join(words[0]))