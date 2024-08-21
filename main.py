from __future__ import annotations

from langchain_openai import ChatOpenAI

from src.DND_character_creator.character import get_character_template
from src.DND_character_creator.config import Config
from src.DND_character_creator.config import create_config_with_args
from src.DND_character_creator.config import parse_arguments


def main():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    character_template = get_character_template(config)
    llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(
        character_template
    )
    llm.invoke(config.description)


if __name__ == "__main__":
    exit(main())
