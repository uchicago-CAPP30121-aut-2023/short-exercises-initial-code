import sys
import os

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se1

MODULE = "se1"

def test_add_one_and_multiply_1():
    do_test_add_one_and_multiply(a=0, x=0, expected=0)


def test_add_one_and_multiply_2():
    do_test_add_one_and_multiply(a=5, x=2, expected=12)


def test_add_one_and_multiply_3():
    do_test_add_one_and_multiply(a=5, x=0, expected=0)


def test_add_one_and_multiply_4():
    do_test_add_one_and_multiply(a=9, x=1, expected=10)


def test_add_one_and_multiply_5():
    do_test_add_one_and_multiply(a=9, x=-2, expected=-20)


def test_add_one_and_multiply_6():
    do_test_add_one_and_multiply(a=-11, x=2, expected=-20)


def test_same_parity_1():
    do_test_same_parity(a=0, b=0, expected=True)


def test_same_parity_2():
    do_test_same_parity(a=1, b=1, expected=True)


def test_same_parity_3():
    do_test_same_parity(a=1, b=3, expected=True)


def test_same_parity_4():
    do_test_same_parity(a=8, b=1002, expected=True)


def test_same_parity_5():
    do_test_same_parity(a=2021, b=55, expected=True)


def test_same_parity_6():
    do_test_same_parity(a=0, b=1, expected=False)


def test_same_parity_7():
    do_test_same_parity(a=1, b=0, expected=False)


def test_same_parity_8():
    do_test_same_parity(a=8, b=11, expected=False)


def test_same_parity_9():
    do_test_same_parity(a=11, b=8, expected=False)


def test_same_parity_10():
    do_test_same_parity(a=1001, b=56, expected=False)


def test_same_parity_11():
    do_test_same_parity(a=27, b=1888, expected=False)


def test_num_to_string_1():
    do_test_num_to_string(x=0, expected="ZERO")


def test_num_to_string_2():
    do_test_num_to_string(x=1, expected="POSITIVE")


def test_num_to_string_3():
    do_test_num_to_string(x=2055, expected="POSITIVE")


def test_num_to_string_4():
    do_test_num_to_string(x=-1, expected="NEGATIVE")


def test_num_to_string_5():
    do_test_num_to_string(x=-1000, expected="NEGATIVE")


def test_num_divisible_1():
    do_test_num_divisible(lb=1, ub=10, p=2, q=3, expected=6)


def test_num_divisible_2():
    do_test_num_divisible(lb=1, ub=10, p=1, q=5, expected=8)


def test_num_divisible_3():
    do_test_num_divisible(lb=1, ub=10, p=10, q=15, expected=1)


def test_num_divisible_4():
    do_test_num_divisible(lb=1, ub=10, p=15, q=16, expected=0)


def test_num_divisible_5():
    do_test_num_divisible(lb=1, ub=100, p=10, q=50, expected=8)


def test_num_divisible_6():
    do_test_num_divisible(lb=5, ub=20, p=2, q=3, expected=7)


def test_num_greater_than_1():
    do_test_num_greater_than(lst=[1, 2, 3, 4, 5], t=3, expected=2)


def test_num_greater_than_2():
    do_test_num_greater_than(lst=[6, 1, 4, 5, 3, 2, 3], t=3, expected=3)


def test_num_greater_than_3():
    do_test_num_greater_than(lst=[6, 1, 4, 5, 3, 3, 2], t=2, expected=5)


def test_num_greater_than_4():
    do_test_num_greater_than(lst=[1, 2, 3, 4, 5], t=0, expected=5)


def test_num_greater_than_5():
    do_test_num_greater_than(lst=[1, 2, 3, 4, 5], t=6, expected=0)


def test_num_greater_than_6():
    do_test_num_greater_than(lst=[], t=6, expected=0)


def test_keep_if_in_range_1():
    do_test_keep_if_in_range(lst=[1, 2, 3, 4, 5, 6], lb=2, ub=4, expected=[2, 3, 4])


def test_keep_if_in_range_2():
    do_test_keep_if_in_range(lst=[1, 2, 3, 4, 5, 6], lb=0, ub=7, expected=[1, 2, 3, 4, 5, 6])


def test_keep_if_in_range_3():
    do_test_keep_if_in_range(lst=[1, 2, 3, 4, 5, 6], lb=8, ub=10, expected=[])


def test_keep_if_in_range_4():
    do_test_keep_if_in_range(lst=[1, 2, 3, 4, 5, 6], lb=4, ub=4, expected=[4])


def test_keep_if_in_range_5():
    do_test_keep_if_in_range(lst=[1, 2, 3, 4, 5, 6], lb=0, ub=7, expected=[1, 2, 3, 4, 5, 6])


def test_keep_if_in_range_6():
    do_test_keep_if_in_range(lst=[6, 1, 4, 5, 3, 2, 3], lb=3, ub=5, expected=[4, 5, 3, 3])


# # #
#
# HELPER FUNCTIONS
#
# # #

def gen_recreate_msg(module, function, *params):
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg


def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg


def check_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_float_equals(actual, expected, epsilon, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert abs(actual - expected) < epsilon, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    msg = "You modified the contents of {} (this is not allowed).\n".format(param_name)
    msg += "  Value before your code: {}\n".format(before)
    msg += "  Value after your code:  {}".format(after)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg


# # #
#
# TEST HELPERS
#
# # #


def do_test_add_one_and_multiply(a, x, expected):
    recreate_msg = gen_recreate_msg(MODULE, "add_one_and_multiply", *(a, x))

    actual = se1.add_one_and_multiply(a, x)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_same_parity(a, b, expected):
    recreate_msg = gen_recreate_msg(MODULE, "same_parity", *(a, b))

    actual = se1.same_parity(a, b)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_num_to_string(x, expected):
    recreate_msg = gen_recreate_msg(MODULE, "num_to_string", *(x,))

    actual = se1.num_to_string(x)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_num_divisible(lb, ub, p, q, expected):
    recreate_msg = gen_recreate_msg(MODULE, "num_divisible", *(lb, ub, p, q))

    actual = se1.num_divisible(lb, ub, p, q)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_num_greater_than(lst, t, expected):
    recreate_msg = gen_recreate_msg(MODULE, "num_greater_than", *(lst, t))

    orig = lst[:]
    actual = se1.num_greater_than(lst, t)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_list_unmodified("lst", orig, lst, recreate_msg)


def do_test_keep_if_in_range(lst, lb, ub, expected):
    recreate_msg = gen_recreate_msg(MODULE, "keep_if_in_range", *(lst, lb, ub))

    orig = lst[:]
    actual = se1.keep_if_in_range(lst, lb, ub)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_list_unmodified("lst", orig, lst, recreate_msg)