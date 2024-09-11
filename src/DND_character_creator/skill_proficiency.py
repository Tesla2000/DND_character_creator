from __future__ import annotations

from enum import Enum

from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)


class SkillAndAny(str, Enum):
    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimidation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"
    ANY_OF_YOUR_CHOICE = "Any one of your choice"


class Skill(str, Enum):
    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimidation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"


skill2ability = {
    Skill.ACROBATICS: Statistic.DEXTERITY,
    Skill.ANIMAL_HANDLING: Statistic.WISDOM,
    Skill.ARCANA: Statistic.INTELLIGENCE,
    Skill.ATHLETICS: Statistic.STRENGTH,
    Skill.DECEPTION: Statistic.CHARISMA,
    Skill.HISTORY: Statistic.INTELLIGENCE,
    Skill.INSIGHT: Statistic.WISDOM,
    Skill.INTIMIDATION: Statistic.CHARISMA,
    Skill.INVESTIGATION: Statistic.INTELLIGENCE,
    Skill.MEDICINE: Statistic.WISDOM,
    Skill.NATURE: Statistic.INTELLIGENCE,
    Skill.PERCEPTION: Statistic.WISDOM,
    Skill.PERFORMANCE: Statistic.CHARISMA,
    Skill.PERSUASION: Statistic.CHARISMA,
    Skill.RELIGION: Statistic.INTELLIGENCE,
    Skill.SLEIGHT_OF_HAND: Statistic.DEXTERITY,
    Skill.STEALTH: Statistic.DEXTERITY,
    Skill.SURVIVAL: Statistic.WISDOM,
}
