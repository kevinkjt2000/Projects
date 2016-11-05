def int_to_digits(x):
    def _int_to_digits(x):
        while x > 9:
            yield x % 10
            x //= 10
        yield x
    return list(reversed(list(_int_to_digits(x))))


def test_int_to_digits():
    assert int_to_digits(1) == [1]
    assert int_to_digits(10) == [1, 0]
    assert int_to_digits(12345) == [1, 2, 3, 4, 5]


def is_happy_number(x):
    encountered = set([x])

    while x is not 1:
        digits = int_to_digits(x)
        x = sum(map(lambda a: a ** 2, digits))
        if x in encountered:
            return False
        encountered.add(x)
    return True


def test_happy_numbers():
    assert is_happy_number(1)
    assert not is_happy_number(2)
    assert not is_happy_number(3)
    assert not is_happy_number(4)
    assert not is_happy_number(5)
    assert not is_happy_number(6)
    assert is_happy_number(7)
    assert not is_happy_number(8)
    assert is_happy_number(10)
    assert is_happy_number(13)
    assert not is_happy_number(14)
    assert is_happy_number(998)


def first_n_happy_numbers(n):
    x = 1
    while n > 0:
        while not is_happy_number(x):
            x += 1
        yield x
        x += 1
        n -= 1


def test_lots_of_happiness():
    assert all(first_n_happy_numbers(1000))


if __name__ == '__main__':
    print(list(first_n_happy_numbers(8)))

