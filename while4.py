n = int(input())
while n % 3 == 0:
    n //= 3
print("TRUE" if n == 1 else "FALSE")
