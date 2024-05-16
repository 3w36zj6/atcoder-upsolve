H, W = map(int, input().split())

print(((H + 1) // 2) * ((W + 1) // 2) if H != 1 and W != 1 else H * W)
