def season_1(month):
    return {
        month in (1, 2, 12): 'winter',
        month in (3, 4, 5): 'spring',
        month in (6, 7, 8): 'summer',
        month in (9, 10, 11): 'autumn',
        month not in range(1, 13): 'not correct month'
    }[True]


def season_2(month):
    if month in (1, 2, 12):
        return 'winter'
    elif month in (3, 4, 5):
        return 'spring'
    elif month in (6, 7, 8):
        return 'summer'
    elif month in (9, 10, 11):
        return 'autumn'
    else:
        raise ValueError('not correct month')
