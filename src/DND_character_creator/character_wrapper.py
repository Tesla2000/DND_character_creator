from __future__ import annotations

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.choices.health_creation.health_creation_method import (  # noqa: E501
    HealthCreationMethod,
)
from src.DND_character_creator.choices.health_creation.hit_dice import (
    class2hit_die,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.choices.stats_creation.stats_creation_method import (  # noqa: E501
    StatsCreationMethod,
)
from src.DND_character_creator.config import Config


class CharacterWrapper:
    _health = None
    _attributes = {}

    def __init__(self, character_base: CharacterBase, config: Config):
        self.config = config
        self.character_base = character_base
        self._character_details = None

    @property
    def health(self) -> int:
        if self._health:
            return self._health
        hit_die = class2hit_die[self.character_base.class_]
        if self.config.health_creation_method == HealthCreationMethod.AVERAGE:
            average = hit_die // 2 + 1
            self._health = hit_die + (self.character_base.level - 1) * average
        self._health += self.attributes
        return self._health

    @property
    def attributes(self) -> dict[Statistic, int]:
        if self._attributes:
            return self._attributes
        if (
            self.config.stats_creation_method
            == StatsCreationMethod.STANDARD_ARRAY
        ):
            for attribute, points in zip(
                (
                    self.character_base.first_most_important_stat,
                    self.character_base.second_most_important_stat,
                    self.character_base.third_most_important_stat,
                    self.character_base.forth_most_important_stat,
                    self.character_base.fifth_most_important_stat,
                    self.character_base.sixth_most_important_stat,
                ),
                (15, 14, 13, 12, 10, 8),
            ):
                self._attributes[attribute] = points
            assert (
                len(self._attributes) == 6
            ), "Some attribute value are duplicated. Ask author for help"

    @property
    def character_details(self):
        pass
