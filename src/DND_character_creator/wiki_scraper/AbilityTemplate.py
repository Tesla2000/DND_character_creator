from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.abilities.AbilityType import AbilityType


class AbilityTemplate(BaseModel):
    name: str
    ability_type: AbilityType = Field(
        description="Free action if not provided."
    )
    combat_related: bool = Field(
        description="Does this ability posses utility in combat. Mostly yes, "
        "the exceptions are improvements to skills parameters, "
        "and abilities such as trans or increased carrying "
        "capacity. Examples pack tactics, sunlite sensitivity."
    )
    spell_grant: bool = Field(
        description="This ability allows of a use of a spell"
    )
    description: str
    required_level: int

    def __init__(self, /, **data: Any):
        if data["ability_type"] not in AbilityType:
            data["ability_type"] = "passive"
        super().__init__(**data)


class AbilitiesTemplate(BaseModel):
    abilities: list[AbilityTemplate]
