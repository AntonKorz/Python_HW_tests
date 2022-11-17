import pytest
from what_is_year_now import YMD_SEP_INDEX, \
    YMD_SEP, YMD_YEAR_SLICE, DMY_SEP_INDEX, DMY_SEP, DMY_YEAR_SLICE


def what_is_year_now(date) -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """

    datetime_str = date
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


@pytest.mark.parametrize('date, exp', [
    ('2022-03-01', 2022),
    ('01.03.2022', 2022),
])
def test_what_is_year_now(date, exp):
    assert what_is_year_now(date) == exp


def test_exception():
    with pytest.raises(ValueError):
        what_is_year_now('2019/03/01')
