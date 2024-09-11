from __future__ import annotations

import string
from itertools import filterfalse
from operator import attrgetter

from more_itertools import roundrobin

from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.choices.stats_creation.statistic import (
    Statistic,
)
from src.DND_character_creator.feats import Feat
from src.DND_character_creator.LatexString import LatexString
from src.DND_character_creator.skill_proficiency import Skill


def update_prototype(
    character_wrapper: CharacterWrapper,
    character_full: CharacterFull,
    prototype: str,
) -> str:
    prototype = LatexString(prototype)
    prototype = prototype.replace("Nende Firiel", character_full.name)
    prototype = prototype.replace(
        "Sorceror 2",
        character_full.main_class + " " + str(character_full.level),
    )
    prototype = prototype.replace("Adopted", character_full.background)
    prototype = prototype.replace("Triton", character_full.sub_race)
    prototype = prototype.replace(
        "Neutral good", character_full.alignment.replace("_", " ").capitalize()
    )

    prototype = prototype.replace(
        "StrengthScore{9",
        "StrengthScore{"
        + str(character_wrapper.attributes[Statistic.STRENGTH]),
    )
    prototype = prototype.replace(
        "DexterityScore{14",
        "DexterityScore{"
        + str(character_wrapper.attributes[Statistic.DEXTERITY]),
    )
    prototype = prototype.replace(
        "ConstitutionScore{14",
        "ConstitutionScore{"
        + str(character_wrapper.attributes[Statistic.CONSTITUTION]),
    )
    prototype = prototype.replace(
        "IntelligenceScore{12",
        "IntelligenceScore{"
        + str(character_wrapper.attributes[Statistic.INTELLIGENCE]),
    )
    prototype = prototype.replace(
        "WisdomScore{10",
        "WisdomScore{" + str(character_wrapper.attributes[Statistic.WISDOM]),
    )
    prototype = prototype.replace(
        "CharismaScore{16",
        "CharismaScore{"
        + str(character_wrapper.attributes[Statistic.CHARISMA]),
    )

    prototype = prototype.replace(
        "StrengthModifier{-1",
        "StrengthModifier{"
        + str(character_wrapper.modifiers[Statistic.STRENGTH]),
    )
    prototype = prototype.replace(
        "DexterityModifier{2",
        "DexterityModifier{"
        + str(character_wrapper.modifiers[Statistic.DEXTERITY]),
    )
    prototype = prototype.replace(
        "ConstitutionModifier{2",
        "ConstitutionModifier{"
        + str(character_wrapper.modifiers[Statistic.CONSTITUTION]),
    )
    prototype = prototype.replace(
        "IntelligenceModifier{1",
        "IntelligenceModifier{"
        + str(character_wrapper.modifiers[Statistic.INTELLIGENCE]),
    )
    prototype = prototype.replace(
        "WisdomModifier{0",
        "WisdomModifier{" + str(character_wrapper.modifiers[Statistic.WISDOM]),
    )
    prototype = prototype.replace(
        "CharismaModifier{3",
        "CharismaModifier{"
        + str(character_wrapper.modifiers[Statistic.CHARISMA]),
    )

    prototype = prototype.replace(
        "StrengthSavingThrowModifier{-1",
        "StrengthSavingThrowModifier{"
        + str(character_wrapper.saving_throw_modifiers[Statistic.STRENGTH]),
    )
    prototype = prototype.replace(
        "DexteritySavingThrowModifier{2",
        "DexteritySavingThrowModifier{"
        + str(character_wrapper.saving_throw_modifiers[Statistic.DEXTERITY]),
    )
    prototype = prototype.replace(
        "ConstitutionSavingThrowModifier{4",
        "ConstitutionSavingThrowModifier{"
        + str(
            character_wrapper.saving_throw_modifiers[Statistic.CONSTITUTION]
        ),
    )
    prototype = prototype.replace(
        "IntelligenceSavingThrowModifier{1",
        "IntelligenceSavingThrowModifier{"
        + str(
            character_wrapper.saving_throw_modifiers[Statistic.INTELLIGENCE]
        ),
    )
    prototype = prototype.replace(
        "WisdomSavingThrowModifier{0",
        "WisdomSavingThrowModifier{"
        + str(character_wrapper.saving_throw_modifiers[Statistic.WISDOM]),
    )
    prototype = prototype.replace(
        "CharismaSavingThrowModifier{5",
        "CharismaSavingThrowModifier{"
        + str(character_wrapper.saving_throw_modifiers[Statistic.CHARISMA]),
    )

    prototype = prototype.replace(
        "SetStrengthProficiency{0",
        "SetStrengthProficiency{"
        + str(int(Statistic.STRENGTH in character_wrapper.saving_throws)),
    )
    prototype = prototype.replace(
        "SetDexterityProficiency{0",
        "SetDexterityProficiency{"
        + str(int(Statistic.DEXTERITY in character_wrapper.saving_throws)),
    )
    prototype = prototype.replace(
        "SetConstitutionProficiency{1",
        "SetConstitutionProficiency{"
        + str(int(Statistic.CONSTITUTION in character_wrapper.saving_throws)),
    )
    prototype = prototype.replace(
        "SetIntelligenceProficiency{0",
        "SetIntelligenceProficiency{"
        + str(int(Statistic.INTELLIGENCE in character_wrapper.saving_throws)),
    )
    prototype = prototype.replace(
        "SetWisdomProficiency{0",
        "SetWisdomProficiency{"
        + str(int(Statistic.WISDOM in character_wrapper.saving_throws)),
    )
    prototype = prototype.replace(
        "SetCharismaProficiency{1",
        "SetCharismaProficiency{"
        + str(int(Statistic.CHARISMA in character_wrapper.saving_throws)),
    )

    prototype = prototype.replace(
        r"\Proficiency{2",
        r"\Proficiency{" + str(character_wrapper.proficiency_bonus),
    )
    prototype = prototype.replace(
        "Perception{10",
        "Perception{"
        + str(character_wrapper.skill_modifiers[Skill.PERCEPTION]),
    )
    prototype = prototype.replace(
        "ArmorClass{12", "ArmorClass{" + str(character_wrapper.ac)
    )
    prototype = prototype.replace(
        "Initiative{2", "Initiative{" + str(character_wrapper.initiative)
    )
    prototype = prototype.replace(
        "Speed{30", "Speed{" + str(character_wrapper.speed)
    )

    prototype = prototype.replace(
        "MaxHitPoints{13", "MaxHitPoints{" + str(character_wrapper.health)
    )
    prototype = prototype.replace(
        "MaxHitDice{2d6",
        "MaxHitDice{" + f"{character_full.level}d{character_wrapper.hit_die}",
    )
    prototype = prototype.replace(
        "CurrentHitDice{",
        "CurrentHitDice{"
        + f"{character_full.level}d{character_wrapper.hit_die}",
    )

    prototype = prototype.replace(
        r"\AddWeapon{Dagger}{+4}{1d4+2/p}",
        "\n".join(
            r"\AddWeapon{"
            + weapon.name
            + "}{"
            + str(weapon.get_attack_bonus(character_wrapper))
            + "}{"
            + weapon.get_damage(character_wrapper)
            + "}"
            for weapon in character_wrapper.weapons
        ),
    )
    prototype = prototype.replace(
        "AttacksAdditional{\n\\textbf{Guiding Bolt}: att. +4, dmg 4d6/r",
        "AttacksAdditional{"
        + "".join(
            "\n" r"\textbf{" + str(additional_attack)
            for additional_attack in character_wrapper.additional_attack
        ),
    )
    prototype = prototype.replace(
        r"OtherProficienciesLanguages{\textbf{Languages:} Elvish, Common, "
        "Primordial",
        r"OtherProficienciesLanguages{\textbf{Languages:} "
        + ", ".join(character_wrapper.languages),
    )
    prototype = prototype.replace(
        r"\textbf{Weapons}: Quarterstaff, Sling, Dart, Dagger, Light Crossbow",
        r"\textbf{Weapons}: "
        + ", ".join(
            map(attrgetter("name"), character_wrapper.weapon_proficiencies)
        ),
    )

    prototype = prototype.replace(
        "Equipment{",
        "Equipment{\n"
        + ", ".join(map(attrgetter("name"), character_wrapper.equipment)),
    )
    prototype = prototype.replace(
        "{Weight:} 82.25 lb",
        "{Weight:} "
        + str(sum(map(attrgetter("weight"), character_wrapper.equipment)))
        + " lb",
    )
    prototype = prototype.replace(
        "{Capacity:} 135 lb",
        "{Capacity:} " + str(character_wrapper.capacity) + " lb",
    )

    prototype = prototype.replace(
        "PersonalityTraits{",
        "PersonalityTraits{\n" + str(character_full.character_traits),
    )
    prototype = prototype.replace(
        "Ideals{", "Ideals{\n" + str(character_full.ideals)
    )
    prototype = prototype.replace(
        "Bonds{", "Bonds{\n" + str(character_full.bonds)
    )
    prototype = prototype.replace(
        "Flaws{", "Flaws{\n" + str(character_full.weaknesses)
    )
    prototype = prototype.replace(
        "FeaturesTraits{",
        "FeaturesTraits{\n"
        r"\textbf{Features} \\"
        + r"\\".join(
            f"\n{feat} "
            for feat in filterfalse(
                Feat.ABILITY_SCORE_IMPROVEMENT.__eq__, character_wrapper.feats
            )
        ),
    )

    prototype = prototype.replace("Age{21", "Age{" + str(character_full.age))
    prototype = prototype.replace(
        "Height{1,60m}", "Height{" + str(character_full.height) + " cm}"
    )
    prototype = prototype.replace(
        "Weight{98 lbs}", "Weight{" + str(character_full.weight) + " kg}"
    )
    prototype = prototype.replace(
        "Eyes{Amber", "Eyes{" + character_full.eye_color
    )
    prototype = prototype.replace(
        "Skin{Blue", "Skin{" + character_full.skin_color
    )
    prototype = prototype.replace(
        "Hair{Bright Green", "Hair{" + character_full.hairstyle
    )
    prototype = prototype.replace(
        "CharacterAppearance{",
        "CharacterAppearance{\n" + character_full.appearance,
    )
    prototype = prototype.replace(
        "AdditionalFeaturesAndTraits{",
        "AdditionalFeaturesAndTraits{"
        + (
            (
                "\\\\Action\\\\"
                + "\\\\".join(character_wrapper.action_abilities)
            )
            if character_wrapper.action_abilities
            else ""
        )
        + (
            (
                "\\\\\\\\Bonus Action\\\\"
                + "\\\\".join(character_wrapper.bonus_action_abilities)
            )
            if character_wrapper.bonus_action_abilities
            else ""
        )
        + (
            (
                "\\\\\\\\Reaction\\\\"
                + "\\\\".join(character_wrapper.reaction_abilities)
            )
            if character_wrapper.reaction_abilities
            else ""
        )
        + (
            (
                "\\\\\\\\Free Action\\\\"
                + "\\\\".join(character_wrapper.free_action_abilities)
            )
            if character_wrapper.free_action_abilities
            else ""
        )
        + (
            (
                "\\\\\\\\Passive\\\\"
                + "\\\\".join(character_wrapper.passive_abilities)
            )
            if character_wrapper.passive_abilities
            else ""
        ),
    )
    prototype = prototype.replace(
        "Characterbackground{",
        "Characterbackground{\n" + character_full.backstory,
    )

    prototype = prototype.replace(
        "SpellcastingAbility{CHA",
        "SpellcastingAbility{"
        + str(
            character_wrapper.spellcasting_ability
            and character_wrapper.spellcasting_ability.value
        ),
    )
    prototype = prototype.replace(
        "SpellSaveDC{13", "SpellSaveDC{" + str(character_wrapper.spellsave_dc)
    )
    prototype = prototype.replace(
        "SpellAttackBonus{+5",
        "SpellAttackBonus{" + str(character_wrapper.spell_attack_bonus),
    )
    enum = (
        "CantripSlot",
        "FirstLevelSpellSlot",
        "SecondLevelSpellSlot",
        "ThirdLevelSpellSlot",
        "FourthLevelSpellSlot",
        "FifthLevelSpellSlot",
        "SixthLevelSpellSlot",
        "SeventhLevelSpellSlot",
        "EighthLevelSpellSlot",
        "NinthLevelSpellSlot",
    )
    spell_slots = "\n".join(
        "\\" + name + "sTotal{" + str(number) + "}"
        for name, number in zip(enum[1:], character_wrapper.spell_slots)
        if number
    )
    spells = (
        rf"\{spell_level}" + letter + "{" + spell + "}"
        for spell_level, level_spells in zip(
            enum, character_full.spells_by_level
        )
        for letter, spell in zip(string.ascii_uppercase, level_spells)
    )
    spells_prepared = (
        rf"\{spell_level}" + letter + "Prepared{False}"
        for spell_level, level_spells in zip(
            enum, character_full.spells_by_level
        )
        for letter, spell in zip(string.ascii_uppercase, level_spells)
    )
    spells_string = "\n".join(
        filter(
            lambda spell: not ("Cantrip" in spell and "Prepared" in spell),
            roundrobin(spells, spells_prepared),
        )
    )
    prepared_spells = list(
        spell if isinstance(spell, str) else spell.value
        for spell in character_wrapper.prepared_spells
    )
    prepared_spells_tex = list(
        spells_string.partition(spell_name)[0].rpartition("\\")[-1][:-1]
        for spell_name in prepared_spells
    )
    for spell in prepared_spells_tex:
        spells_string = spells_string.replace(
            f"{spell}Prepared" "{False}", f"{spell}Prepared" "{True}"
        )
    prototype = prototype.replace(
        r"\FirstLevelSpellSlotsTotal{3}",
        spell_slots + "\n\n" + spells_string,
    )

    return prototype
