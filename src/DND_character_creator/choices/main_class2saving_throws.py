from __future__ import annotations

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)

main_class2saving_throws = {
    MainClass.BARBARIAN: {Statistic.STRENGTH, Statistic.CONSTITUTION},
    MainClass.BARD: {Statistic.DEXTERITY, Statistic.CHARISMA},
    MainClass.CLERIC: {Statistic.WISDOM, Statistic.CHARISMA},
    MainClass.DRUID: {Statistic.INTELLIGENCE, Statistic.WISDOM},
    MainClass.FIGHTER: {Statistic.STRENGTH, Statistic.CONSTITUTION},
    MainClass.MONK: {Statistic.STRENGTH, Statistic.DEXTERITY},
    MainClass.PALADIN: {Statistic.WISDOM, Statistic.CHARISMA},
    MainClass.RANGER: {Statistic.STRENGTH, Statistic.DEXTERITY},
    MainClass.ROGUE: {Statistic.DEXTERITY, Statistic.INTELLIGENCE},
    MainClass.SORCERER: {Statistic.CONSTITUTION, Statistic.CHARISMA},
    MainClass.WARLOCK: {Statistic.WISDOM, Statistic.CHARISMA},
    MainClass.WIZARD: {Statistic.INTELLIGENCE, Statistic.WISDOM},
    MainClass.ARTIFICER: {Statistic.CONSTITUTION, Statistic.INTELLIGENCE},
}
