from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from src.DND_character_creator.other_profficiencies import ToolProficiency
from src.DND_character_creator.skill_proficiency import SkillProficiencyAndAny
from src.DND_character_creator.wiki_scraper.AbilityTemplate import Ability


class Abilities(BaseModel):
    ability: Ability
    skill_proficiency_gain: Optional[SkillProficiencyAndAny]
    skill_expertise_gain: Optional[SkillProficiencyAndAny]
    tool_proficiency_gain: Optional[ToolProficiency]
    weapon_proficiencies_gain: list[ToolProficiency]
