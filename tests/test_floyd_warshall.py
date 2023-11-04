from src.library.floyd_warshall import floyd_warshall


def test_floyd_warshall() -> None:
    """floyd_warshallのテスト"""
    n = 4
    edges = [(0, 1, 1), (0, 2, 5), (1, 2, 2), (1, 3, 4), (2, 3, 1)]
    dist, pred = floyd_warshall(n, edges)
    assert dist == [
        [0, 1, 3, 4],
        [float("inf"), 0, 2, 3],
        [float("inf"), float("inf"), 0, 1],
        [float("inf"), float("inf"), float("inf"), 0],
    ]
    assert pred == [[None, 0, 1, 2], [None, None, 1, 2], [None, None, None, 2], [None, None, None, None]]
