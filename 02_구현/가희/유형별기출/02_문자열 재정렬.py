# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열
# 모든 알파벳 오름차순 정렬하여 이어서 출력한 뒤,
# 그 뒤에 모든 숫자를 더한 값 이어서 출력

# 문자열 S, 1 <= S의 길이 <= 10,000
s = input()
result = []
value = 0

for i in s:
    # 알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        result.append(i)
    # 숫자인 경우 따로 더함
    else:
        value += int(i)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
    
# 리스트를 문자열로 변환하여 출력
print(''.join(result))


# <-- 더 공부할 내용 -->
# - isalpha()
# - 알파벳 정렬
# - 리스트를 문자열로 변환하기
        
    
    