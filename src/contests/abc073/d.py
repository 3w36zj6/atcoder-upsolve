import itertools
import sys
from collections.abc import Sequence

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
ABC: list[tuple[int, int, int]] = []

for _ in range(M):
    a, b, c = map(int, input().split())
    ABC.append((a, b, c))


def floyd_warshall(
    n: int,
    edges: Sequence[tuple[int, int, float | int]],
) -> tuple[list[list[float | int]], list[list[int | None]]]:
    """ワーシャルフロイド(Floyd-Warshall)法

    重み付き有向グラフの全ての頂点間の最短距離をO(V^3)で求める。

    Args:
        n (int):
            頂点数
        edges (Sequence[tuple[int, int, float | int]]):
            辺のリスト [(始点, 終点, 辺の重み), ...]

    Returns:
        list[list[float | int]]:
            各頂点間の最短距離のリスト [[頂点0から頂点0への最短距離, ..., 頂点0から頂点n-1への最短距離], ...]
        list[list[int | None]]]:
            各頂点間の最短距離の終点の親の頂点のリスト [[頂点0から頂点0への最短距離の終点の親の頂点, ..., 頂点0から頂点n-1への最短距離の終点の親の頂点], ...]

    Examples:
        >>> n = 4
        >>> edges = [(0, 1, 1), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 3, 1)]
        >>> dist, pred = floyd_warshall(n, edges)
        >>> dist
        [[0, 1, 3, 4], [inf, 0, 2, 3], [inf, inf, 0, 1], [inf, inf, inf, 0]]
        >>> pred
        [[None, 0, 1, 2], [None, None, 1, 2], [None, None, None, 2], [None, None, None, None]]
    """
    dist: list[list[float | int]] = [[0 if i == j else float("inf") for i in range(n)] for j in range(n)]
    pred: list[list[int | None]] = [[None] * n for _ in range(n)]

    for u, v, d in edges:
        dist[u][v] = d
        pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


edges: list[tuple[int, int, int]] = []

for a, b, c in ABC:
    edges.append((a - 1, b - 1, c))
    edges.append((b - 1, a - 1, c))

dist, pred = floyd_warshall(N, edges)

print(dist, file=sys.stderr)


candidate_routes = itertools.permutations(r, R)

ans: float | int = float("inf")
for candidate_route in candidate_routes:
    candidate_ans: float | int = 0
    print(candidate_route, file=sys.stderr)
    for i in range(R - 1):
        candidate_ans += dist[candidate_route[i] - 1][candidate_route[i + 1] - 1]
    print(candidate_ans, file=sys.stderr)
    ans = min(ans, candidate_ans)

print(ans)
