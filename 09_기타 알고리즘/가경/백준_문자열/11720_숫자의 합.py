n = int(input())
numbers = list(input())

result = 0
for i in range(n):
    result += int(numbers[i])
print(result)