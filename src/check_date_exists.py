from src.is_year_leap import is_year_leap


def check_date_exists(day, month, year):
    if type(day) is not int or type(month) is not int or type(year) is not int:
        raise ValueError(str(day) + ' ' + str(month) + ' ' + str(year))

    day_in_month = {
        1: 31,
        2: 29 if is_year_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True

    return False
