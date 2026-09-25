n = int(input())
k = 0
p = 1
while p * 3 < n:
    p *= 3
    k += 1
print(k + 1)
