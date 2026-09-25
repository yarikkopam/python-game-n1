n = int(input())
result = 0.0
sign = 1
for i in range(1, n + 1):
    value = 1 + i / 10
    result += sign * value
    sign *= -1
print(result)
