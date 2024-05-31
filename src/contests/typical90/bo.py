import numpy as np

N, k = input().split()
K = int(k)

n = int(N, 8)

for _ in range(K):
    n_base_9 = np.base_repr(n, base=9)
    n = int(str(n_base_9).replace("8", "5"), 8)

print(np.base_repr(n, base=8))
