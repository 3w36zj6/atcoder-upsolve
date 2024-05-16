import math

A, B = map(int, input().split())
lcm = math.lcm(A, B)

print(lcm if lcm <= 10**18 else "Large")
