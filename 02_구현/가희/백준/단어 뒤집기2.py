# 17413번

# 문자열 s가 주어졌을 때, 단어만 뒤집음
# 1. 알파벳 소문자, 숫자, 공백, 특수문자(<,>)로만 구성
# 2. 문자열의 시작과 끝은 공백 x
# 3. <와 >가 문자열에 있는 경우 번갈아가면서 등장하며,
#   <이 먼저 등장. <,>의 개수는 같음

# 태그는 <로 시작해서 >로 끝나는 길이가 3이상인 부분 문자열,
# <와 > 사이에는 알파벳 소문자와 공백만 있음.
# 태그는 단어가 아니고, 태그와 단어 사이에 공백 x

# 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고,
# 연속하는 두 단어는 공백 하나로 구분

# 문자열 s (s <= 100,000)
s = input()

flag = False # True: 정상 출력, False: 뒤집어서 출력
stack = "" 
result = ""

for i in s:    
    if not flag:         # 뒤집어서 출력
        if i == '<':
            flag = True
            stack += i
        elif i == ' ':
            stack += i
            result += stack
            stack = ""
        else:
            stack = i + stack
    else:                   # 정상 출력
        stack += i
        if i == '>':
            flag = False
            result += stack
            stack = ""
            
print(result + stack)
        
# <, 공백 만나기 전에는 스택에 저장
# < 만나면 다른 스택에다가 넣어두고, > 만나면 스택이랑 합침 