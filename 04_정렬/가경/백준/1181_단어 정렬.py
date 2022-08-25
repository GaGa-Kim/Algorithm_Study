import sys

n = int(input())
words = []
for _ in range(n):
    word = str(sys.stdin.readline().rstrip())
    length = len(word)
    words.append((word, length))

# 한 번씩만 출력하기 위해 중복 제거
words = list(set(words))

# 길이 순, 사전 순 정리
words.sort(key = lambda word: (word[1], word[0]))

for word in words:
    print(word[0])