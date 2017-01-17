def prime_factors(x):
    if x > 3:
        factors = []
        divisor = 2
        while divisor <= x:
            if x % divisor == 0:
                x /= divisor
                factors.append(divisor)
            else:
                divisor += 1
        return factors
    return [x]


def test_one_factor():
    assert prime_factors(1) == [1]
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(5) == [5]


def test_two_factors():
    assert prime_factors(4) == [2, 2]
    assert prime_factors(6) == [2, 3]


def test_big_numbers():
    assert prime_factors(12345) == [3, 5, 823]
    assert prime_factors(123456789) == [3, 3, 3607, 3803]
