# 1543번
# 문서와 검색하려는 단어가 주어졌을 때, 
# 그 단어가 최대 몇 번 중복되지 않게 등장하는지 구하는 프로그램

# word 길이만큼 doc를 자른 후 비교하고 맞으면 count+1
# word와 doc를 자른 부분이 같으면, 인덱스 + word 길이
# word와 doc를 자른 부분이 다르면, 인덱스 + 1


# 문서 doc (문서 길이 <= 2,500)
doc = input()
# 검색하려는 단어
word = input()

count = 0
i = 0
while i <= (len(doc) - len(word)):
    if doc[i:i + len(word)] == word:
        count += 1
        i += len(word)
    else:
        i += 1

print(count)

#-------------------------------------------------

doc = input()
word = input()

# 문자열.split('구분자') ~ 문자열을 잘라서 리스트로 만들어 줌
sp_doc = doc.split(word)
# print(sp_doc)
print(len(sp_doc) - 1)
