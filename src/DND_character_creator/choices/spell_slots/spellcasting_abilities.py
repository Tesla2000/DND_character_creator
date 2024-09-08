from __future__ import annotations

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)

spellcasting_ability_map = {
    MainClass.BARD: Statistic.CHARISMA,
    MainClass.CLERIC: Statistic.WISDOM,
    MainClass.DRUID: Statistic.WISDOM,
    MainClass.FIGHTER: Statistic.INTELLIGENCE,  # For Eldritch Knight subclass
    MainClass.PALADIN: Statistic.CHARISMA,
    MainClass.RANGER: Statistic.WISDOM,
    MainClass.ROGUE: Statistic.INTELLIGENCE,  # For Arcane Trickster subclass
    MainClass.SORCERER: Statistic.CHARISMA,
    MainClass.WARLOCK: Statistic.CHARISMA,
    MainClass.WIZARD: Statistic.INTELLIGENCE,
    MainClass.ARTIFICER: Statistic.INTELLIGENCE,
}
