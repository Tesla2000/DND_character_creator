from __future__ import annotations

from typing import Any
from typing import Type

from pydantic import BaseModel
from pydantic import create_model
from pydantic import Field

from src.DND_character_creator.choices.alignment import Alignment
from src.DND_character_creator.choices.background_creatrion.background import (
    Background,
)
from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.race_creation.main_race import MainRace
from src.DND_character_creator.choices.sex import Sex
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.config import Config


class CharacterBase(BaseModel):
    sex: Sex
    backstory: str
    level: int
    age: int
    main_class: MainClass
    first_most_important_stat: Statistic
    second_most_important_stat: Statistic
    third_most_important_stat: Statistic
    forth_most_important_stat: Statistic
    fifth_most_important_stat: Statistic
    sixth_most_important_stat: Statistic
    main_race: MainRace
    name: str
    background: Background
    alignment: Alignment
    height: int
    weight: int
    eye_color: str
    skin_color: str
    hairstyle: str
    appearance: str
    character_traits: str
    ideals: str
    bounds: str
    weaknesses: str


def get_base_character_template(
    config: Config,
) -> tuple[Type[BaseModel], dict[str, Any]]:
    fields_dictionary = dict(
        sex=(Sex, ...),
        main_class=(MainClass, ...),
        backstory=(str, Field(description=config.backstory_prompt)),
        level=(int, ...),
        age=(int, ...),
        first_most_important_stat=(Statistic, ...),
        second_most_important_stat=(Statistic, ...),
        third_most_important_stat=(Statistic, ...),
        forth_most_important_stat=(Statistic, ...),
        fifth_most_important_stat=(Statistic, ...),
        sixth_most_important_stat=(Statistic, ...),
        main_race=(MainRace, ...),
        name=(str, ...),
        background=(Background, ...),
        alignment=(Alignment, ...),
        height=(int, Field(description=config.height_prompt)),
        weight=(int, Field(description=config.weight_prompt)),
        eye_color=(str, ...),
        skin_color=(str, ...),
        hairstyle=(str, ...),
        appearance=(str, Field(description=config.appearance_prompt)),
        character_traits=(str, ...),
        ideals=(str, ...),
        bounds=(str, ...),
        weaknesses=(str, ...),
    )
    pre_set_values = {}
    for key in tuple(fields_dictionary.keys()):
        if (pre_set_value := getattr(config, key)) is None:
            continue
        pre_set_values[key] = pre_set_value
        del fields_dictionary[key]
    character = create_model(
        "Character",
        **fields_dictionary,
        __base__=BaseModel,
        __doc__="""D&D e5 character""",
    )
    return character, pre_set_values
