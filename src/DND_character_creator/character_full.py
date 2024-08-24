from __future__ import annotations

from typing import Any
from typing import Type

from pydantic import BaseModel
from pydantic import create_model
from pydantic import Field

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)  # noqa: E501
from src.DND_character_creator.choices.class_creation.character_class import (
    subclasses,
)  # noqa: E501
from src.DND_character_creator.choices.race_creation.subraces import (
    get_sub_races,
)
from src.DND_character_creator.choices.spell_slots.spell_slots import Cantrip
from src.DND_character_creator.choices.spell_slots.spell_slots import (
    filter_accessible,
)  # noqa: E501
from src.DND_character_creator.choices.spell_slots.spell_slots import (
    FirstLevel,
)  # noqa: E501
from src.DND_character_creator.choices.spell_slots.spell_slots import (
    SecondLevel,
)  # noqa: E501
from src.DND_character_creator.choices.spell_slots.spell_slots import (
    ThirdLevel,
)  # noqa: E501
from src.DND_character_creator.choices.spell_slots.spell_slots_by_level import (  # noqa: E501
    full_caster_max_spell_level,
)  # noqa: E501
from src.DND_character_creator.choices.spell_slots.spell_slots_by_level import (  # noqa: E501
    half_caster_max_spell_level,
)  # noqa: E501
from src.DND_character_creator.config import Config
from src.DND_character_creator.feats import Feat


class CharacterFull(CharacterBase):
    cantrips: list[Cantrip]
    first_level_spells: list[FirstLevel]
    second_level_spells: list[SecondLevel]
    third_level_spells: list[ThirdLevel]
    feats: list[Feat]
    sub_race: str
    sub_class: str


level_names = [
    "cantrips",
    "first_level_spells",
    "second_level_spells",
    "third_level_spells",
]


class SpellFixing(BaseModel):
    def __init__(self, /, **data: Any):
        for level_name in level_names:
            for spell in data.get(level_name, []):
                if (
                    spell
                    not in self.model_fields[level_name].annotation.__args__[0]
                ):
                    for reference_level_name in level_names:
                        if (
                            data.get(reference_level_name)
                            and spell
                            in self.model_fields[
                                reference_level_name
                            ].annotation.__args__[0]
                        ):
                            data[reference_level_name].append(spell)
                            break
                    data[level_name].remove(spell)
        super().__init__(**data)


def get_full_character_template(
    config: Config,
    character_base: CharacterBase,
) -> tuple[Type[BaseModel], dict[str, Any]]:
    fields_dictionary = dict(
        cantrips=(
            list[
                filter_accessible(Cantrip, character_base.main_class, config)
            ],
            Field(description="Not more than 6"),
        ),
        first_level_spells=(
            list[
                filter_accessible(
                    FirstLevel, character_base.main_class, config
                )
            ],
            Field(description="Not more than 6"),
        ),
        second_level_spells=(
            list[
                filter_accessible(
                    SecondLevel, character_base.main_class, config
                )
            ],
            Field(description="Not more than 4"),
        ),
        third_level_spells=(
            list[
                filter_accessible(
                    ThirdLevel, character_base.main_class, config
                )
            ],
            Field(description="Not more than 2"),
        ),
        feats=(list[Feat], ...),
        sub_race=(get_sub_races(character_base.race, config), ...),
        sub_class=(subclasses[character_base.main_class], ...),
    )
    pre_set_values = {}
    for key in tuple(fields_dictionary.keys()):
        if (pre_set_value := getattr(config, key)) is None:
            continue
        pre_set_values[key] = pre_set_value
        del fields_dictionary[key]
    if character_base.main_class in (
        MainClass.BARBARIAN,
        MainClass.FIGHTER,
        MainClass.MONK,
    ):
        for level in level_names:
            del fields_dictionary[level]
    elif character_base.main_class in (
        MainClass.ARTIFICER,
        MainClass.PALADIN,
        MainClass.RANGER,
    ):
        max_level = half_caster_max_spell_level[character_base.level]
        for i, level in enumerate(level_names):
            if i > max_level:
                del fields_dictionary[level]
    else:
        max_level = full_caster_max_spell_level[character_base.level]
        for i, level in enumerate(level_names):
            if i > max_level:
                del fields_dictionary[level]
    character = create_model(
        "Character",
        **fields_dictionary,
        __base__=SpellFixing,
        __doc__="""D&D e5 character""",
    )
    return character, pre_set_values
