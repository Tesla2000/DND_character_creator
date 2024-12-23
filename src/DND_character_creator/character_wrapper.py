from __future__ import annotations

import json
import random
import sys
from enum import Enum
from functools import partial
from itertools import chain
from itertools import filterfalse
from itertools import islice
from itertools import repeat
from operator import attrgetter
from typing import Any
from typing import Callable
from typing import Optional
from typing import Sequence
from typing import TYPE_CHECKING

from langchain_core.language_models import BaseChatModel
from more_itertools import always_iterable
from pydantic import BaseModel
from pydantic import create_model
from pydantic import Field

from src.DND_character_creator.choices.abilities.AbilityType import AbilityType
from src.DND_character_creator.choices.background_creatrion.background2stats import (  # noqa: E501
    background2stats,
)
from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.language import Language
from src.DND_character_creator.choices.main_class.main_class2proficiencies import (  # noqa: E501
    main_class2proficiencies,
)
from src.DND_character_creator.choices.race_creation.main_race import MainRace
from src.DND_character_creator.choices.spell_slots.spell_slots import Spell
from src.DND_character_creator.choices.spell_slots.spell_slots_by_level import (  # noqa: E501
    main_class2spell_slots,
)
from src.DND_character_creator.choices.spell_slots.spellcasting_abilities import (  # noqa: E501
    spellcasting_ability_map,
)
from src.DND_character_creator.other_profficiencies import ArmorProficiency
from src.DND_character_creator.other_profficiencies import GamingSet
from src.DND_character_creator.other_profficiencies import MusicalInstrument
from src.DND_character_creator.other_profficiencies import ToolProficiency
from src.DND_character_creator.other_profficiencies import WeaponProficiency
from src.DND_character_creator.skill_proficiency import Skill
from src.DND_character_creator.skill_proficiency import skill2ability
from src.DND_character_creator.skill_proficiency import SkillAndAny

