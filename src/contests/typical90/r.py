import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]


def get_position(t: int) -> tuple[float, float, float]:
    """時刻tのときの座標を返す"""
    theta = 2 * math.pi * t / T
    y = -L / 2 * math.sin(theta)
    z = L / 2 - L / 2 * math.cos(theta)
    return (0, y, z)


for t in E:
    x, y, z = get_position(t)
    r = math.sqrt((X - x) ** 2 + (Y - y) ** 2 + z**2)
    print(math.degrees(math.asin(z / r)))
