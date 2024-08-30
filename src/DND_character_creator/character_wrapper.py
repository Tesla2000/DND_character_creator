from __future__ import annotations

import json
from itertools import chain
from itertools import islice
from itertools import repeat
from operator import attrgetter
from typing import Sequence

from langchain_core.language_models import BaseChatModel
from pydantic import BaseModel
from pydantic import create_model

from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    BattleManeuver,
)  # noqa: E501
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    maneuver_descriptions,
)  # noqa: E501
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    n_maneuvers,
)  # noqa: E501
from src.DND_character_creator.choices.feat_creation.ability_score_improvements import (  # noqa: E501
    main_class2ability_score_improvements,
)
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    fighting_style_descriptions,
)  # noqa: E501
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    FightingStyle,
)  # noqa: E501
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    n_fighting_styles,
)  # noqa: E501
from src.DND_character_creator.choices.health_creation.health_creation_method import (  # noqa: E501
    HealthCreationMethod,
)
from src.DND_character_creator.choices.health_creation.hit_dice import (
    class2hit_die,
)
from src.DND_character_creator.choices.main_class2saving_throws import (
    main_class2saving_throws,
)
from src.DND_character_creator.choices.race_creation.sub_race2attributes import (  # noqa: E501
    sub_race2stats,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)  # noqa: E501
from src.DND_character_creator.choices.stats_creation.statistic import (
    StatisticAndAny,
)  # noqa: E501
from src.DND_character_creator.choices.stats_creation.stats_creation_method import (  # noqa: E501
    StatsCreationMethod,
)
from src.DND_character_creator.config import Config
from src.DND_character_creator.feats import Feat
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilityTemplate,
)
from src.DND_character_creator.wiki_scraper.FeatTemplate import FeatTemplate


class CharacterWrapper:
    def __init__(
        self, character_full: CharacterFull, config: Config, llm: BaseChatModel
    ):
        self.llm = llm
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
        race_attributes = self._race_stats.statistics.model_dump()
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
            elif (
                self._feat2feat_template(feat).attribute_increase
                == StatisticAndAny.ANY_OF_YOUR_CHOICE
            ):
                attributes_in_order = self._reduce_attributes_in_order(
                    attributes_in_order
                )
                if attributes_in_order:
                    self._attributes[attributes_in_order[0]] += 1
            elif self._feat2feat_template(feat).attribute_increase:
                self._attributes[
                    self._feat2feat_template(feat).attribute_increase
                ] = min(
                    20,
                    self._attributes[
                        self._feat2feat_template(feat).attribute_increase
                    ]
                    + 1,
                )
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
    def saving_throws(self) -> set[Statistic]:
        return main_class2saving_throws[self.character.main_class]

    @property
    def fighting_styles(self) -> dict[BattleManeuver, str]:
        n_styles = n_maneuvers(self)
        if not n_styles:
            return {}
        battle_maneuver_fields = tuple(
            f"battle_maneuver{i}" for i in range(1, 1 + n_styles)
        )
        fields_dictionary = {
            field_name: (BattleManeuver, ...)
            for field_name in battle_maneuver_fields
        }
        battle_maneuvers = create_model(
            "BattleManeuver",
            **fields_dictionary,
            __base__=BaseModel,
        )
        battle_maneuver_llm = self.llm.with_structured_output(battle_maneuvers)
        picked_maneuvers = attrgetter(*battle_maneuver_fields)(
            battle_maneuver_llm.invoke(
                "Given the description of character pick suitable fighting "
                "styles.\n\nDescription:\n\n"
                + self.character.model_dump_json(indent=2)
            )
        )
        return {
            maneuver: maneuver_descriptions[maneuver]
            for maneuver in picked_maneuvers
        }

    @property
    def fighting_battle_maneuvers(self) -> dict[FightingStyle, str]:
        n_styles = n_fighting_styles(self)
        if not n_styles:
            return {}
        fighting_style_fields = tuple(
            f"fighting_style{i}" for i in range(1, 1 + n_styles)
        )
        fields_dictionary = {
            field_name: (FightingStyle, ...)
            for field_name in fighting_style_fields
        }
        fighting_styles = create_model(
            "FightingStyles",
            **fields_dictionary,
            __base__=BaseModel,
        )
        fighting_style_llm = self.llm.with_structured_output(fighting_styles)
        picked_styles = attrgetter(*fighting_style_fields)(
            fighting_style_llm.invoke(
                f"Given the description of character pick suitable fighting "
                f"styles.\n\nDescription:\n\n"
                f"{self.character.model_dump_json(indent=2)}"
            )
        )
        return {
            style: fighting_style_descriptions[style]
            for style in picked_styles
        }

    @property
    def combat_abilities(self) -> list[str]:
        abilities = []
        for feat in self.feats:
            ability = self._feat2feat_template(feat).ability
            if (
                ability.combat_related
                and ability.required_level <= self.character.level
            ):
                abilities.append(ability.description)
        for ability_name in self._race_stats.other_active_abilities:
            ability_name = ability_name.split(":")[0]
            ability = AbilityTemplate(
                **json.loads(
                    self.config.race_abilities_root.joinpath(
                        self.character.main_race.value
                    )
                    .joinpath(f"{ability_name}.json")
                    .read_text()
                )
            )
            if (
                ability.combat_related
                and ability.required_level <= self.character.level
            ):
                abilities.append(ability.description)
        for (
            main_class_ability_path
        ) in self.config.main_class_abilities_root.joinpath(
            self.character.main_class
        ).iterdir():
            ability = AbilityTemplate(
                **json.loads(main_class_ability_path.read_text())
            )
            if (
                ability.combat_related
                and ability.required_level <= self.character.level
            ):
                abilities.append(ability.description)
        for sub_class_ability_path in (
            self.config.sub_class_abilities_root.joinpath(
                self.character.main_class
            )
            .joinpath(self.character.sub_class)
            .iterdir()
        ):
            ability = AbilityTemplate(
                **json.loads(sub_class_ability_path.read_text())
            )
            if (
                ability.combat_related
                and ability.required_level <= self.character.level
            ):
                abilities.append(ability.description)
        return abilities

    def _feat2feat_template(self, feat: Feat) -> FeatTemplate:
        return FeatTemplate(
            **json.loads(
                self.config.feats_root.joinpath(
                    f"{feat.value}.json"
                ).read_text()
            )
        )

    def _improve_from_ability_score(
        self, attributes_in_order: Sequence[Statistic]
    ):
        def _add2next_odd() -> bool:
            for attribute in attributes_in_order[1:]:
                if self._attributes[attribute] % 2:
                    self._attributes[attribute] += 1
                    return True

        attributes_in_order = self._reduce_attributes_in_order(
            attributes_in_order
        )
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

    def _reduce_attributes_in_order(
        self, attributes_in_order: tuple[Statistic, ...]
    ) -> tuple[Statistic, ...]:
        while (
            attributes_in_order
            and self._attributes[attributes_in_order[0]] == 20
        ):
            attributes_in_order = attributes_in_order[1:]
        return attributes_in_order
