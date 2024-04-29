from typing import Self


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
