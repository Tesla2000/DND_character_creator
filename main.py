from __future__ import annotations

from langchain_openai import ChatOpenAI

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.character_base import (
    get_character_base_template,
)  # noqa: E501
from src.DND_character_creator.config import Config
from src.DND_character_creator.config import create_config_with_args
from src.DND_character_creator.config import parse_arguments


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    character_template, pre_defined_fields = get_character_base_template(
        config
    )
    llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(
        character_template
    )
    description = config.description.strip()
    if pre_defined_fields:
        description += (
            f"\nThe following details about the character are "
            f"given {pre_defined_fields}"
        )
    character_template = llm.invoke(description)
    CharacterBase(**pre_defined_fields, **character_template.model_fields())


if __name__ == "__main__":
    exit(main())
