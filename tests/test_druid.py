# flake8: noqa E501
from __future__ import annotations

from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.choices.equipment_creation.armor import Armor
from src.DND_character_creator.choices.equipment_creation.armor import (
    ArmorCategory,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.weapons import (
    DamageType,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.weapons import (
    HitDieSize,
)  # noqa: E501
from src.DND_character_creator.choices.equipment_creation.weapons import Weapon
from src.DND_character_creator.choices.equipment_creation.weapons import (
    WeaponName,
)  # noqa: E501
from src.DND_character_creator.choices.language import Language
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.config import Config
from src.DND_character_creator.config import create_config_with_args
from src.DND_character_creator.config import parse_arguments
from src.DND_character_creator.feats import Feat
from src.DND_character_creator.pdf_creator.create_pdf import create_pdf
from src.DND_character_creator.skill_proficiency import Skill
from src.DND_character_creator.wiki_scraper.MainRaceTemplate import Statistics
from src.DND_character_creator.wiki_scraper.MainRaceTemplate import (
    SubRaceTemplate,
)


def test():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    llm = None
    character_full = CharacterFull(
        **{
            "sex": "male",
            "backstory": "",
            "level": 18,
            "age": 70,
            "main_class": "Druid",
            "first_most_important_stat": "wisdom",
            "second_most_important_stat": "constitution",
            "third_most_important_stat": "intelligence",
            "forth_most_important_stat": "strength",
            "fifth_most_important_stat": "dexterity",
            "sixth_most_important_stat": "charisma",
            "main_race": "Lizardfolk",
            "name": "Grix",
            "background": "Hermit",
            "alignment": "true_neutral",
            "height": 180,
            "weight": 90,
            "eye_color": "yellow",
            "skin_color": "green",
            "hairstyle": "none",
            "appearance": "An old lizardfolk with deep scales and a wise gaze, wearing tattered robes adorned with natural motifs and carrying a gnarled staff.",
            "character_traits": "Calm, insightful, and deeply connected to the swamps, often speaks in riddles.",
            "ideals": "Harmony with nature and respect for all living things.",
            "bonds": "Protects the swamp and its creatures as his family.",
            "weaknesses": "Overly trusting of nature, sometimes neglects the dangers posed by outsiders.",
            "amount_of_gold_for_equipment": 9223372036854775807,
            "cantrips": [
                "Druidcraft",
                "Guidance",
                "Produce Flame",
                "Thorn Whip",
                "Control Flames",
                "Mending",
            ],
            "first_level_spells": [
                "Goodberry",
                "Cure Wounds",
                "Entangle",
                "Detect Magic",
                "Fog Cloud",
                "Thunderwave",
            ],
            "second_level_spells": [
                "Moonbeam",
                "Healing Spirit",
                "Pass Without Trace",
                "Flame Blade",
                "Dust Devil",
                "Barkskin",
            ],
            "third_level_spells": [
                "Call Lightning",
                "Conjure Animals",
                "Plant Growth",
                "Protection from Energy",
                "Dispel Magic",
                "Daylight",
            ],
            "fourth_level_spells": [
                "Blight",
                "Conjure Woodland Beings",
                "Control Water",
                "Ice Storm",
                "Polymorph",
                "Guardian of Nature",
            ],
            "fifth_level_spells": [
                "Awaken",
                "Greater Restoration",
                "Insect Plague",
                "Tree Stride",
                "Commune with Nature",
                "Mass Cure Wounds",
            ],
            "sixth_level_spells": [
                "Heal",
                "Find the Path",
                "Druid Grove",
                "Transport via Plants",
                "Wall of Thorns",
                "Primordial Ward",
            ],
            "seventh_level_spells": [
                "Regenerate",
                "Fire Storm",
                "Plane Shift",
                "Mirage Arcane",
                "Whirlwind",
                "Draconic Transformation",
            ],
            "eighth_level_spells": [
                "Earthquake",
                "Control Weather",
                "Animal Shapes",
                "Sunburst",
                "Feeblemind",
                "Tsunami",
            ],
            "ninth_level_spells": [
                "Shapechange",
                "Storm of Vengeance",
                "True Resurrection",
                "Foresight",
            ],
            "feats": ["Ability Score Improvement", "War Caster", "Observant"],
            "sub_race": "Lizardfolk",
            "sub_class": "Circle of the Land",
            "warlock_pact": None,
            "armor": "Clothes",
            "uses_shield": False,
            "weapons": ["Quarterstaff", "Dagger", "Spear"],
        }
    )
    character_wrapped = CharacterWrapper(character_full, config, llm)
    character_wrapped.__dict__.update(
        {
            "_character_details": None,
            "_feats": [
                Feat.ABILITY_SCORE_IMPROVEMENT,
                Feat.WAR_CASTER,
                Feat.OBSERVANT,
                Feat.ABILITY_SCORE_IMPROVEMENT,
            ],
            "_attributes": {
                Statistic.WISDOM: 20,
                Statistic.CONSTITUTION: 16,
                Statistic.INTELLIGENCE: 14,
                Statistic.STRENGTH: 12,
                Statistic.DEXTERITY: 10,
                Statistic.CHARISMA: 8,
            },
            "_health": 147,
            "_prepared_spells": [
                "Goodberry",
                "Cure Wounds",
                "Entangle",
                "Detect Magic",
                "Fog Cloud",
                "Thunderwave",
                "Moonbeam",
                "Healing Spirit",
                "Pass Without Trace",
                "Call Lightning",
                "Conjure Animals",
                "Plant Growth",
                "Polymorph",
                "Guardian of Nature",
                "Awaken",
                "Greater Restoration",
                "Insect Plague",
                "Tree Stride",
                "Druid Grove",
                "Regenerate",
                "Fire Storm",
                "Control Weather",
                "Shapechange",
            ],
            "_race_stats": SubRaceTemplate(
                name="Lizardfolk",
                speed=30,
                darkvision_range=0,
                languages=[Language.COMMON, Language.DRACONIC],
                skill_proficiencies=[
                    Skill.ANIMAL_HANDLING,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.STEALTH,
                    Skill.SURVIVAL,
                ],
                tool_proficiencies=[],
                additional_feat=False,
                statistics=Statistics(
                    strength=0,
                    dexterity=0,
                    constitution=2,
                    intelligence=0,
                    wisdom=1,
                    charisma=0,
                    any_of_your_choice=0,
                ),
                other_active_abilities=[
                    "Bite",
                    "Cunning Artisan",
                    "Hold Breath",
                    "Hunter's Lore",
                    "Natural Armor",
                    "Hungry Jaws",
                ],
            ),
            "_eldritch_invocations": None,
            "_fighting_styles": None,
            "_battle_maneuvers": {},
            "_saving_throws": [Statistic.INTELLIGENCE, Statistic.WISDOM],
            "_equipment": [
                Armor(
                    name="Clothes",
                    cost=0.0,
                    weight=0,
                    category=ArmorCategory.NONE,
                    disadvantage_on_stealth=False,
                    base_ac=10,
                ),
                Weapon(
                    name=WeaponName.QUARTERSTAFF,
                    cost=2.0,
                    weight=4.0,
                    damage_type=DamageType.BLUDGEONING,
                    base_hit_die=HitDieSize.SIX,
                    two_dies=False,
                    is_martial=False,
                    is_ammunition=False,
                    is_finesse=False,
                    is_heavy=False,
                    is_light=False,
                    is_range=False,
                    is_reach=False,
                    is_special=False,
                    is_thrown=False,
                    is_two_handed=False,
                    is_versatile=True,
                ),
                Weapon(
                    name=WeaponName.DAGGER,
                    cost=2.0,
                    weight=1.0,
                    damage_type=DamageType.PIERCING,
                    base_hit_die=HitDieSize.FOUR,
                    two_dies=False,
                    is_martial=False,
                    is_ammunition=False,
                    is_finesse=True,
                    is_heavy=False,
                    is_light=True,
                    is_range=True,
                    is_reach=False,
                    is_special=False,
                    is_thrown=True,
                    is_two_handed=False,
                    is_versatile=False,
                ),
                Weapon(
                    name=WeaponName.SPEAR,
                    cost=1.0,
                    weight=3.0,
                    damage_type=DamageType.PIERCING,
                    base_hit_die=HitDieSize.SIX,
                    two_dies=False,
                    is_martial=False,
                    is_ammunition=False,
                    is_finesse=False,
                    is_heavy=False,
                    is_light=False,
                    is_range=True,
                    is_reach=False,
                    is_special=False,
                    is_thrown=True,
                    is_two_handed=False,
                    is_versatile=True,
                ),
            ],
        }
    )
    create_pdf(character_wrapped, character_full, config)


if __name__ == "__main__":
    exit(test())
