"""基础干支工具。

P0 阶段只提供确定性的干支基础数据结构与时支计算；
完整的节气、日柱算法将在后续模块中加入，并通过测试固定边界行为。
"""

from dataclasses import dataclass
from datetime import datetime

STEMS = "甲乙丙丁戊己庚辛壬癸"
BRANCHES = "子丑寅卯辰巳午未申酉戌亥"


@dataclass(frozen=True)
class Pillar:
    stem: str
    branch: str

    @property
    def ganzhi(self) -> str:
        return self.stem + self.branch


def hour_branch(dt: datetime) -> str:
    """按传统两小时区间计算时支。

    子时为 23:00–00:59；随后每两个小时一个时辰。
    日界线如何影响日柱/子初换日由上层日柱算法单独处理。
    """
    hour = dt.hour
    if hour >= 23 or hour < 1:
        return "子"
    index = (hour + 1) // 2
    return BRANCHES[index]


def year_pillar_by_ganzhi_index(index: int) -> Pillar:
    """从 0..59 的六十甲子索引取得干支。"""
    if not 0 <= index < 60:
        raise ValueError("ganzhi index must be between 0 and 59")
    return Pillar(STEMS[index % 10], BRANCHES[index % 12])
