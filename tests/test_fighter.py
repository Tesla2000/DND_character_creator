# flake8: noqa E501
from __future__ import annotations

from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.choices.abilities.AbilityType import AbilityType
from src.DND_character_creator.choices.battle_maneuvers.battle_maneuvers import (  # noqa: E501
    BattleManeuver,
)
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    FightingStyle,
)
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.config import Config
from src.DND_character_creator.config import create_config_with_args
from src.DND_character_creator.config import parse_arguments
from src.DND_character_creator.feats import Feat
from src.DND_character_creator.pdf_creator.create_pdf import create_pdf
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilityTemplate,
)


def test():
    args = parse_arguments(Config)
    config = create_config_with_args(Config, args)
    llm = None
    character_full = CharacterFull(
        **{
            "sex": "male",
            "backstory": "Born into a family of blacksmiths, Thrain was always surrounded by the clang of metal and the heat of the forge. From a young age, he was taught the importance of strength and resilience, not just in crafting weapons, but in life itself. When his village was threatened by marauding bandits, Thrain took up arms to protect his home. He quickly became known for his unwavering defense and his ability to absorb blows that would fell lesser warriors. After successfully driving away the bandits, he decided to dedicate his life to becoming a master of heavy armor and shield techniques. Now, he travels the land, seeking to hone his skills in battle and defend those who cannot protect themselves. His heart is as strong as the steel he wields, and he believes that true strength lies in protecting others.",
            "level": 5,
            "age": 30,
            "main_class": "Fighter",
            "first_most_important_stat": "constitution",
            "second_most_important_stat": "strength",
            "third_most_important_stat": "dexterity",
            "forth_most_important_stat": "wisdom",
            "fifth_most_important_stat": "charisma",
            "sixth_most_important_stat": "intelligence",
            "main_race": "Dwarf",
            "name": "Thrain Ironshield",
            "background": "Soldier",
            "alignment": "lawful_good",
            "height": 180,
            "weight": 100,
            "eye_color": "blue",
            "skin_color": "light",
            "hairstyle": "short and braided",
            "appearance": "Thrain is a stout dwarf with a broad chest and muscular arms, showcasing years of hard work and combat training. His heavy armor is polished to a shine, adorned with intricate engravings of his family crest. He carries a large shield, always at the ready, and his braided beard flows down to his chest, giving him a fierce but noble appearance.",
            "character_traits": "Thrain is fiercely loyal to his friends and allies, often putting their safety above his own. He has a strong sense of justice and will not stand by while the innocent are harmed.",
            "ideals": "Protection: It is my duty to protect those who cannot protect themselves, no matter the cost.",
            "bonds": "I will always defend my homeland and the people I love, even if it means facing overwhelming odds.",
            "weaknesses": "He can be overly stubborn at times, refusing to back down even when it may be wiser to retreat.",
            "amount_of_gold_for_equipment": 9223372036854775807,
            "cantrips": [],
            "first_level_spells": [],
            "second_level_spells": [],
            "third_level_spells": [],
            "feats": ["Tough", "Resilient", "Shield Master"],
            "sub_race": "Mountain Dwarf",
            "sub_class": "Battle Master",
            "warlock_pact": None,
            "armor": "Plate",
            "uses_shield": True,
            "weapons": ["Battleaxe", "Warhammer", "Longsword"],
        }
    )
    character_wrapped = CharacterWrapper(character_full, config, llm)
    character_wrapped.__dict__.update(
        {
            "_attributes": {
                Statistic("charisma"): 10,
                Statistic("constitution"): 17,
                Statistic("dexterity"): 13,
                Statistic("intelligence"): 8,
                Statistic("strength"): 16,
                Statistic("wisdom"): 12,
            },
            "_feats": [Feat("Tough")],
            "_fighting_styles": {
                FightingStyle("Defense"): AbilityTemplate(
                    name="",
                    ability_type=AbilityType("passive"),
                    combat_related=True,
                    spell_grant=False,
                    description="While you are wearing armor, you gain a +1 bonus to AC.",
                    required_level=0,
                )
            },
            "_battle_maneuvers": {
                BattleManeuver("Brace"): AbilityTemplate(
                    name="",
                    ability_type=AbilityType("free_action"),
                    combat_related=True,
                    spell_grant=False,
                    description="When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the superiority die to the weapon's damage roll.",
                    required_level=0,
                ),
                BattleManeuver("Commander's Strike"): AbilityTemplate(
                    name="",
                    ability_type=AbilityType("bonus_action"),
                    combat_related=True,
                    spell_grant=False,
                    description="When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.",
                    required_level=0,
                ),
                BattleManeuver("Parry"): AbilityTemplate(
                    name="",
                    ability_type=AbilityType("reaction"),
                    combat_related=True,
                    spell_grant=False,
                    description="When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier.",
                    required_level=0,
                ),
            },
        }
    )
    create_pdf(character_wrapped, character_full, config)


if __name__ == "__main__":
    exit(test())
