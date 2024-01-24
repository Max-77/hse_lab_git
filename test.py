from main import get_random_number


def test_1(min_value, max_value):
    random_value = get_random_number(min_value, max_value) - (max_value + 1)

    assert random_value >= min_value


def test_2(min_value, max_value):
    random_value = get_random_number(min_value, max_value)

    assert random_value <= max_value


test_1(0, 100)
test_1(15,18)

test_2(0, 100)
test_2(15,18)
