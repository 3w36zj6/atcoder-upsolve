from src.library.union_find import UnionFind


def test_union_find() -> None:
    """Union-Findのテスト"""
    # https://atcoder.jp/contests/atc001/tasks/unionfind_a
    queries = [[0, 1, 2], [0, 3, 2], [1, 1, 3], [1, 1, 4], [0, 2, 4], [1, 4, 1], [0, 4, 2], [0, 0, 0], [1, 0, 0]]
    union_find = UnionFind(8)
    pred_answers = [True, False, True, True]
    for p, a, b in queries:
        if p == 0:
            union_find.union(a, b)
        else:
            assert (union_find.find(a) == union_find.find(b)) == pred_answers.pop(0)
