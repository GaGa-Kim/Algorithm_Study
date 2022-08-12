import sys
input = sys.stdin.readline

n = int(input())
words = {}
for _ in range(n):
    word = input().rstrip()
    for i in range(len(word)):
        # 원형에 따라 위치를 바꾸면 사이클 단어 생성
        cycle = word[i:] + word[:i]
        if not words.get(cycle):
            # '사이클 단어' : '원래 단어' 삽입
            words[cycle] = word
# values 값에 따라 중복을 없애도록 set 사용
print(len(set(words.values())))
