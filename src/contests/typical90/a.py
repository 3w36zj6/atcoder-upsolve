N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


def check(x: int) -> bool:
    """すべてのピースの長さがx以上になるように切ることができるかを判定する"""
    pre_cut_position: int = 0
    piece_count: int = 0
    for a in A:
        if a - pre_cut_position >= x:
            piece_count += 1
            pre_cut_position = a

    # 最後のピース
    if L - pre_cut_position >= x:
        piece_count += 1

    return piece_count >= K + 1


# 二分探索
left = 0
right = L
mid: int
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
