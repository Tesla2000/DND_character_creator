from __future__ import annotations

import json
from collections import ChainMap

from langchain_openai import ChatOpenAI

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.character_base import (
    get_base_character_template,
)
from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.character_full import (
    get_full_character_template,
)  # noqa: E501
from src.DND_character_creator.config import Config
from src.DND_character_creator.config import create_config_with_args
from src.DND_character_creator.config import parse_arguments


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    llm = ChatOpenAI(model=config.llm)
    character_base_template, base_pre_defined_fields = (
        get_base_character_template(config)
    )
    description_base = config.description.strip()
    if base_pre_defined_fields:
        description_base += (
            f"\nThe following details about the character are "
            f"given:\n{json.dumps(base_pre_defined_fields, indent=2)}"
        )
    base_template = llm.with_structured_output(character_base_template)
    character_base_template = base_template.invoke(description_base)
    character_base = CharacterBase(
        **base_pre_defined_fields, **character_base_template.model_dump()
    )
    # character_base = CharacterBase(
    #     **{
    #         "sex": "male",
    #         "backstory": "",
    #         "level": 5,
    #         "age": 30,
    #         "main_class": "Druid",
    #         "first_most_important_stat": "wisdom",
    #         "second_most_important_stat": "dexterity",
    #         "third_most_important_stat": "constitution",
    #         "forth_most_important_stat": "strength",
    #         "fifth_most_important_stat": "intelligence",
    #         "sixth_most_important_stat": "charisma",
    #         "race": "Elf",
    #         "name": "Elion Greenleaf",
    #         "background": "Outlander",
    #         "alignment": "chaotic_good",
    #         "height": 180,
    #         "weight": 75,
    #         "eye_color": "green",
    #         "skin_color": "light",
    #         "hairstyle": "long and flowing",
    #         "appearance": "Elion has a lean, athletic build with a deep connection to nature. He has striking green eyes that reflect the forest, and his long, flowing hair is reminiscent of leaves swaying in the breeze. His attire consists of natural materials, adorned with symbols of the forest and wildlife.",  # noqa: E501
    #     }
    # )
    character_full_template, full_pre_defined_fields = (
        get_full_character_template(config, character_base)
    )
    description_full = config.full_description.strip()
    pre_defined = json.dumps(
        dict(
            **ChainMap(
                full_pre_defined_fields,
                json.loads(character_base.model_dump_json()),
            )
        ),
        indent=2,
    )
    description_full += (
        f"\nThe following details about the character are given:\n"
        f"{pre_defined}"
    )
    full_template = llm.with_structured_output(character_full_template)
    character_full_template = full_template.invoke(description_full)

    _ = CharacterFull(
        **full_pre_defined_fields, **character_full_template.model_dump()
    )
    # character_full = CharacterFull(**{
    #     'cantrips': ['Druidcraft', 'Thorn Whip', 'Produce Flame', 'Guidance',
    #                  'Shape Water', 'Mending'],
    #     'first_level_spells': ['Entangle', 'Goodberry', 'Healing Word',
    #                            'Detect Magic', 'Faerie Fire', 'Thunderwave'],
    #     'second_level_spells': ['Barkskin', 'Moonbeam', 'Pass Without Trace',
    #                             'Spike Growth'],
    #     'third_level_spells': ['Conjure Animals', 'Call Lightning'],
    #     'feats': ['Mobile', 'Resilient', 'Lucky', 'Observant'],
    #     'sub_race': 'Wood Elf', 'sub_class': 'Circle of the Shepherd'})


if __name__ == "__main__":
    exit(main())
