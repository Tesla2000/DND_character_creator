from __future__ import annotations

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)

class2hit_die = {
    MainClass.BARBARIAN: 12,
    MainClass.BARD: 8,
    MainClass.CLERIC: 8,
    MainClass.DRUID: 8,
    MainClass.FIGHTER: 10,
    MainClass.MONK: 8,
    MainClass.PALADIN: 10,
    MainClass.RANGER: 10,
    MainClass.ROGUE: 8,
    MainClass.SORCERER: 6,
    MainClass.WARLOCK: 8,
    MainClass.WIZARD: 6,
    MainClass.ARTIFICER: 8,
}
