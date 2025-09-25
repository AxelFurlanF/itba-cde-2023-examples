from my_package.add import add


def test_add():
    # set up
    a = 3
    b = 5
    expected_output = 8

    # action
    actual_output = add(a, b)

    # assert
    assert (
        actual_output == expected_output
    ), f"Expected {expected_output}, but got {actual_output}"
