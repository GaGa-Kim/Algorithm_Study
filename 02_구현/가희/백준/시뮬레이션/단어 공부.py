# 1157번
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
# (단, 대문자와 소문자를 구분하지 않는다.)

# 200ms------------------------------------------------------

# 단어 길이 <= 1,000,000
word = input().upper()
alp = [0] * 26 # 알파벳 개수 26개

for i in word:
    alp[ord(i)-65] += 1

max_alp = alp.index(max(alp))
result = [i for i, v in enumerate(alp) if v==max(alp)]

# 가장 많이 사용된 알파벳이 여러 개인 경우 ? 출력
if len(result) > 1:
    print('?')
else: # 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
    print(chr(max_alp+65))
    
# 시간 단축---------------------------------------------------

word = input().upper()
# 입력받은 문자열에서 중복값 제거
alp_set = list(set(word))

alp_cnt = []
for i in alp_set:
    alp_cnt.append(word.count(i))

if alp_cnt.count(max(alp_cnt)) > 1:
    print('?')
else:
    print(alp_set[alp_cnt.index(max(alp_cnt))])



