from __future__ import annotations

import json
from itertools import chain
from itertools import islice
from itertools import repeat
from typing import Sequence

from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.choices.feat_creation.ability_score_improvements import (  # noqa: E501
    main_class2ability_score_improvements,
)
from src.DND_character_creator.choices.health_creation.health_creation_method import (  # noqa: E501
    HealthCreationMethod,
)
from src.DND_character_creator.choices.health_creation.hit_dice import (
    class2hit_die,
)
from src.DND_character_creator.choices.race_creation.sub_race2attributes import (  # noqa: E501
    sub_race2stats,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.choices.stats_creation.stats_creation_method import (  # noqa: E501
    StatsCreationMethod,
)
from src.DND_character_creator.config import Config
from src.DND_character_creator.feats import Feat
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilityTemplate,
)


class CharacterWrapper:
    def __init__(self, character_full: CharacterFull, config: Config):
        self.config = config
        self.character = character_full
        self._character_details = None
        self._feats = None
        self._attributes = {}
        self._health = None
        self._race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, config
        )

    @property
    def health(self) -> int:
        if self._health:
            return self._health
        hit_die = class2hit_die[self.character.main_class]
        if self.config.health_creation_method == HealthCreationMethod.AVERAGE:
            average = hit_die // 2 + 1
            self._health = hit_die + (self.character.level - 1) * average
        self._health += self.character.level * (
            (self.attributes[Statistic.CONSTITUTION] - 10) // 2
        )
        if Feat.TOUGH in self.feats:
            self._health += 2 * self.character.level
        return self._health

    @property
    def attributes(self) -> dict[Statistic, int]:
        attributes_in_order = (
            self.character.first_most_important_stat,
            self.character.second_most_important_stat,
            self.character.third_most_important_stat,
            self.character.forth_most_important_stat,
            self.character.fifth_most_important_stat,
            self.character.sixth_most_important_stat,
        )
        if self._attributes:
            return self._attributes
        if (
            self.config.stats_creation_method
            == StatsCreationMethod.STANDARD_ARRAY
        ):
            for attribute, points in zip(
                attributes_in_order,
                (15, 14, 13, 12, 10, 8),
            ):
                self._attributes[attribute] = points
            assert (
                len(self._attributes) == 6
            ), "Some attribute value are duplicated. Ask author for help"
        race_attributes = self._race_stats.statistics
        for attribute_name in self._attributes:
            self._attributes[attribute_name] += race_attributes[attribute_name]
        if race_attributes["any_of_your_choice"] == 3:
            self._attributes[self.character.first_most_important_stat] += 2
            self._attributes[self.character.second_most_important_stat] += 1
        elif race_attributes["any_of_your_choice"]:
            self._attributes[
                self.character.first_most_important_stat
            ] += race_attributes["any_of_your_choice"]
        for feat in self.feats:
            if feat == Feat.ABILITY_SCORE_IMPROVEMENT:
                self._improve_from_ability_score(attributes_in_order)
        return self._attributes

    @property
    def feats(self) -> list[Feat]:
        if self._feats:
            return self._feats
        ability_score_improvements = main_class2ability_score_improvements[
            self.character.main_class
        ]
        for improvements, level_required in enumerate(
            ability_score_improvements
        ):
            if level_required > self.character.level:
                break
        improvements += self._race_stats.additional_feat
        self._feats = list(
            islice(
                chain.from_iterable(
                    (
                        self.character.feats,
                        repeat(Feat.ABILITY_SCORE_IMPROVEMENT),
                    )
                ),
                improvements,
            )
        )
        return self._feats

    @property
    def combat_abilities(self) -> list[str]:
        abilities = []
        for feat in self.feats:
            ability = AbilityTemplate(
                **json.loads(
                    self.config._feats_root.joinpath(
                        f"{feat.value}.json"
                    ).read_text()
                )
            )
            if (
                ability.combat_related
                and ability.required_level >= self.character.level
            ):
                abilities.append(ability.description)
        for ability_name in self._race_stats.other_active_abilities:
            ability_name = ability_name.split(":")[0]
            ability = AbilityTemplate(
                **json.loads(
                    self.config._race_abilities_root.joinpath(
                        self.character.main_race.value
                    )
                    .joinpath(f"{ability_name}.json")
                    .read_text()
                )
            )
            if (
                ability.combat_related
                and ability.required_level >= self.character.level
            ):
                abilities.append(ability.description)

    def _improve_from_ability_score(
        self, attributes_in_order: Sequence[Statistic]
    ):
        def _add2next_odd() -> bool:
            for attribute in attributes_in_order[1:]:
                if self._attributes[attribute] % 2:
                    self._attributes[attribute] += 1
                    return True

        while attributes_in_order and attributes_in_order[0] == 20:
            attributes_in_order = attributes_in_order[1:]
        if len(attributes_in_order) == 1:
            self._attributes[attributes_in_order[0]] = min(
                20, self._attributes[attributes_in_order[0]] + 2
            )
            return
        if (
            self._attributes[attributes_in_order[0]] % 2
            and self._attributes[attributes_in_order[0]] == 19
        ):
            self._attributes[attributes_in_order[0]] += 1
            if not _add2next_odd():
                self._attributes[attributes_in_order[1]] += 1
        elif self._attributes[attributes_in_order[0]] % 2:
            self._attributes[attributes_in_order[0]] += 1
            if not _add2next_odd():
                self._attributes[attributes_in_order[0]] += 1
        else:
            self._attributes[attributes_in_order[0]] += 2
