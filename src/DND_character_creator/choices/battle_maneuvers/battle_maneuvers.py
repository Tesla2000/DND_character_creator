# flake8: noqa E501
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from src.DND_character_creator.choices.abilities.AbilityType import AbilityType
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilityTemplate,
)

if TYPE_CHECKING:
    from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.choices.class_creation.character_class import (
    FighterSubclass,
)
from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.fighting_styles.fighting_styles import (
    FightingStyle,
)
from src.DND_character_creator.feats import Feat


class BattleManeuver(str, Enum):
    AMBUSH = "Ambush"
    BAIT_AND_SWITCH = "Bait and Switch"
    BRACE = "Brace"
    COMMANDERS_STRIKE = "Commander's Strike"
    COMMANDING_PRESENCE = "Commanding Presence"
    DISARMING_ATTACK = "Disarming Attack"
    DISTRACTING_STRIKE = "Distracting Strike"
    EVASIVE_FOOTWORK = "Evasive Footwork"
    FEINTING_ATTACK = "Feinting Attack"
    GOADING_ATTACK = "Goading Attack"
    GRAPPLING_STRIKE = "Grappling Strike"
    LUNGING_ATTACK = "Lunging Attack"
    MANEUVERING_ATTACK = "Maneuvering Attack"
    MENACING_ATTACK = "Menacing Attack"
    PARRY = "Parry"
    PRECISION_ATTACK = "Precision Attack"
    PUSHING_ATTACK = "Pushing Attack"
    QUICK_TOSS = "Quick Toss"
    RALLY = "Rally"
    RIPOSTE = "Riposte"
    SWEEPING_ATTACK = "Sweeping Attack"
    TACTICAL_ASSESSMENT = "Tactical Assessment"
    TRIP_ATTACK = "Trip Attack"


