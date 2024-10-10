import timeit


def func1(lst: list):
    for i in range(len(lst)):
        if i not in lst:
            yield i


def func2(lst: list) -> list:
    res = []
    for i in range(len(lst)):
        if i not in lst:
            a.append(i)
    return res


def test1(lst: list) -> None:
    for i in range(len(lst)):
        if i not in lst:
            pass


def test2(lst: list) -> None:
    if set(range(len(lst))) <= set(lst):
        pass


def test3(lst: list) -> None:
    _ = [i for i in range(len(lst)) if i not in lst]


def func_test(func, lst: list) -> None:
    func(lst)


runs = 100000
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]


def format_time(seconds):
    return f"{seconds * 1000:.5f}ms"


print("Test 1 (conditional for loop with pass):", format_time(timeit.timeit(lambda: test1(a), number=runs) / runs))
print("Test 2 (set of range is subset of list):", format_time(timeit.timeit(lambda: test2(a), number=runs) / runs))
print("Test 3 (generator with  empty variable):", format_time(timeit.timeit(lambda: test3(a), number=runs) / runs))
print("Test 4 (function yielding missing data):", format_time(timeit.timeit(lambda: func_test(func1, a), number=runs) / runs))
print("Test 5 (function returning  list of MD):", format_time(timeit.timeit(lambda: func_test(func2, a), number=runs) / runs))

