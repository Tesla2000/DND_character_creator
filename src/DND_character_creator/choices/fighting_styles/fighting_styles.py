from __future__ import annotations

from enum import Enum

from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.choices.class_creation.character_class import (
    ArtificerSubclass,
)  # noqa: E501
from src.DND_character_creator.choices.class_creation.character_class import (
    BarbarianSubclass,
)  # noqa: E501
from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)  # noqa: E501
from src.DND_character_creator.choices.class_creation.character_class import (
    WarlockSubclass,
)  # noqa: E501
from src.DND_character_creator.feats import Feat


class FightingStyle(str, Enum):
    ARCHERY = "Archery"
    BLIND_FIGHTING = "Blind Fighting"
    DEFENSE = "Defense"
    DUELING = "Dueling"
    GREAT_WEAPON_FIGHTING = "Great Weapon Fighting"
    INTERCEPTION = "Interception"
    PROTECTION = "Protection"
    SUPERIOR_TECHNIQUE = "Superior Technique"
    THROWN_WEAPON_FIGHTING = "Thrown Weapon Fighting"
    TWO_WEAPON_FIGHTING = "Two-Weapon Fighting"
    UNARMED_FIGHTING = "Unarmed Fighting"
    CLOSE_QUARTERS_SHOOTER = "Close Quarters Shooter"
    MARINER = "Mariner"
    TUNNEL_FIGHTER = "Tunnel Fighter"


fighting_style_descriptions = {
    FightingStyle.ARCHERY: "You gain a +2 bonus to attack rolls you make with ranged weapons.",  # noqa: E501
    FightingStyle.BLIND_FIGHTING: "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.",  # noqa: E501
    FightingStyle.DEFENSE: "While you are wearing armor, you gain a +1 bonus to AC.",  # noqa: E501
    FightingStyle.DUELING: "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",  # noqa: E501
    FightingStyle.GREAT_WEAPON_FIGHTING: "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.",  # noqa: E501
    FightingStyle.INTERCEPTION: "When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",  # noqa: E501
    FightingStyle.PROTECTION: "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",  # noqa: E501
    FightingStyle.SUPERIOR_TECHNIQUE: "You learn one maneuver of your choice from among those available to the Battle Master archetype. You gain one superiority die, which is a d6. This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.",  # noqa: E501
    FightingStyle.THROWN_WEAPON_FIGHTING: "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",  # noqa: E501
    FightingStyle.TWO_WEAPON_FIGHTING: "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",  # noqa: E501
    FightingStyle.UNARMED_FIGHTING: "Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.",  # noqa: E501
    FightingStyle.CLOSE_QUARTERS_SHOOTER: "When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.",  # noqa: E501
    FightingStyle.MARINER: "As long as you are not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class.",  # noqa: E501
    FightingStyle.TUNNEL_FIGHTER: "As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.",  # noqa: E501
}


def n_fighting_styles(character_wrapper: CharacterWrapper) -> int:
    conditions = [
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.level >= 10,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.RANGER
        and character_wrapper.character.level >= 2,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.PALADIN
        and character_wrapper.character.level >= 2,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.ARTIFICER
        and character_wrapper.character.sub_class == ArtificerSubclass.ARMORER
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.BARBARIAN
        and character_wrapper.character.sub_class == BarbarianSubclass.BEAST
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.WARLOCK
        and character_wrapper.character.sub_class == WarlockSubclass.HEXBLADE
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: Feat.FIGHTING_INITIATE
        in character_wrapper.feats,
    ]
    return sum(condition(character_wrapper) for condition in conditions)
