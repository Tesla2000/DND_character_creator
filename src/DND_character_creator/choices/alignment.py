from __future__ import annotations

from enum import Enum


class Alignment(str, Enum):
    LAWFUL_GOOD = "lawful_good"
    TRUE_LAWFUL = "true_lawful"
    LAWFUL_EVIL = "lawful_evil"
    TRUE_GOOD = "ture_good"
    TRUE_NEUTRAL = "true_neutral"
    TRUE_EVIL = "true_evil"
    CHAOTIC_GOOD = "chaotic_good"
    TRUE_CHAOTIC = "true_chaotic"
    CHAOTIC_EVIL = "chaotic_evil"
