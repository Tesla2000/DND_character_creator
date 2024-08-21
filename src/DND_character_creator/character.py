from __future__ import annotations

from typing import Type

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.alignment import Alignment
from src.DND_character_creator.choices.background_creatrion.background import (
    Background,
)
from src.DND_character_creator.choices.class_creation.character_class import (
    CharacterClass,
)
from src.DND_character_creator.choices.race import Race
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.config import Config


def get_character_template(config: Config) -> Type[BaseModel]:
    class Character(BaseModel):
        """D&D e5 character"""

        class_: CharacterClass
        backstory: str = Field(description=config.backstory_prompt)
        age: int
        first_most_important_stat: Statistic
        second_most_important_stat: Statistic
        third_most_important_stat: Statistic
        forth_most_important_stat: Statistic
        fifth_most_important_stat: Statistic
        sixth_most_important_stat: Statistic
        race: Race
        name: str
        background: Background
        alignment: Alignment

    return Character
