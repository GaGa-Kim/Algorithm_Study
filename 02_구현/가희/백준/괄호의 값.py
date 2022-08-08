# 2504번
# 주어진 괄호열을 읽고 괄호의 값 계산

# 올바른 괄호열) (), [] 짝이 맞아야 함

# <괄호 값>
# 1. () ~ 2
# 2. [] ~ 3
# 3. (x) ~ 2x
# 4. [x] ~ 3x
# 5. 올바른 괄호열 x와 y가 결합된 xy의 괄호값은
# 값(xy) = 값(x) + 값(y) 으로 계산

# 괄호열을 나타내는 문자열 (1 <= s <= 30)
s = list(input())

stack = []
result = 0
tmp = 1 
    
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
        
    elif s[i] == '[':
        stack.append(s[i])
        tmp *= 3
        
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        if s[i-1] == '(':
            result += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        if s[i-1] == '[':
            result += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)        
else:
    print(result)

# 반례 ) ([)] 