from itertools import product

N = int(input())


def check(string: str) -> bool:
    """文字列の括弧の対応が取れているかを判定する"""
    depth = 0
    for char in string:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

        if depth < 0:
            return False

    return depth == 0


for string in product(["(", ")"], repeat=N):
    joined_string = "".join(string)
    if check(joined_string):
        print(joined_string)
