import datetime
from zoneinfo import ZoneInfo

local_tz = ZoneInfo("Asia/Seoul")


def tz_now():
    return datetime.datetime.now().astimezone(local_tz)


def get_ym_formats(months: int) -> list[tuple[int]]:
    res = []
    now = tz_now()
    this_year, this_month = now.year, now.month
    for _ in range(months):
        res.append((this_year, this_month))
        if this_month == 12:
            this_year += 1
            this_month = 1
        else:
            this_month += 1
    return res


def get_remain_days_of_month(year: int, month: int) -> int:
    """
    해당 연월의 남은 일수를 count
    """
    now = tz_now()
    if now.year > year or (now.year == year and now.month > month):
        return 0

    if month == 2:
        month_days = 29 if year % 4 == 0 else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        month_days = 31
    else:
        month_days = 30

    if now.year == year and now.month == month:
        return month_days - now.day + 1
    return month_days
