from __future__ import annotations

from enum import Enum

from src.DND_character_creator.choices.equipment_creation.item import Item


class ArmorName(str, Enum):
    CLOTHES = "Clothes"
    PADDED = "Padded"
    LEATHER = "Leather"
    STUDDED_LEATHER = "Studded Leather"
    HIDE = "Hide"
    CHAIN_SHIRT = "Chain Shirt"
    SCALE_MALE = "Scale Male"
    SPIKED_ARMOR = "Spiked Armor"
    BREASTPLATE = "Breastplate"
    HALFPLATE = "Halfplate"
    RING_MAIL = "Ring Mail"
    CHAIN_MAIL = "Chain Mail"
    SPLINT = "Splint"
    PLATE = "Plate"


class ArmorCategory(str, Enum):
    NONE = "None"
    LIGHT = "Light"
    MEDIUM = "Medium"
    HEAVY = "Heavy"


class Armor(Item):
    name: str
    category: ArmorCategory
    disadvantage_on_stealth: bool
    base_ac: int


armor_list = [
    Armor(
        name=ArmorName.CLOTHES,
        category=ArmorCategory.NONE,
        disadvantage_on_stealth=False,
        base_ac=10,
        cost=0,
    ),
    Armor(
        name=ArmorName.PADDED,
        category=ArmorCategory.LIGHT,
        disadvantage_on_stealth=True,
        base_ac=11,
        cost=5,
    ),
    Armor(
        name=ArmorName.LEATHER,
        category=ArmorCategory.LIGHT,
        disadvantage_on_stealth=False,
        base_ac=11,
        cost=10,
    ),
    Armor(
        name=ArmorName.STUDDED_LEATHER,
        category=ArmorCategory.LIGHT,
        disadvantage_on_stealth=False,
        base_ac=12,
        cost=45,
    ),
    Armor(
        name=ArmorName.HIDE,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=False,
        base_ac=12,
        cost=10,
    ),
    Armor(
        name=ArmorName.CHAIN_SHIRT,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=False,
        base_ac=13,
        cost=50,
    ),
    Armor(
        name=ArmorName.SCALE_MALE,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=True,
        base_ac=14,
        cost=50,
    ),
    Armor(
        name=ArmorName.SPIKED_ARMOR,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=True,
        base_ac=14,
        cost=75,
    ),
    Armor(
        name=ArmorName.BREASTPLATE,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=False,
        base_ac=14,
        cost=400,
    ),
    Armor(
        name=ArmorName.HALFPLATE,
        category=ArmorCategory.MEDIUM,
        disadvantage_on_stealth=True,
        base_ac=15,
        cost=750,
    ),
    Armor(
        name=ArmorName.RING_MAIL,
        category=ArmorCategory.HEAVY,
        disadvantage_on_stealth=True,
        base_ac=14,
        cost=30,
    ),
    Armor(
        name=ArmorName.CHAIN_MAIL,
        category=ArmorCategory.HEAVY,
        disadvantage_on_stealth=True,
        base_ac=16,
        cost=75,
    ),
    Armor(
        name=ArmorName.SPLINT,
        category=ArmorCategory.HEAVY,
        disadvantage_on_stealth=True,
        base_ac=17,
        cost=200,
    ),
    Armor(
        name=ArmorName.PLATE,
        category=ArmorCategory.HEAVY,
        disadvantage_on_stealth=True,
        base_ac=18,
        cost=1500,
    ),
    Item(name="shield", cost=10),
]
