from datetime import datetime

from src.calendar.ganzhi import BRANCHES, STEMS, Pillar, hour_branch, year_pillar_by_ganzhi_index


def test_stems_and_branches_lengths():
    assert len(STEMS) == 10
    assert len(BRANCHES) == 12


def test_ganzhi_index_zero():
    assert year_pillar_by_ganzhi_index(0) == Pillar("甲", "子")


def test_ganzhi_index_59():
    assert year_pillar_by_ganzhi_index(59) == Pillar("癸", "亥")


def test_hour_branch_boundaries():
    assert hour_branch(datetime(2026, 1, 1, 22, 59)) == "亥"
    assert hour_branch(datetime(2026, 1, 1, 23, 0)) == "子"
    assert hour_branch(datetime(2026, 1, 2, 0, 59)) == "子"
    assert hour_branch(datetime(2026, 1, 2, 1, 0)) == "丑"
    assert hour_branch(datetime(2026, 1, 2, 22, 59)) == "亥"


def test_pillar_string():
    assert Pillar("甲", "子").ganzhi == "甲子"
