from __future__ import annotations

import json

from src.DND_character_creator.choices.race_creation.main_race import MainRace
from src.DND_character_creator.config import Config
from src.DND_character_creator.wiki_scraper.MainRaceTemplate import (
    SubRaceTemplate,
)


def sub_race2stats(
    race: MainRace, sub_race: str, config: Config
) -> SubRaceTemplate:
    return SubRaceTemplate(
        **json.loads(
            next(
                config._sub_races_root.joinpath(race.value).rglob(
                    f"{sub_race}.json"
                )
            ).read_text()
        )
    )