maneuver2ability = {
    BattleManeuver.AMBUSH: AbilityTemplate(
        description="When you make a Dexterity (Stealth) check or an "
        "initiative roll, you can expend one superiority die "
        "and add the die to the roll, provided you aren't incapacitated.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.BAIT_AND_SWITCH: AbilityTemplate(
        description="When you're within 5 feet of a creature on your turn, you can expend"
        " one superiority die and switch places with that creature, provided you spend at least 5 feet of movement and the"
        " creature is willing and isn't incapacitated. This movement doesn't provoke opportunity attacks.\n"
        "Roll the superiority die. Until the start of your next turn, you or the other creature (your choice) gains a bonus "
        "to AC equal to the number rolled.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.BRACE: AbilityTemplate(
        description="When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction "
        "to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the "
        "superiority die to the weapon's damage roll.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.COMMANDERS_STRIKE: AbilityTemplate(
        description="When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of "
        "your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. "
        "That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.",
        ability_type=AbilityType.BONUS_ACTION,
    ),
    BattleManeuver.COMMANDING_PRESENCE: AbilityTemplate(
        description="When you make a Charisma (Intimidation), a Charisma (Performance), "
        "or a Charisma (Persuasion) check, you can expend one superiority "
        "die and add the superiority die to the ability check.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.DISARMING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to attempt to disarm the target, forcing it to "
        "drop one item of your choice that it's holding. You add the "
        "superiority die to the attack's damage roll, and the target must "
        "make a Strength saving throw. On a failed save, it drops the object "
        "you choose. The object lands at its feet.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.DISTRACTING_STRIKE: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to distract the creature, giving your allies an "
        "opening. You add the superiority die to the attack's damage roll. The next "
        "attack roll against the target by an attacker other than you has "
        "advantage if the attack is made before the start of your next turn.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.EVASIVE_FOOTWORK: AbilityTemplate(
        description="When you move, you can expend one superiority die, rolling the die "
        "and adding the number rolled to your AC until you stop moving.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.FEINTING_ATTACK: AbilityTemplate(
        description="You can expend one superiority die and use a bonus action on your "
        "turn to feint, choosing one creature within 5 feet of you as your target. "
        "You have advantage on your next attack roll against that creature "
        "this turn. If that attack hits, add the superiority die to the "
        "attack's damage roll.",
        ability_type=AbilityType.BONUS_ACTION,
    ),
    BattleManeuver.GOADING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to attempt to goad the target into attacking you. "
        "You add the superiority die to the attack's damage roll, and the target must make "
        "a Wisdom saving throw. On a failed save, the target has disadvantage on all attack "
        "rolls against targets other than you until the end of your next turn.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.GRAPPLING_STRIKE: AbilityTemplate(
        description="Immediately after you hit a creature with a melee attack on your "
        "turn, you can expend one superiority die and then try to grapple the target as a bonus action. "
        "Add the superiority die to your Strength (Athletics) check.",
        ability_type=AbilityType.BONUS_ACTION,
    ),
    BattleManeuver.LUNGING_ATTACK: AbilityTemplate(
        description="When you make a melee weapon attack on your turn, you can expend one"
        " superiority die to increase your reach for that attack by 5 feet. "
        "If you hit, you add the superiority die to the attack's damage roll.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.MANEUVERING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to maneuver one of your comrades into a more advantageous position. "
        "You add the superiority die to the attack's damage roll, and you "
        "choose a friendly creature who can see or hear you. That creature "
        "can use its reaction to move up to half its speed without provoking opportunity attacks "
        "from the target of your attack.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.MENACING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to attempt to frighten the target. You add the "
        "superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. "
        "On a failed save, it is frightened of you until the end of your next turn.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.PARRY: AbilityTemplate(
        description="When another creature damages you with a melee attack, you can use "
        "your reaction and expend one superiority die to reduce the damage by "
        "the number you roll on your superiority die + your Dexterity modifier.",
        ability_type=AbilityType.REACTION,
    ),
    BattleManeuver.PRECISION_ATTACK: AbilityTemplate(
        description="When you make a weapon attack roll against a creature, you can expend "
        "one superiority die to add it to the roll. You can use this maneuver "
        "before or after making the attack roll, but before any effects of the attack are applied.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.PUSHING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can expend one "
        "superiority die to attempt to drive the target back. You add the "
        "superiority die to the attack's damage roll, and if the target is Large or smaller, "
        "it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.QUICK_TOSS: AbilityTemplate(
        description="As a bonus action, you can expend one superiority die and make a "
        "ranged attack with a weapon that has the thrown property. You can draw the weapon as part of making this attack. "
        "If you hit, add the superiority die to the weapon's damage roll.",
        ability_type=AbilityType.BONUS_ACTION,
    ),
    BattleManeuver.RALLY: AbilityTemplate(
        description="On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. "
        "When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the "
        "superiority die roll + your Charisma modifier.",
        ability_type=AbilityType.BONUS_ACTION,
    ),
    BattleManeuver.RIPOSTE: AbilityTemplate(
        description="When a creature misses you with a melee attack, you can use your "
        "reaction and expend one superiority die to make a melee weapon "
        "attack against the creature. If you hit, you add the superiority die to the attack's damage roll.",
        ability_type=AbilityType.REACTION,
    ),
    BattleManeuver.SWEEPING_ATTACK: AbilityTemplate(
        description="When you hit a creature with a melee weapon attack, you can expend "
        "one superiority die to attempt to damage another creature with the "
        "same attack. Choose another creature within 5 feet of the original "
        "target and within your reach. If the original attack roll would hit "
        "the second creature, it takes damage equal to the number you roll on "
        "your superiority die. The damage is of the same type dealt by the "
        "original attack.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.TACTICAL_ASSESSMENT: AbilityTemplate(
        description="When you make an Intelligence (Investigation), an "
        "Intelligence (History), or a Wisdom (Insight) check, you can expend "
        "one superiority die and add the superiority die to the ability check.",
        ability_type=AbilityType.FREE_ACTION,
    ),
    BattleManeuver.TRIP_ATTACK: AbilityTemplate(
        description="When you hit a creature with a weapon attack, you can "
        "expend one superiority die to attempt to knock the target down. You "
        "add the superiority die to the attack's damage roll, and if the "
        "target is Large or smaller, it must make a Strength saving throw. "
        "On a failed save, you knock the target prone.",
        ability_type=AbilityType.FREE_ACTION,
    ),
}


def get_n_maneuvers(character_wrapper: "CharacterWrapper") -> int:
    conditions = [
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 3,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 7,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 10,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 15,
        lambda character_wrapper: character_wrapper.character.main_class
        == MainClass.FIGHTER
        and character_wrapper.character.sub_class
        == FighterSubclass.BATTLE_MASTER
        and character_wrapper.character.level >= 15,
        lambda character_wrapper: FightingStyle.SUPERIOR_TECHNIQUE
        in character_wrapper.fighting_styles,
        lambda character_wrapper: Feat.MARTIAL_ADEPT
        in character_wrapper.feats,
        lambda character_wrapper: Feat.MARTIAL_ADEPT
        in character_wrapper.feats,
    ]
    return sum(condition(character_wrapper) for condition in conditions)
