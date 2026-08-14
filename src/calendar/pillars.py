"""四柱计算入口（P0）。

当前阶段只实现可验证的时支，并明确拒绝猜测缺失的年/月/日柱。
完整四柱算法会在节气与日柱模块完成后接入。
"""

from datetime import datetime

from .ganzhi import hour_branch


def calculate_pillars(dt: datetime) -> dict[str, dict[str, str]]:
    """返回当前已实现的四柱计算结果。

    P0 不会伪造尚未实现的年、月、日柱，因此这些字段明确标记为未实现。
    """
    return {
        "year": {"stem": "", "branch": "", "status": "not_implemented"},
        "month": {"stem": "", "branch": "", "status": "requires_jieqi"},
        "day": {"stem": "", "branch": "", "status": "requires_day_ganzhi"},
        "hour": {"stem": "", "branch": hour_branch(dt), "status": "implemented_branch_only"},
    }
