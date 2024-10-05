from __future__ import annotations

import json

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.config import Config
from src.DND_character_creator.wiki_scraper.MainClassTemplate import (
    MainClassTemplate,
)


def main_class2proficiencies(
    main_class: MainClass, config: Config
) -> MainClassTemplate:
    return MainClassTemplate(
        **json.loads(
            config.main_class_root.joinpath(main_class.value)
            .with_suffix(".json")
            .read_text()
        )
    )