if TYPE_CHECKING:
    from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    BattleManeuver,
)  # noqa: E501
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    maneuver2ability,
)  # noqa: E501
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    get_n_maneuvers,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.armor import Armor
from src.DND_character_creator.choices.equipment_creation.armor import (
    armor_list,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.armor import (
    ArmorCategory,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.item import Item
from src.DND_character_creator.choices.equipment_creation.weapons import (
    weapon_list,
    Weapon,
)
from src.DND_character_creator.choices.feat_creation.ability_score_improvements import (  # noqa: E501
    main_class2ability_score_improvements,
)
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    fighting_style2ability,
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
from src.DND_character_creator.choices.invocations.eldritch_invocation import (
    invocations,
)  # noqa: E501
from src.DND_character_creator.choices.invocations.eldritch_invocation import (
    n_eldrich_invocations,
)  # noqa: E501
from src.DND_character_creator.choices.main_class.main_class2saving_throws import (  # noqa: E501
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
        self._feats = None
        self._attributes = {}
        self._health = None
        self._race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, config
        )
        self._eldritch_invocations = None
        self._fighting_styles = None
        self._battle_maneuvers = None
        self._saving_throws = None
        self._equipment = None
        self._prepared_spells = None
        self._skill_proficiencies = None
        self._tool_proficiencies = None
        self._languages = None
        self._gaming_set_proficiencies = None
        self._musical_instrument_proficiencies = None

    @property
    def health(self) -> int:
        if self._health:
            return self._health
        hit_die = self.hit_die
        if self.config.health_creation_method == HealthCreationMethod.AVERAGE:
            average = hit_die // 2 + 1
            self._health = hit_die + (self.character.level - 1) * average
        self._health += self.character.level * (
            self.attributes[Statistic.CONSTITUTION] // 2 - 5
        )
        if Feat.TOUGH in self.feats:
            self._health += 2 * self.character.level
        self._health += self.character.main_race == MainRace.DWARF
        return self._health

    @property
    def skill_proficiencies(self) -> list[Skill]:
        if self._skill_proficiencies:
            return self._skill_proficiencies
        skill_proficiencies = set()
        race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        )
        background_stats = background2stats(
            self.character.background, self.config
        )
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        skill_proficiencies = skill_proficiencies.union(
            main_class.obligatory_skills
        )
        skill_proficiencies = skill_proficiencies.union(
            race_stats.obligatory_skills
        )
        skill_proficiencies = skill_proficiencies.union(
            filterfalse(
                SkillAndAny.ANY_OF_YOUR_CHOICE.__eq__, background_stats.skills
            )
        )
        n_any_choice = sum(
            map(SkillAndAny.ANY_OF_YOUR_CHOICE.__eq__, background_stats.skills)
        )
        race_choice_options = race_stats.skills_to_choose_from
        n_race_choices = race_stats.n_skills
        class_choice_options = main_class.skills_to_choose_from
        n_class_choices = main_class.n_skills
        other_options = Enum(
            "OtherOptions",
            {
                option.value.upper().replace(" ", ""): option.value
                for option in Skill
                if option.value not in skill_proficiencies
            },
        )
        race_options = Enum(
            "RaceOptions",
            {
                option.value.upper().replace(" ", ""): option.value
                for option in race_choice_options
                if option.value not in skill_proficiencies
            },
        )
        class_options = Enum(
            "ClassOptions",
            {
                option.value.upper().replace(" ", ""): option.value
                for option in class_choice_options
                if option.value not in skill_proficiencies
            },
        )

        class PickSkillAtRandom(BaseModel):
            def __init__(self, /, **data: Any):
                for key, value in data.items():
                    while value not in self.model_fields[key].annotation:
                        value = random.choice(
                            tuple(self.model_fields[key].annotation)
                        )
                        data[key] = value
                super().__init__(**data)

        skill_choice_model = create_model(
            "SkillChoice",
            **{
                f"race_skill{i + 1}": (race_options, ...)
                for i in range(n_race_choices)
                if len(race_options)
            },
            **{
                f"class_skill{i + 1}": (class_options, ...)
                for i in range(n_class_choices)
                if len(class_options)
            },
            **{
                f"other_skill{i + 1}": (other_options, ...)
                for i in range(n_any_choice)
                if len(other_options)
            },
            __base__=PickSkillAtRandom,
        )
        skills_llm = self.llm.with_structured_output(skill_choice_model)
        picked_skills = attrgetter(
            *tuple(
                f"race_skill{i + 1}"
                for i in range(n_race_choices)
                if len(race_options)
            ),
            *tuple(
                f"class_skill{i + 1}"
                for i in range(n_class_choices)
                if len(class_options)
            ),
            *tuple(
                f"other_skill{i + 1}"
                for i in range(n_any_choice)
                if len(other_options)
            ),
        )(
            skills_llm.invoke(
                "Given the description of character pick suitable skills."
                f"WARNING! the flowing skills {skill_proficiencies} are "
                "already known and can't be chosen!\n\nDescription:\n\n"
                + self.character.model_dump_json(indent=2)
            )
        )
        self._skill_proficiencies = list(
            skill_proficiencies.union(always_iterable(picked_skills))
        )
        return self._skill_proficiencies

    @property
    def skill_modifiers(self) -> dict[Skill, int]:
        proficiencies = tuple(s.value for s in self.skill_proficiencies)
        return {
            Skill(skill): self.modifiers[skill2ability[skill]]
            + (skill.value in proficiencies) * self.proficiency_bonus
            for skill in Skill
        }

    @property
    def weapon_proficiencies(self) -> list[WeaponProficiency]:
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        return main_class.weapons

    @property
    def armor_proficiencies(self) -> list[ArmorProficiency]:
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        return main_class.armor

    @property
    def tool_proficiencies(self) -> list[ToolProficiency]:
        if self._tool_proficiencies:
            return self._tool_proficiencies
        race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        )
        background_stats = background2stats(
            self.character.background, self.config
        )
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        race_tools_proficiencies = list(
            filter(ToolProficiency.__instancecheck__, main_class.tools)
        )
        background_tools_proficiencies = list(
            filter(ToolProficiency.__instancecheck__, background_stats.tools)
        )
        main_class_tools_proficiencies = list(
            filter(
                ToolProficiency.__instancecheck__,
                race_stats.tool_proficiencies,
            )
        )
        all_proficiencies = (
            race_tools_proficiencies
            + background_tools_proficiencies
            + main_class_tools_proficiencies
        )
        obligatory = set(
            filterfalse(
                ToolProficiency.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies
            )
        )
        n_additional = sum(
            map(ToolProficiency.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies)
        )
        rest = Enum(
            "ToolProficiency",
            {
                tool.value.upper().replace(" ", ""): tool.value
                for tool in ToolProficiency
                if tool not in obligatory
            },
        )
        additional = list()
        if n_additional:
            field_names = tuple(
                f"tool_proficiency{i + 1}" for i in range(n_additional)
            )
            tool_template = create_model(
                "ToolProficiencies",
                **{name: (rest, ...) for name in field_names},
            )
            tool_llm = self.llm.with_structured_output(tool_template)
            additional = attrgetter(*field_names)(
                tool_llm.invoke(
                    "Given the description of character pick suitable tool "
                    "proficiencies.\n\nDescription:\n\n"
                    + self.character.model_dump_json(indent=2)
                )
            )
        additional = always_iterable(additional)
        self._tool_proficiencies = list(obligatory.union(additional))
        return self._tool_proficiencies

    @property
    def gaming_set_proficiencies(self) -> list[GamingSet]:
        tool_type = GamingSet
        if self._gaming_set_proficiencies:
            return self._gaming_set_proficiencies
        race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        )
        background_stats = background2stats(
            self.character.background, self.config
        )
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        race_gaming_set_proficiencies = list(
            filter(tool_type.__instancecheck__, main_class.tools)
        )
        background_gaming_set_proficiencies = list(
            filter(tool_type.__instancecheck__, background_stats.tools)
        )
        main_class_gaming_set_proficiencies = list(
            filter(tool_type.__instancecheck__, race_stats.tool_proficiencies)
        )
        all_proficiencies = (
            race_gaming_set_proficiencies
            + background_gaming_set_proficiencies
            + main_class_gaming_set_proficiencies
        )
        obligatory = set(
            filterfalse(tool_type.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies)
        )
        n_additional = sum(
            map(tool_type.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies)
        )
        rest = Enum(
            "GamingSetProficiency",
            {
                tool.value.upper().replace(" ", ""): tool.value
                for tool in tool_type
                if tool not in obligatory
            },
        )
        additional = list()
        if n_additional:
            field_names = tuple(
                f"gaming_set_proficiency{i + 1}" for i in range(n_additional)
            )
            tool_template = create_model(
                "GamingSetProficiencies",
                **{name: (rest, ...) for name in field_names},
            )
            tool_llm = self.llm.with_structured_output(tool_template)
            additional = attrgetter(*field_names)(
                tool_llm.invoke(
                    "Given the description of character pick suitable gaming "
                    "set proficiencies.\n\nDescription:\n\n"
                    + self.character.model_dump_json(indent=2)
                )
            )
        additional = (
            additional if isinstance(additional, list) else [additional]
        )
        self._gaming_set_proficiencies = list(obligatory.union(additional))
        return self._gaming_set_proficiencies

    @property
    def musical_instrument_proficiencies(self) -> list[MusicalInstrument]:
        tool_type = MusicalInstrument
        if self._musical_instrument_proficiencies:
            return self._musical_instrument_proficiencies
        race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        )
        background_stats = background2stats(
            self.character.background, self.config
        )
        main_class = main_class2proficiencies(
            self.character.main_class, self.config
        )
        race_musical_instrument_proficiencies = list(
            filter(tool_type.__instancecheck__, main_class.tools)
        )
        background_musical_instrument_proficiencies = list(
            filter(tool_type.__instancecheck__, background_stats.tools)
        )
        main_class_musical_instrument_proficiencies = list(
            filter(tool_type.__instancecheck__, race_stats.tool_proficiencies)
        )
        all_proficiencies = (
            race_musical_instrument_proficiencies
            + background_musical_instrument_proficiencies
            + main_class_musical_instrument_proficiencies
        )
        obligatory = set(
            filterfalse(tool_type.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies)
        )
        n_additional = sum(
            map(tool_type.ANY_OF_YOUR_CHOICE.__eq__, all_proficiencies)
        )
        rest = Enum(
            "MusicalInstrumentProficiency",
            {
                tool.value.upper().replace(" ", ""): tool.value
                for tool in tool_type
                if tool not in obligatory
            },
        )
        additional = list()
        if n_additional:
            field_names = tuple(
                f"musical_instrument_proficiency{i + 1}"
                for i in range(n_additional)
            )
            tool_template = create_model(
                "MusicalInstrumentProficiencies",
                **{name: (rest, ...) for name in field_names},
            )
            tool_llm = self.llm.with_structured_output(tool_template)
            additional = attrgetter(*field_names)(
                tool_llm.invoke(
                    "Given the description of character pick suitable musical "
                    "instrument proficiencies.\n\nDescription:\n\n"
                    + self.character.model_dump_json(indent=2)
                )
            )

        self._musical_instrument_proficiencies = list(
            obligatory.union(always_iterable(additional))
        )
        return self._musical_instrument_proficiencies

    @property
    def languages(self) -> list[Language]:
        if self._languages:
            return self._languages
        race_stats = sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        )
        background_stats = background2stats(
            self.character.background, self.config
        )
        main_class_languages = {
            MainClass.DRUID: [Language.DRUIDIC],
            MainClass.ROGUE: [Language.THIEVES_CANT],
        }.get(self.character.main_class, [])
        background_languages = background_stats.languages
        race_languages = race_stats.languages
        all_languages = (
            race_languages + background_languages + main_class_languages
        )
        obligatory = set(
            filterfalse(Language.ANY_OF_YOUR_CHOICE.__eq__, all_languages)
        )
        n_additional = sum(
            map(Language.ANY_OF_YOUR_CHOICE.__eq__, all_languages)
        )

        additional = list()
        if n_additional:
            field_names = tuple(
                f"language{i + 1}" for i in range(n_additional)
            )
            language_template = create_model(
                "Languages", **{name: (Language, ...) for name in field_names}
            )
            language_llm = self.llm.with_structured_output(language_template)
            additional = attrgetter(*field_names)(
                language_llm.invoke(
                    "Given the description of character pick suitable know "
                    f"language. Already known languages are "
                    f"{', '.join(o.value for o in obligatory)} "
                    "you are forbidden to pick them.\n\nDescription:\n\n"
                    + self.character.model_dump_json(indent=2)
                )
            )
        additional = always_iterable(additional)
        self._languages = list(obligatory.union(additional))
        return self._languages

    @property
    def passive_perception(self) -> int:
        return self.skill_modifiers[Skill.PERCEPTION] + 10

    @property
    def initiative(self) -> int:
        return self.modifiers[Statistic.DEXTERITY]

    @property
    def speed(self) -> int:
        return sub_race2stats(
            self.character.main_race, self.character.sub_race, self.config
        ).speed

    @property
    def hit_die(self) -> int:
        return class2hit_die[self.character.main_class]

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
            order = iter(attributes_in_order)
            for stat in order:
                if stat in race_attributes:
                    continue
                if race_attributes["any_of_your_choice"] == 2:
                    self._attributes[stat] += 1
                    self._attributes[next(order)] += 1
                else:
                    self._attributes[stat] += 1
                break
        for feat in self.feats:
            if feat == Feat.ABILITY_SCORE_IMPROVEMENT:
                self._improve_from_ability_score(attributes_in_order)
            elif feat == Feat.RESILIENT:
                _ = self.saving_throw_proficiencies
                important_saves = (
                    Statistic.DEXTERITY,
                    Statistic.CONSTITUTION,
                    Statistic.WISDOM,
                )
                important_saves = tuple(
                    filterfalse(
                        self._saving_throws.__contains__, important_saves
                    )
                )
                attributes_in_order = tuple(
                    filter(
                        important_saves.__contains__,
                        self._reduce_attributes_in_order(attributes_in_order),
                    )
                )
                if attributes_in_order:
                    self._attributes[attributes_in_order[0]] += 1
                    self._saving_throws.append(attributes_in_order[0])
                else:
                    raise ValueError
            elif (
                self._feat2feat_template(feat).attribute_increase
                == StatisticAndAny.ANY_OF_YOUR_CHOICE
            ):
                attributes_in_order = self._reduce_attributes_in_order(
                    attributes_in_order
                )
                if attributes_in_order:
                    self._attributes[attributes_in_order[0]] += 1
                else:
                    raise ValueError
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
    def modifiers(self) -> dict[Statistic, int]:
        return {key: value // 2 - 5 for key, value in self.attributes.items()}

    @property
    def saving_throw_modifiers(self) -> dict[Statistic, int]:
        return {
            key: value
            + self.proficiency_bonus * (key in self.saving_throw_proficiencies)
            for key, value in self.modifiers.items()
        }

    @property
    def proficiency_bonus(self) -> int:
        return (self.character.level - 1) // 4 + 2

    @property
    def feats(self) -> list[Feat]:
        if self._feats:
            return self._feats
        ability_score_improvements = main_class2ability_score_improvements[
            self.character.main_class
        ]
        n_improvements = 0
        for n_improvements, level_required in enumerate(
            ability_score_improvements
        ):
            if level_required > self.character.level:
                break
        n_improvements += self._race_stats.additional_feat
        self._feats = list(
            islice(
                chain.from_iterable(
                    (
                        self.character.feats,
                        repeat(Feat.ABILITY_SCORE_IMPROVEMENT),
                    )
                ),
                n_improvements,
            )
        )
        return self._feats

    @property
    def equipment(self) -> list[Item]:
        if self._equipment:
            return self._equipment
        character_gold = (
            self.character.amount_of_gold_for_equipment or sys.maxsize
        )
        armor = next(
            armor for armor in armor_list if armor.name == self.character.armor
        )
        if armor.cost > character_gold:
            self._equipment = [armor_list[0]]  # clothes
        else:
            character_gold -= armor.cost
            self._equipment = [armor]
        if (
            self.character.uses_shield
            and armor_list[-1].cost <= character_gold
        ):
            self._equipment.append(armor_list[-1])
            character_gold -= armor_list[-1].cost
        for weapon_name in self.character.weapons:
            weapon = next(
                weapon for weapon in weapon_list if weapon.name == weapon_name
            )
            if weapon.cost > character_gold:
                continue
            character_gold -= weapon.cost
            self._equipment.append(weapon)
        return self._equipment

    @property
    def uses_shield(self):
        return self.character.uses_shield and armor_list[-1] in self.equipment

    @property
    def weapons(self) -> list[Weapon]:
        return list(filter(Weapon.__instancecheck__, self.equipment))

    @property
    def capacity(self) -> int:
        return 15 * self.attributes[Statistic.STRENGTH]

    @property
    def additional_attack(self) -> list[str]:
        return []

    @property
    def spellcasting_ability(self) -> Optional[Statistic]:
        return spellcasting_ability_map.get(self.character.main_class)

    @property
    def spellsave_dc(self) -> int:
        if self.spellcasting_ability is None:
            return 0
        return (
            8
            + self.proficiency_bonus
            + self.modifiers[self.spellcasting_ability]
        )

    @property
    def spell_attack_bonus(self) -> int:
        if self.spellcasting_ability is None:
            return 0
        return self.spellcasting_modifier + self.proficiency_bonus

    @property
    def spellcasting_modifier(self) -> int:
        return self.modifiers.get(self.spellcasting_ability, 0)

    @property
    def spell_slots(self) -> tuple[int, ...]:
        return main_class2spell_slots[self.character.main_class][
            self.character.level
        ]

    @property
    def saving_throw_proficiencies(self) -> list[Statistic]:
        if self._saving_throws:
            return self._saving_throws
        self._saving_throws = list(
            main_class2saving_throws[self.character.main_class]
        )
        return self._saving_throws

    @property
    def battle_maneuvers(self) -> dict[BattleManeuver, AbilityTemplate]:
        if self._battle_maneuvers:
            return self._battle_maneuvers
        n_maneuvers = get_n_maneuvers(self)
        if not n_maneuvers:
            self._battle_maneuvers = {}
            return self._battle_maneuvers
        battle_maneuver_fields = tuple(
            f"battle_maneuver{i}" for i in range(1, 1 + n_maneuvers)
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
        self._battle_maneuvers = {
            maneuver: maneuver2ability[maneuver]
            for maneuver in picked_maneuvers
        }
        return self._battle_maneuvers

    @property
    def eldritch_invocations(self) -> dict[str, str]:
        if self._eldritch_invocations:
            return self._eldritch_invocations
        n_invocations = n_eldrich_invocations(self)
        if not n_invocations:
            return {}
        eldritch_invocation_fields = tuple(
            f"eldritch_invocation{i}" for i in range(1, 1 + n_invocations)
        )
        invocation = Enum(
            "Invocation",
            {
                invocation.name.upper().replace(" ", "_"): invocation.name
                for invocation in invocations
                if invocation.required_level <= self.character.level
                and (
                    invocation.pact is None
                    or invocation.pact == self.character.warlock_pact
                )
            },
        )
        fields_dictionary = {
            field_name: (invocation, ...)
            for field_name in eldritch_invocation_fields
        }
        invocations_model = create_model(
            "EldritchInvocations",
            **fields_dictionary,
            __base__=BaseModel,
        )
        eldritch_invocations_llm = self.llm.with_structured_output(
            invocations_model
        )
        eldritch_invocations = attrgetter(*eldritch_invocation_fields)(
            eldritch_invocations_llm.invoke(
                "Given the description of character pick suitable eldritch "
                "invocations.\n\nDescription:\n\n"
                + self.character.model_dump_json(indent=2)
            )
        )
        self._eldritch_invocations = {
            invocation.value: next(
                invocation.description
                for invocation in invocations
                if invocation.name == invocation.value
            )
            for invocation in eldritch_invocations
        }
        return self._eldritch_invocations

    @property
    def fighting_styles(self) -> dict[FightingStyle, AbilityTemplate]:
        if self._fighting_styles:
            return self._fighting_styles
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
                f"Given the description of character pick suitable battle "
                f"maneuvers.\n\nDescription:\n\n"
                f"{self.character.model_dump_json(indent=2)}"
            )
        )
        self._fighting_styles = {
            style: fighting_style2ability[style]
            for style in (
                [picked_styles]
                if isinstance(picked_styles, FightingStyle)
                else picked_styles
            )
        }
        return self._fighting_styles

    @property
    def action_abilities(self) -> list[str]:
        check_valid = partial(
            self._ability_valid, type_checker=AbilityType.ACTION.__eq__
        )
        return self._get_abilities(check_valid)

    @property
    def bonus_action_abilities(self) -> list[str]:
        check_valid = partial(
            self._ability_valid, type_checker=AbilityType.BONUS_ACTION.__eq__
        )
        return self._get_abilities(check_valid)

    @property
    def reaction_abilities(self) -> list[str]:
        check_valid = partial(
            self._ability_valid, type_checker=AbilityType.REACTION.__eq__
        )
        return self._get_abilities(check_valid)

    @property
    def free_action_abilities(self) -> list[str]:
        check_valid = partial(
            self._ability_valid, type_checker=AbilityType.FREE_ACTION.__eq__
        )
        return self._get_abilities(check_valid)

    @property
    def passive_abilities(self) -> list[str]:
        check_valid = partial(
            self._ability_valid, type_checker=AbilityType.PASSIVE.__eq__
        )
        return self._get_abilities(check_valid)

    @property
    def ac(self):
        armor = next(
            filter(Armor.__instancecheck__, self.equipment), armor_list[0]
        )
        modifier = self.attributes[Statistic.DEXTERITY] // 2 - 5
        if armor.category == ArmorCategory.HEAVY:
            bonus = 0
        elif armor.category == ArmorCategory.MEDIUM:
            bonus = min(2, modifier)
        else:
            bonus = modifier
            if self.character.main_class == MainClass.MONK:
                bonus += self.attributes[Statistic.WISDOM] // 2 - 5
            elif self.character.main_class == MainClass.BARBARIAN:
                bonus += self.attributes[Statistic.CONSTITUTION] // 2 - 5
        no_abilities = armor.base_ac + bonus
        if self.character.main_race == MainRace.LIZARDFOLK:
            no_abilities = max(no_abilities, 13 + modifier)
        defense = int(
            armor.category != ArmorCategory.NONE
            and FightingStyle.DEFENSE in self.fighting_styles
        )
        return no_abilities + 2 * self.uses_shield + defense

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
        self, attributes_in_order: Sequence[Statistic]
    ) -> Sequence[Statistic]:
        while (
            attributes_in_order
            and self._attributes[attributes_in_order[0]] == 20
        ):
            attributes_in_order = attributes_in_order[1:]
        return attributes_in_order

    def _ability_valid(
        self,
        ability: AbilityTemplate,
        type_checker: Callable[[AbilityType], bool],
    ) -> bool:
        return (
            ability
            and type_checker(ability.ability_type)
            and ability.combat_related
            and ability.required_level <= self.character.level
        )

    def _get_abilities(
        self, check_valid: Callable[[AbilityTemplate], bool]
    ) -> list[str]:
        abilities = []
        for feat in filterfalse(
            Feat.ABILITY_SCORE_IMPROVEMENT.__eq__, self.feats
        ):
            ability = self._feat2feat_template(feat).ability
            if check_valid(ability):
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
            if check_valid(ability):
                abilities.append(ability.description)
        for (
            main_class_ability_path
        ) in self.config.main_class_abilities_root.joinpath(
            self.character.main_class
        ).iterdir():
            ability = AbilityTemplate(
                **json.loads(main_class_ability_path.read_text())
            )
            if check_valid(ability):
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
            if check_valid(ability):
                abilities.append(ability.description)
        for maneuver in self.battle_maneuvers.values():
            if check_valid(maneuver):
                abilities.append(maneuver.description)
        for fighting_style in self.fighting_styles.values():
            if check_valid(fighting_style):
                abilities.append(fighting_style.description)
        return abilities

    def is_proficient_with(self, weapon: Weapon) -> bool:
        return True

    @property
    def n_prepared_spells(self):
        return bool(self.character.spells_by_level[1]) * (
            self.character.level + max(0, self.spellcasting_modifier)
        )

    @property
    def prepared_spells(self) -> list[Spell]:
        if self._prepared_spells:
            return self._prepared_spells
        if not (n_prepared_spells := self.n_prepared_spells):
            return []
        known_spells = chain.from_iterable(self.character.spells_by_level[1:])
        KnownSpell = Enum(
            "KnownSpell",
            {
                spell.value.upper().replace(" ", "_"): spell.value
                for spell in known_spells
            },
        )
        prepared_spells = create_model(
            "PreparedSpells",
            prepared_spells=(
                list[KnownSpell],
                Field(
                    description="Spells from options "
                    "for D&D character to have prepared"
                ),
            ),
            __base__=BaseModel,
        )
        prepared_spells_llm = self.llm.with_structured_output(prepared_spells)
        self._prepared_spells = prepared_spells_llm.invoke(
            f"Given the description of character pick suitable spells he has "
            f"prepared. Choose exactly {n_prepared_spells}. "
            f"\n\nDescription:\n\n{self.character.model_dump_json(indent=2)}"
        ).prepared_spells
        return self._prepared_spells
