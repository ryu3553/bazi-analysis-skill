"""命令行测试入口。

用法:
  python -m src.calendar.cli 1990-05-15 10:30
"""

import argparse
from datetime import datetime

from .solar import calculate_solar_datetime


def main() -> None:
    parser = argparse.ArgumentParser(description="八字四柱测试计算器")
    parser.add_argument("date", help="公历日期，例如 1990-05-15")
    parser.add_argument("time", help="当地时间，例如 10:30")
    args = parser.parse_args()

    dt = datetime.strptime(f"{args.date} {args.time}", "%Y-%m-%d %H:%M")
    result = calculate_solar_datetime(dt)

    print(f"出生时间：{result['input']['date']} {result['input']['time']}")
    print(f"年柱：{result['pillars']['year']}")
    print(f"月柱：{result['pillars']['month']}")
    print(f"日柱：{result['pillars']['day']}")
    print(f"时柱：{result['pillars']['hour']}")
    print(f"说明：{result['note']}")


if __name__ == "__main__":
    main()
