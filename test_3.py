from typing import List, Tuple
import unittest


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


class TestTF(unittest.TestCase):
    def test_1(self):
        actual = fit_transform(['Anton', 'Ivan', 'Anton'])
        expected = [('Anton', [0, 1]), ('Ivan', [1, 0]), ('Anton', [0, 1])]
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = fit_transform(['Anton', 'Anton', 'Anton', 'Anton'])
        expected = [('Anton', [1]), ('Anton', [1]), ('Anton', [1]), ('Anton', [1])]
        self.assertEqual(actual, expected)

    def test_3(self):
        actual = fit_transform(['Anton', 'ANTON'])
        expected = [('Anton', [0, 1]), ('ANTON', [1, 0])]
        self.assertEqual(actual, expected)

    def test_4(self):
        actual = fit_transform(['A', 'B', 'C', 'D', 'A'])
        expected = [('A', [0, 0, 0, 1]), ('B', [0, 0, 1, 0]), ('C', [0, 1, 0, 0]), ('D', [1, 0, 0, 0]), ('A', [0, 0, 0, 1])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_not_in(self):
        actual = fit_transform(['Anton', 'Ivan', 'Korznikov'])
        expected = ('Ivan', [0, 1, 0])
        self.assertNotIn(actual, expected)

if __name__ == '__main__':
    unittest.main()
