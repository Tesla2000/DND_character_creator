from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field

from src.DND_character_creator.choices.abilities.AbilityType import AbilityType


class Ability(BaseModel):
    name: str
    ability_type: AbilityType
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


class Abilities(BaseModel):
    abilities: list[Ability]
