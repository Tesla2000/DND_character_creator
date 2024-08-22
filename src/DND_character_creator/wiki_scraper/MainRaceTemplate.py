from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.language import Language
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.skill_proficiency import SkillProficiency


class SubRaceTemplate(BaseModel):
    name: str
    speed: int
    darkvision_range: int
    languages: list[Optional[Language]] = Field(
        description="List of languages known by this race None if language can"
        " be chosen marked as 'other language of your choice'"
    )
    obligatory_skill_proficiencies: list[SkillProficiency] = Field(
        description="List of skill proficiencies that are provided by default"
    )
    additional_skill_proficiencies: list[SkillProficiency] = Field(
        description="List of skill proficiencies that can be chosen"
    )
    n_additional_skill_proficiencies: int = Field(
        description="How many skill proficiencies can be chosen"
    )
    # obligatory_tool_proficiencies: int = Field(
    #     description="How many skill proficiencies can be chosen")
    # additional_tool_proficiencies: int = Field(
    #     description="How many skill proficiencies can be chosen")
    # n_additional_tool_proficiencies: int = Field(
    #     description="How many tool proficiencies can be chosen")
    statistics: list[list[Optional[Statistic]]] = Field(
        description="Statistic options of a class. For example if class grants"
        " either 2 strength and 1 constitution of 1 strenght and 2"
        " constitution it should be a 2 list. One with ['strength'"
        ", 'strength', 'constitution'] another one with ["
        "'strength', 'constitution', 'constitution']. If the "
        "statistic can be chose return None for example 2 of your "
        "choice would be [[None, None]]. If only one option can is"
        " provided for example 'Your Strength score increases by "
        "2, and your Constitution score increases by 1.' return a "
        "single list of [['strength', 'strength', 'constitution']]"
    )


class MainRaceTemplate(BaseModel):
    sub_races: list[SubRaceTemplate] = Field(
        description="Sub-races of the main race for example for Elf race the "
        "sub-races would be Pallid elf, Dark and High Elf. For "
        "Human Standard and Variant Human. If none is given for "
        "example for Half Orc list the main class in this case "
        "Half Orc. Ignore 'Eberron: Rising from the Last War' "
        "sub-races or sub-races from other expansions"
    )
