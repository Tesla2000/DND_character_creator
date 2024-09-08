from __future__ import annotations

from itertools import filterfalse
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.stats_creation.statistic import (
    StatisticAndAny,
)
from src.DND_character_creator.other_profficiencies import ArmorProficiency
from src.DND_character_creator.other_profficiencies import GamingSet
from src.DND_character_creator.other_profficiencies import MusicalInstrument
from src.DND_character_creator.other_profficiencies import ToolProficiency
from src.DND_character_creator.other_profficiencies import WeaponProficiency
from src.DND_character_creator.skill_proficiency import SkillAndAny
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilityTemplate,
)


class FeatTemplate(BaseModel):
    source: Optional[str]
    ability: Optional[AbilityTemplate]
    skill_proficiency_gain: Optional[SkillAndAny]
    skill_expertise_gain: Optional[SkillAndAny] = Field(
        description="The same as double proficiency."
    )
    tool_proficiency_gain: Optional[ToolProficiency]
    instrument_proficiency_gain: Optional[MusicalInstrument]
    gaming_set_proficiency_gain: Optional[GamingSet]
    weapon_proficiencies_gain: list[WeaponProficiency] = Field(
        description="Must remain empty if nothing is provided."
    )
    armor_proficiencies_gain: list[ArmorProficiency] = Field(
        description="Must remain empty if nothing is provided."
    )
    attribute_increase: Optional[StatisticAndAny]

    def __init__(self, /, **data: Any):
        data["weapon_proficiencies_gain"] = list(
            filterfalse(
                ArmorProficiency.__contains__, data["armor_proficiencies_gain"]
            )
        )
        if (
            data["skill_proficiency_gain"] not in SkillAndAny
            and data["skill_proficiency_gain"] in ToolProficiency
        ):
            data["tool_proficiency_gain"] = data["skill_proficiency_gain"]
            data["skill_proficiency_gain"] = None
        try:
            super().__init__(**data)
        except Exception as e:
            raise e
