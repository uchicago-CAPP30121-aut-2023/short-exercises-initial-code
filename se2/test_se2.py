import sys
import os
import copy

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se2

MODULE = "se2"

def test_eisenstein_triple_1():
    do_test_eisenstein_triple(a=3, b=8, c=7, expected=True)


def test_eisenstein_triple_2():
    do_test_eisenstein_triple(a=5, b=8, c=7, expected=True)


def test_eisenstein_triple_3():
    do_test_eisenstein_triple(a=5, b=21, c=19, expected=True)


def test_eisenstein_triple_4():
    do_test_eisenstein_triple(a=3, b=9, c=7, expected=False)


def test_eisenstein_triple_5():
    do_test_eisenstein_triple(a=4, b=8, c=7, expected=False)


def test_eisenstein_triple_6():
    do_test_eisenstein_triple(a=3, b=8, c=6, expected=False)


def test_first_negative_1():
    lst = [-1]
    do_test_first_negative(lst=lst, expected=-1)


def test_first_negative_2():
    lst = [-1, 0]
    do_test_first_negative(lst=lst, expected=-1)


def test_first_negative_3():
    lst = [0, -1]
    do_test_first_negative(lst=lst, expected=-1)


def test_first_negative_4():
    lst = [0, -1, -3]
    do_test_first_negative(lst=lst, expected=-1)


def test_first_negative_5():
    lst = [0, 1, -3, 2]
    do_test_first_negative(lst=lst, expected=-3)


def test_first_negative_6():
    lst = [0, 1, 3, 2, 4, -5]
    do_test_first_negative(lst=lst, expected=-5)


def test_first_negative_7():
    lst = [0, 1, 3, 2, 4, 5]
    do_test_first_negative(lst=lst, expected=0)


def test_first_negative_8():
    lst = []
    do_test_first_negative(lst=lst, expected=0)


def test_clip_in_range_1():
    do_test_clip_in_range(lst=[], lb=0, ub=2, expected=[])


def test_clip_in_range_2():
    do_test_clip_in_range(lst=[1], lb=0, ub=2, expected=[1])


def test_clip_in_range_3():
    do_test_clip_in_range(lst=[0, 1, 2], lb=0, ub=2, expected=[0, 1, 2])


def test_clip_in_range_4():
    do_test_clip_in_range(lst=[1, 4, 4, 3, -3], lb=-2, ub=5, expected=[1, 4, 4, 3, -2])


def test_clip_in_range_5():
    do_test_clip_in_range(lst=[-1, 9, 0, 3, 3, 7], lb=-2, ub=5, expected=[-1, 5, 0, 3, 3, 5])


def test_clip_in_range_6():
    do_test_clip_in_range(lst=[0, -1, 2, 4, -5, 7, 1], lb=0, ub=2, expected=[0, 0, 2, 2, 0, 2, 1])


def test_expand_1():
    do_test_expand(a=0, b=1, expected=[0, 1])


def test_expand_2():
    do_test_expand(a=1, b=2, expected=[1, 2])


def test_expand_3():
    do_test_expand(a=0, b=2, expected=[0, 1, 2])


def test_expand_4():
    do_test_expand(a=0, b=6, expected=[0, 1, 2, 3, 4, 5, 6])


def test_expand_5():
    do_test_expand(a=4, b=9, expected=[4, 5, 6, 7, 8, 9])


def test_expand_6():
    do_test_expand(a=12, b=25, expected=[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])


def test_same_length_1():
    lst_of_lsts = [[1], [2], [3]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=True)


def test_same_length_2():
    lst_of_lsts = [[1, 1], [2, 2], [3, 3]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=True)


def test_same_length_3():
    lst_of_lsts = [[], []]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=True)


def test_same_length_4():
    lst_of_lsts = [[1, 1], [2, 2], [3]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=False)


def test_same_length_5():
    lst_of_lsts = [[1, 1], [2, 2, 2, 3], [3, 3]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=False)


def test_same_length_6():
    lst_of_lsts = [[1, 1, 1], [2, 2], [3, 3]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=False)


def test_same_length_7():
    lst_of_lsts = [[1, 1], [2, 2], [3, 3], [4]]
    do_test_same_length(lst_of_lsts=lst_of_lsts, expected=False)


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
    msg += " Did you forget to clip_in_range the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg


def check_expected_none(actual, recreate_msg=None):
    msg = "The function is expected to return None."
    msg += " Your function returns: {}".format(actual)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg


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


def do_test_eisenstein_triple(a, b, c, expected):
    recreate_msg = gen_recreate_msg(MODULE, "eisenstein_triple", *(a, b, c))

    actual = se2.eisenstein_triple(a, b, c)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_first_negative(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "first_negative", *(lst,))

    orig = lst[:]
    actual = se2.first_negative(lst)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_list_unmodified("lst", orig, lst, recreate_msg)


def do_test_expand(a, b, expected):
    recreate_msg = gen_recreate_msg(MODULE, "expand", *(a, b))

    actual = se2.expand(a, b)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_clip_in_range(lst, lb, ub, expected):
    recreate_msg = gen_recreate_msg(MODULE, "clip_in_range", *(lst, lb, ub))

    lst_copy = lst[:]
    actual = se2.clip_in_range(lst_copy, lb, ub)

    check_expected_none(actual, recreate_msg)
    check_equals(lst_copy, expected, recreate_msg)


def do_test_same_length(lst_of_lsts, expected):
    recreate_msg = gen_recreate_msg(MODULE, "same_length", *(lst_of_lsts,))

    orig = copy.deepcopy(lst_of_lsts)
    actual = se2.same_length(lst_of_lsts)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
    check_list_unmodified("lst_of_lsts", orig, lst_of_lsts, recreate_msg)