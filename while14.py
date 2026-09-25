a = float(input())
k = 0
s = 0.0
while s + 1.0 / (k + 1) < a:
    k += 1
    s += 1.0 / k
print(k, s)
