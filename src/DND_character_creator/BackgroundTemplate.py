from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.language import Language
from src.DND_character_creator.other_profficiencies import GamingSet
from src.DND_character_creator.other_profficiencies import MusicalInstrument
from src.DND_character_creator.other_profficiencies import ToolProficiency
from src.DND_character_creator.skill_proficiency import SkillAndAny


class BackgroundTemplate(BaseModel):
    skills: list[SkillAndAny] = Field(
        description="Skill proficiencies gained with background. "
        "Empty list if None."
    )
    tools: list[ToolProficiency | GamingSet | MusicalInstrument] = Field(
        description="Tool proficiencies gained with background. "
        "Empty list if None. "
        "Mind options you are provided 'Vehicles (Land)' should be"
        " 'Land vehicles' for example."
    )
    languages: list[Language] = Field(
        description="Languages gained with backgroud. "
        "If 2 or more of your choice place as many values in a "
        "list. For example for 'Two of your choice' it is "
        "['Any of your choice', 'Any of your choice']. "
        "Empty list if None."
    )

    def __init__(self, /, **data: Any):
        data["tools"] = list(map(str.capitalize, data["tools"]))
        super().__init__(**data)
