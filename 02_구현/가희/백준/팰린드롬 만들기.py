# 1213번
# 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램

# <팰린드롬(Palindrome)>
# 어떤 단어나 특정 문장을 뒤집어도 같은 말이 되는 것
# = 회문 ex) 일요일
# 팰린드롬을 만들기 위해서는 
# 1) 이름 길이가 짝수인 경우 ~ 각 알파벳이 짝수 개만 존재해야 함
# 2) 이름 길이가 홀수인 경우 ~ 홀수 개인 알파벳 하나 있어도 됨

from collections import Counter 

# 임한수의 영어 이름(알파벳 대문자, 최대 50글자)
name = list(input())
name.sort()             # 사전 순으로 정렬(오름차순 정렬)
name_cnt = Counter(name)   # 문자 빈도수 확인

odd_cnt = 0     # 홀수 개수
odd_chr = ''    # 홀수 문자(가운데 위치)
alpha = ''
for i in name_cnt:
    # 문자 개수가 홀수인 경우
    if name_cnt[i] % 2 == 1 :
        odd_cnt += 1
        odd_chr += i
    # 홀수 개수가 2개 이상이면 불가능
    if odd_cnt > 1:
        print("I'm Sorry Hansoo")

result = ''
for i in range(0, len(name), 2):
    # 처음으로 빈도수가 홀수인 알파벳을 만날 경우 
    if name_cnt[name[i]] % 2 == 1:
        # 빈도수만 -= 1을 해줘서, 
        # 이 다음부터 팰린드롬 문자열에 추가되게 해줌
        name_cnt[name[i]] -= 1
    else:
        result += name[i]

print(result + odd_chr + result[::-1])

#----------------------------------------------------
# 더 빠른 코드
arr = input()
arr_cnt=[0 for _ in range(26)]
for a in arr: #알파벳만큼의 길이를 생성한 후, 배열에 저장
    arr_cnt[ord(a)-65]+=1

odd = 0
odd_alphabet = ''
alphabet=''

for i in range(26):
    if arr_cnt[i]%2 == 1: #저장된 갯수가 홀수이면
        odd+=1 
        odd_alphabet+= chr(i+65) #홀수만 모아놓은 배열에 저장
    alphabet+=chr(i+65)*(arr_cnt[i]//2)

if odd>1: #만약 홀수가 두개 이상이면 팰린드롬 못만듦 (가운데에 하나만 있어야 하므로)
    print("I'm Sorry Hansoo")
else:
    print(alphabet+odd_alphabet+alphabet[::-1])