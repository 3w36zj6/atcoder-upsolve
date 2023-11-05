from src.library.dfs import dfs


def test_dfs() -> None:
    """dfsのテスト"""
    graph: list[list[int]] = [[1, 2], [0], [0], [4], [3]]
    visited, dp = dfs(graph, 0)
    assert visited == [True, True, True, False, False]
    assert dp == [3, 1, 1, 0, 0]
