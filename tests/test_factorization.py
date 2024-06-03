from collections import Counter

from src.library.factorization import calculate_divisors, calculate_prime_factors, pollard_rho


def test_pollard_rho() -> None:
    """pollard_rhoのテスト"""
    # 素因数の1つを返す
    assert pollard_rho(12) == 2  # noqa: PLR2004
    # 素数の場合はその数を返す
    assert pollard_rho(13) == 13  # noqa: PLR2004
    # $F_6 = 2^64 + 1$の素因数の1つを返す
    assert pollard_rho(18_446_744_073_709_551_617) == 274_177  # noqa: PLR2004


def test_calculate_prime_factors() -> None:
    """calculate_prime_factorsのテスト"""
    assert calculate_prime_factors(12) == Counter({2: 2, 3: 1})
    assert calculate_prime_factors(13) == Counter({13: 1})
    assert calculate_prime_factors(18_446_744_073_709_551_617) == Counter({274_177: 1, 67_280_421_310_721: 1})


def test_calculate_divisors() -> None:
    """calculate_divisorsのテスト"""
    assert calculate_divisors(12) == [1, 2, 4, 3, 6, 12]  # 順序は昇順とは限らない
    assert calculate_divisors(13) == [1, 13]
    assert calculate_divisors(18_446_744_073_709_551_617) == [
        1,
        274_177,
        67_280_421_310_721,
        18_446_744_073_709_551_617,
    ]
