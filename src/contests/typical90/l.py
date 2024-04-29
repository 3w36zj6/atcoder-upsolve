from typing import Self

H, W = map(int, input().split())
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]


class UnionFind:
    """Union-Find (Disjoint Set Union)

    素集合データ構造を管理するクラス。
    """

    def __init__(self: Self, n: int) -> None:
        """データ構造を初期化する。

        Args:
            n (int):
                管理する要素の数
        """
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self: Self, a: int) -> int:
        """ある要素が属する集合の代表元を求める。

        Args:
            a (int):
                要素の番号

        Returns:
            int:
                aが属する集合の代表元
        """
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self: Self, a: int, b: int) -> None:
        """2つの要素が属する集合を併合する。

        Args:
            a (int):
                併合する集合の要素の番号
            b (int):
                併合する集合の要素の番号
        """
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def get_size(self: Self, a: int) -> int:
        """ある要素が属する集合の要素数を取得する。

        Args:
            a (int):
                要素の番号

        Returns:
            int:
                ある要素が属する集合の要素数
        """
        return self.size[self.find(a)]

    def __len__(self: Self) -> int:
        """管理している要素の数を取得する。

        Returns:
            int:
                管理している要素の数
        """
        return self.num_sets


union_find = UnionFind(H * W)

is_painted: list[bool] = [False] * (H * W)

for query in queries:
    if query[0] == 1:
        r, c = query[1], query[2]
        position_index = (r - 1) * W + c - 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            new_position_index = (new_r - 1) * W + new_c - 1
            if 1 <= new_r <= H and 1 <= new_c <= W and is_painted[new_position_index]:
                union_find.union(position_index, new_position_index)
        is_painted[position_index] = True
    else:
        ra, ca, rb, cb = query[1], query[2], query[3], query[4]
        a_position_index = (ra - 1) * W + ca - 1
        b_position_index = (rb - 1) * W + cb - 1

        if (
            is_painted[a_position_index]
            and is_painted[b_position_index]
            and union_find.find(a_position_index) == union_find.find(b_position_index)
        ):
            print("Yes")
        else:
            print("No")
