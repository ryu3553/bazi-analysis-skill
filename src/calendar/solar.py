"""公历出生时间 -> 四柱。

计算依赖 sxtwl 进行历法/节气相关计算，避免在 Skill 中凭模型记忆猜测日柱。
时间默认解释为用户提供的当地民用时间；精确地方时修正暂不自动处理。
"""

from datetime import datetime

import sxtwl

STEMS = "甲乙丙丁戊己庚辛壬癸"
BRANCHES = "子丑寅卯辰巳午未申酉戌亥"


def _gz(gz) -> str:
    return STEMS[gz.getGan()] + BRANCHES[gz.getZhi()]


def calculate_solar_datetime(dt: datetime) -> dict:
    if not 1900 <= dt.year <= 2100:
        raise ValueError("P0 calculator currently supports years 1900-2100")

    day = sxtwl.fromSolar(dt.year, dt.month, dt.day)
    year_gz = day.getYearGZ()
    month_gz = day.getMonthGZ()
    day_gz = day.getDayGZ()
    hour_gz = day.getHourGZ(dt.hour)

    return {
        "input": {
            "date": dt.strftime("%Y-%m-%d"),
            "time": dt.strftime("%H:%M"),
            "calendar": "solar",
        },
        "pillars": {
            "year": _gz(year_gz),
            "month": _gz(month_gz),
            "day": _gz(day_gz),
            "hour": _gz(hour_gz),
        },
        "note": "Calculated by sxtwl; local civil time is used and true-solar-time correction is not applied.",
    }
