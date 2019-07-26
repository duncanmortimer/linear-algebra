import pytest
from hamcrest import contains, assert_that, close_to, is_

from .elimination import find_pivot, elimination_step, DONE, P, E


@pytest.mark.parametrize(
    "matrix, expected_pivot, expected_permutation",
    [
        ([[1, 0], [0, 1]], None, None),
        ([[1, 0], [1, 1]], (0, 0), None),
        ([[0, 1], [1, 0]], None, (0, 1)),
        ([[1, 0], [2, 1]], (0, 0), None),
        ([[1, 1, 2], [0, 1, 1], [0, 1, 0]], (1, 1), None),
        ([[1, 1, 2], [0, 0, 1], [0, 1, 0]], None, (1, 2)),
        ([[1, 1, 2], [0, 1, 1], [0, 0, 1]], None, None),
        ([[1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], (1, 2), None),
    ],
)
def test_find_pivot(matrix, expected_pivot, expected_permutation):
    assert_that(find_pivot(matrix), contains(expected_pivot, expected_permutation))


def matches_DONE():
    return DONE()


def matches_E(location, coefficient):
    return contains(*E(location, close_to(coefficient, 1e-9)))


def matches_P(r1, r2):
    return P(r1, r2)


@pytest.mark.parametrize(
    "matrix, expected_step",
    [
        ([[1, 0], [0, 1]], matches_DONE()),
        ([[1, 0], [1, 1]], matches_E((1, 0), -1)),
        ([[1, 0], [2, 1]], matches_E((1, 0), -2)),
        ([[1, 1, 2], [0, 1, 1], [0, 1, 1]], matches_E((2, 1), -1)),
        ([[1, 1, 2], [5, 1, 1], [0, 1, 1]], matches_E((1, 0), -5)),
        ([[0, 1], [1, 0]], matches_P(0, 1)),
        ([[1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], matches_E((2, 2), -1)),
    ],
)
def test_elimination_step(matrix, expected_step):
    assert_that(elimination_step(matrix), is_(expected_step))
