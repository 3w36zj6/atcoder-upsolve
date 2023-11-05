from collections.abc import Sequence


def dfs(graph: Sequence[Sequence[int]], start: int = 0) -> tuple[list[bool], list[int]]:
    """深さ優先探索(Depth-first search)

    重みなし有向グラフの全ての頂点をO(V+E)で探索する。

    Args:
        graph (Sequence[Sequence[int]]):
            各頂点から到達可能な頂点のリスト [[頂点0から到達可能な頂点, ...], ...]
        start (int, optional):
            探索を開始する頂点の番号 デフォルトは0

    Returns:
        list[bool]:
            各頂点を訪問したかどうかのリスト [頂点0を訪問したかどうか, ...]
        list[int]]:
            各頂点を根とする部分木の頂点数のリスト [頂点0を根とする部分木の頂点数, ...]

    Examples:
        >>> graph = [[1, 2], [0], [0], [4], [3]]
        >>> visited, dp = dfs(graph, 0)
        >>> visited
        [True, True, True, False, False]
        >>> dp
        [3, 1, 1, 0, 0]
    """
    n = len(graph)

    dp: list[int] = [0] * n
    visited: list[bool] = [False] * n
    finished: list[bool] = [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)  # noqa: PERF401
        else:
            stack.pop()

            dp[start] += 1

            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return visited, dp
