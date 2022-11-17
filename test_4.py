from typing import List, Tuple
import pytest


# полный код в файле one_hot_encoder.py
def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


@pytest.mark.parametrize('s, exp', [
    (['Anton', 'Ivan', 'Anton'], [('Anton', [0, 1]), ('Ivan', [1, 0]), ('Anton', [0, 1])]),
    (['Anton', 'Anton', 'Anton', 'Anton'], [('Anton', [1]), ('Anton', [1]), ('Anton', [1]), ('Anton', [1])]),
    (['Anton', 'ANTON'], [('Anton', [0, 1]), ('ANTON', [1, 0])]),
    (['A', 'B', 'C', 'D', 'A'], [('A', [0, 0, 0, 1]), ('B', [0, 0, 1, 0]), ('C', [0, 1, 0, 0]), ('D', [1, 0, 0, 0]), ('A', [0, 0, 0, 1])])
])
def test_fit_transform(s, exp):
    assert fit_transform(s) == exp


print(fit_transform(['Anton', 'Ivan', 'Korznikov']))

