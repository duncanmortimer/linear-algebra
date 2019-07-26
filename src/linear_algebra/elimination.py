import numpy as np


def find_pivot(A):
    def pivot_iter(a, non_zero_p=lambda x: np.abs(x) > 1e-9):
        level = 0
        for j, col in enumerate(a.T):
            is_pivot_column = np.any(non_zero_p(col[level + 1 :]))
            entry_at_level_is_nonzero = non_zero_p(col[level])
            if is_pivot_column:
                if entry_at_level_is_nonzero:
                    yield (level, j), None
                else:
                    non_zero_i = level + np.argmax(non_zero_p(col[level + 1 :])) + 1
                    yield None, (level, non_zero_i)

            if entry_at_level_is_nonzero:
                level += 1

    a = np.array(A)
    try:
        pivot, permutation = next(pivot_iter(a))
        return pivot, permutation
    except StopIteration:
        return None, None


def START():
    return ("START",)

def DONE():
    return ("DONE",)


def E(location, coefficient):
    return ("E", location, coefficient)


def P(r1, r2):
    return ("P", r1, r2)


def elimination_step(A):
    """Returns the next step in Gaussian elimination of the matrix A"""
    a = np.array(A)
    result = find_pivot(a)

    pivot, permutation = result
    if permutation:
        return P(*permutation)

    if pivot:
        i, j = pivot
        pivot_col = a[:, j]
        first_nonzero_i = i + 1 + np.argmax(np.abs(pivot_col[i + 1 :]))
        coefficient = -a[first_nonzero_i, j] / a[i, j]
        return E((first_nonzero_i, i), coefficient)

    return DONE()


def transform(A, step):
    a = np.array(A)
    m, _ = a.shape
    instruction, *args = step
    if instruction == "DONE":
        t = np.eye(m)
    if instruction == "E":
        i, j = args[0]
        c = args[1]
        t = np.eye(m)
        t[i, j] = c
    if instruction == "P":
        r1, r2 = args
        t = np.eye(m)
        t[r1, :] = np.eye(m)[r2, :]
        t[r2, :] = np.eye(m)[r1, :]
    return np.dot(t, a)


def do_elimination(A):
    step = None
    a = np.array(A)
    yield START(), a
    while step != DONE():
        step = elimination_step(a)
        a = transform(a, step)
        yield step, a