n = int(input())
k = 0
s = 0
while s + k + 1 <= n:
    k += 1
    s += k
print(k, s)
