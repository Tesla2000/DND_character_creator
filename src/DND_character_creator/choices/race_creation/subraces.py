from __future__ import annotations

from enum import Enum
from typing import Type
from typing import TYPE_CHECKING

from src.DND_character_creator.choices.race_creation.main_race import MainRace

if TYPE_CHECKING:
    from src.DND_character_creator.config import Config


def get_sub_races(main_race: MainRace, config: "Config") -> Type[Enum]:
    return Enum(
        f"{main_race.value}SubRace",
        dict(
            (
                (name := path.with_suffix("").name).upper().replace(" ", "_"),
                name,
            )
            for path in _get_sub_races(main_race, config)
        ),
    )


def _get_sub_races(main_race: MainRace, config: "Config"):
    for path in filter(
        lambda path: path.name in config.subclass_sources,
        config._sub_races_root.joinpath(main_race.value).iterdir(),
    ):
        yield from path.iterdir()
