from __future__ import annotations

from typing import Any
from typing import Type

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.choices.spell_slots.spell_slots import Spell
from src.DND_character_creator.config import Config


class CharacterFull(CharacterBase):
    spell_slots: list[list[Spell]]


def get_character_additional_info_template(
    config: Config,
    character_base: CharacterBase,
) -> tuple[Type[CharacterBase], dict[str, Any]]:
    pass
    # fields_dictionary = dict(
    #     sex=(Sex, ...),
    #     class_=(MainClass, ...),
    #     backstory=(str, Field(description=config.backstory_prompt)),
    #     level=(int, ...),
    #     age=(int, ...),
    #     first_most_important_stat=(Statistic, ...),
    #     second_most_important_stat=(Statistic, ...),
    #     third_most_important_stat=(Statistic, ...),
    #     forth_most_important_stat=(Statistic, ...),
    #     fifth_most_important_stat=(Statistic, ...),
    #     sixth_most_important_stat=(Statistic, ...),
    #     race=(MainRace, ...),
    #     name=(str, ...),
    #     background=(Background, ...),
    #     alignment=(Alignment, ...),
    #     height=(int, Field(description=config.height_prompt)),
    #     weight=(str, Field(description=config.weight_prompt)),
    #     eye_color=(str, ...),
    #     skin_color=(str, ...),
    #     hairstyle=(str, ...),
    #     appearance=(str, Field(description=config.appearance_prompt)),
    # )
    # pre_set_values = {}
    # for key in tuple(fields_dictionary.keys()):
    #     if (pre_set_value := getattr(config, key)) is None:
    #         continue
    #     pre_set_values[key] = pre_set_value
    #     del fields_dictionary[key]
    # character = create_model(
    #     "Character",
    #     **fields_dictionary,
    #     __base__=BaseModel,
    #     __doc__="""D&D e5 character""",
    # )
    # if not issubclass(character, CharacterProtocol):
    #     raise ValueError(
    #         f"{character=} class is not a subclass of {CharacterProtocol=}"
    #     )
    # return character, pre_set_values
