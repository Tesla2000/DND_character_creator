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
from src.DND_character_creator.character_wrapper import CharacterWrapper
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
    description_base = config.base_description.strip()
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

    character_full = CharacterFull(
        **full_pre_defined_fields,
        **character_full_template.model_dump(),
        **character_base.model_dump(),
    )
    character_wrapped = CharacterWrapper(character_full, config)

    print(
        json.dumps(
            dict(
                ChainMap(
                    dict(
                        health=character_wrapped.health,
                        attributes=character_wrapped.attributes,
                        feats=character_wrapped.feats,
                    ),
                    character_full.get_without_stats(),
                )
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    exit(main())
