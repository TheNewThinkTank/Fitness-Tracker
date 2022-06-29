"""Convert month names from strings to integer representations
"""

from enum import Enum, unique


@unique
class Months(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


def get_year_and_month(date="2022-06-27"):
    """_summary_"""
    month_zeropadded = date[5:7]
    month = int(month_zeropadded.removeprefix("0"))
    MONTH = Months(month).name.capitalize()
    YEAR = date[:4]
    return YEAR, MONTH


if __name__ == "__main__":
    print(get_year_and_month())
