answer = 0
for i in range(int(input())):
    word = input()
    count = 0
    for j in range(len(word) - 1):
        # 이어지는 문자가 다를 때
        if word[j] != word[j + 1]:
            # 남은 문자열에서 word[j]가 나타나면 그룹 단어가 아님
            nword = word[j + 1:]
            if nword.count(word[j]) > 0:
                count += 1
    if count == 0:
        answer += 1

print(answer)
