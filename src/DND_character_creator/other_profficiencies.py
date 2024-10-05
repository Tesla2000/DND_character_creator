from __future__ import annotations

from enum import Enum


class ToolProficiency(str, Enum):
    ALCHEMISTS_SUPPLIES = "Alchemist's supplies"
    BREWERS_SUPPLIES = "Brewer's supplies"
    CALLIGRAPHERS_SUPPLIES = "Calligrapher's supplies"
    CARPENTERS_TOOLS = "Carpenter's tools"
    CARTOGRAPHERS_TOOLS = "Cartographer's tools"
    COBBLERS_TOOLS = "Cobbler's tools"
    COOKS_UTENSILS = "Cook's utensils"
    GLASSBLOWERS_TOOLS = "Glassblower's tools"
    JEWELERS_TOOLS = "Jeweler's tools"
    LEATHERWORKERS_TOOLS = "Leatherworker's tools"
    MASONS_TOOLS = "Mason's tools"
    PAINTERS_SUPPLIES = "Painter's supplies"
    POTTERS_TOOLS = "Potter's tools"
    SMITHS_TOOLS = "Smith's tools"
    TINKERS_TOOLS = "Tinker's tools"
    WEAVERS_TOOLS = "Weaver's tools"
    WOODCARVERS_TOOLS = "Woodcarver's tools"
    DISGUISE_KIT = "Disguise kit"
    FORGERY_KIT = "Forgery kit"
    HERBALISM_KIT = "Herbalism kit"
    POISONERS_KIT = "Poisoner's kit"
    NAVIGATORS_TOOLS = "Navigator's tools"
    THIEVES_TOOLS = "Thieves' tools"
    HEALERS_KIT = "Healer's kit"
    LAND_VEHICLES = "Land vehicles"
    WATER_VEHICLES = "Water vehicles"
    ANY_OF_YOUR_CHOICE = "Artisan tool of your choice"


class GamingSet(str, Enum):
    DICE_SET = "Dice set"
    DRAGONCHESS_SET = "Dragonchess set"
    PLAYING_CARD_SET = "Playing card set"
    THREE_DRAGON_ANTE_SET = "Three-Dragon Ante set"
    ANY_OF_YOUR_CHOICE = "Gaming set of your choice"


class MusicalInstrument(str, Enum):
    BAGPIPES = "Bagpipes"
    DRUM = "Drum"
    DULCIMER = "Dulcimer"
    FLUTE = "Flute"
    LUTE = "Lute"
    LYRE = "Lyre"
    HORN = "Horn"
    PAN_FLUTE = "Pan flute"
    SHAWM = "Shawm"
    VIOL = "Viol"
    ANY_OF_YOUR_CHOICE = "Musical instrument of your choice"


class WeaponProficiency(str, Enum):
    SIMPLE_WEAPON = "Simple Weapon"
    MARTIAL_WEAPON = "Martial Weapon"
    CLUB = "Club"
    DAGGER = "Dagger"
    GREATCLUB = "Greatclub"
    HANDAXE = "Handaxe"
    JAVELIN = "Javelin"
    LIGHT_HAMMER = "Light Hammer"
    MACE = "Mace"
    QUARTERSTAFF = "Quarterstaff"
    SICKLE = "Sickle"
    SPEAR = "Spear"
    LIGHT_CROSSBOW = "Light Crossbow"
    DART = "Dart"
    SHORTBOW = "Shortbow"
    SLING = "Sling"
    BATTLEAXE = "Battleaxe"
    FLAIL = "Flail"
    GLAIVE = "Glaive"
    GREATSWORD = "Greatsword"
    HALBERD = "Halberd"
    LANCE = "Lance"
    FIREARMS = "Firearms"
    LONGSWORD = "Longsword"
    MAUL = "Maul"
    MORNINGSTAR = "Morningstar"
    PIKE = "Pike"
    RAPIER = "Rapier"
    SCIMITAR = "Scimitar"
    SHORTSWORD = "Shortsword"
    TRIDENT = "Trident"
    WAR_PICK = "War Pick"
    WARHAMMER = "Warhammer"
    WHIP = "Whip"
    BLOWGUN = "Blowgun"
    HAND_CROSSBOW = "Hand Crossbow"
    HEAVY_CROSSBOW = "Heavy Crossbow"
    LONG_BOW = "Longbow"
    NET = "Net"
    ANY_OF_YOUR_CHOICE = "Any of your choice"


class ArmorProficiency(str, Enum):
    LIGHT_ARMOR = "Light Armor"
    MEDIUM_ARMOR = "Medium Armor"
    HEAVY_ARMOR = "Heavy Armor"
    SHIELDS = "Shields"
    ANY_OF_YOUR_CHOICE = "Any of your choice"
    ALL_ARMOR = "All Armor"
