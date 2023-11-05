from collections.abc import Sequence
from heapq import heappop, heappush

N = int(input())

graph: list[list[tuple[int, int]]] = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))


def dijkstra(
    graph: Sequence[Sequence[tuple[int, float | int]]],
    start: int = 0,
) -> tuple[list[float | int], list[int | None]]:
    """ダイクストラ(Dijkstra)法

    重み付き有向グラフの全ての頂点への最短距離をO(ElogV)で求める。

    Args:
        graph (Sequence[Sequence[tuple[int, float | int]]]):
            各頂点から到達可能な頂点と辺の重みのリスト [[(頂点0から到達可能な頂点, 辺の重み), ...], ...]
        start (int, optional):
            探索を開始する頂点の番号 デフォルトは0

    Returns:
        list[float | int]:
            各頂点への最短距離のリスト [頂点0への最短距離, ...]
        list[int | None]:
            各頂点への最短経路における直前の頂点のリスト [頂点0の直前の頂点, ...]

    Examples:
        >>> graph = [[(2, 1)], [(0, 1)], [], [(4, 1)], [(3, 1)]]
        >>> dist, parents = dijkstra(graph, 0)
        >>> dist
        [0, inf, 1, inf, inf]
        >>> parents
        [None, None, 0, None, None]
    """
    n = len(graph)
    dist: list[float | int] = [float("inf")] * n
    parents: list[int | None] = [None] * n
    dist[start] = 0

    queue: list[tuple[float | int, int]] = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


dist, parents = dijkstra(graph)

for i in range(N):
    print(dist[i] % 2)
