from src.library.dijkstra import dijkstra


def test_dijkstra() -> None:
    """dijkstraのテスト"""
    graph: list[list[tuple[int, float | int]]] = [[(2, 1)], [(0, 1)], [], [(4, 1)], [(3, 1)]]
    dist, parents = dijkstra(graph, 0)
    assert dist == [0, float("inf"), 1, float("inf"), float("inf")]
    assert parents == [None, None, 0, None, None]
