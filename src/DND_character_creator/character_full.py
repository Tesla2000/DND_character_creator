from __future__ import annotations

from typing import Any
from typing import Optional
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
from src.DND_character_creator.choices.equipment_creation.armor import (
    ArmorName,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.weapons import (
    WeaponName,
)
from src.DND_character_creator.choices.invocations.eldritch_invocation import (
    WarlockPact,
)
from src.DND_character_creator.choices.race_creation.sub_races import (
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
    cantrips: list[Cantrip] = Field(default_factory=list)
    first_level_spells: list[FirstLevel] = Field(default_factory=list)
    second_level_spells: list[SecondLevel] = Field(default_factory=list)
    third_level_spells: list[ThirdLevel] = Field(default_factory=list)
    feats: list[Feat]
    sub_race: str
    sub_class: str
    warlock_pact: Optional[WarlockPact]
    armor: ArmorName = Field(
        description="You would typically have clothes for spell casters. You "
        "have a total of 'amount_of_gold_for_equipment' to spend "
        "for both armor and weapons. Barbarians and Monks usally "
        "don't use armor either."
    )
    uses_shield: bool
    weapons: list[WeaponName] = Field(
        description="You would typically leave it empty for spell casters. "
        "You have a total of 'amount_of_gold_for_equipment' to "
        "spend for both armor and weapons."
    )

    def get_without_stats(self):
        return self.model_dump(
            exclude={
                "first_most_important_stat",
                "second_most_important_stat",
                "third_most_important_stat",
                "fourth_most_important_stat",
                "fifth_most_important_stat",
                "sixth_most_important_stat",
            }
        )


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
        feats=(
            list[Feat],
            Field(
                description="I urge you to consider Ability score "
                "improvement as they are pretty common however "
                "if other feats fit better go for it."
            ),
        ),
        sub_race=(get_sub_races(character_base.main_race, config), ...),
        sub_class=(subclasses[character_base.main_class], ...),
        armor=(
            ArmorName,
            Field(
                description="You would typically have clothes for spell "
                "casters. "
                "You have a total of 'amount_of_gold_for_equipment' to spend "
                "for both armor and weapons. Barbarians and Monks usually "
                "don't use armor either. Shield is not a valid input. Should "
                "be "
                "provided in uses_shield field."
            ),
        ),
        uses_shield=(bool, ...),
        weapons=(
            list[WeaponName],
            Field(
                description="You would typically leave it empty for spell "
                "casters."
                " You have a total of 'amount_of_gold_for_equipment' to "
                "spend for both armor and weapons."
            ),
        ),
    )
    pre_set_values = {}
    if (
        character_base.main_class == MainClass.WARLOCK
        and character_base.level >= 2
    ):
        fields_dictionary["warlock_pact"] = (WarlockPact, ...)
    else:
        pre_set_values["warlock_pact"] = None
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
