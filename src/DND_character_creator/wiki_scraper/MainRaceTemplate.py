from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.language import Language
from src.DND_character_creator.other_profficiencies import GamingSet
from src.DND_character_creator.other_profficiencies import MusicalInstrument
from src.DND_character_creator.other_profficiencies import ToolProficiency
from src.DND_character_creator.skill_proficiency import Skill


class Statistics(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    any_of_your_choice: int = Field(
        description="Typically 'Ability Score Increase: n different ability "
        "scores of your choice increase [...]'"
    )


class SubRaceTemplate(BaseModel):
    name: str
    speed: int
    darkvision_range: int
    languages: list[Language] = Field(
        description="List of languages known by this race"
    )
    obligatory_skills: list[Skill] = Field(
        description="A list of skills always provided by race.",
        default_factory=list,
    )
    skills_to_choose_from: list[Skill] = Field(
        description="A list of skills from which skills can be chosen.",
        default_factory=list,
    )
    n_skills: int = Field(description="Number of skills to choose", default=0)
    tool_proficiencies: list[
        ToolProficiency | GamingSet | MusicalInstrument
    ] = Field(description="List of tool proficiencies.", default_factory=list)
    additional_feat: bool = Field(
        "Does sub-race get a feat 'Feat: You gain " "one Feat of your choice.'"
    )
    statistics: Statistics = Field(
        description="Statistic given by the race and sub-race"
    )
    other_active_abilities: list[str] = Field(
        description="Something like Relentless Endurance or Trance. In other "
        "words abilities that influence gameplay not boosts to "
        "statistics, alignment nor proficiencies."
    )

    def __init__(self, /, **data: Any):
        if "Any of your choice" in data.get("skills_to_choose_from", []):
            data["skills_to_choose_from"] = list(
                skill.value
                for skill in Skill
                if skill.value not in data.get("obligatory_skills", [])
            )
        super().__init__(**data)


class MainRaceTemplate(BaseModel):
    sub_races: list[SubRaceTemplate] = Field(
        description="Sub-races of the main race for example for Elf race the "
        "sub-races would be Pallid elf, Dark and High Elf. For "
        "Human Standard and Variant Human. If none is given for "
        "example for Half Orc list the main class in this case "
        "Half Orc."
    )
