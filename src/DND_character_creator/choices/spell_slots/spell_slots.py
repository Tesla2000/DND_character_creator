from __future__ import annotations

from enum import Enum
from typing import Type
from typing import TYPE_CHECKING

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)

if TYPE_CHECKING:
    from src.DND_character_creator.config import Config


class Spell(str, Enum):
    pass


class Cantrip(Spell):
    ACID_SPLASH = "Acid Splash"
    BLADE_WARD = "Blade Ward"
    BOOMING_BLADE = "Booming Blade"
    CHILL_TOUCH = "Chill Touch"
    CONTROL_FLAMES = "Control Flames"
    CREATE_BONFIRE = "Create Bonfire"
    DANCING_LIGHTS = "Dancing Lights"
    DECOMPOSE = "Decompose"
    DRUIDCRAFT = "Druidcraft"
    ELDRITCH_BLAST = "Eldritch Blast"
    ENCODE_THOUGHTS = "Encode Thoughts"
    FIRE_BOLT = "Fire Bolt"
    FRIENDS = "Friends"
    FROSTBITE = "Frostbite"
    GREEN_FLAME_BLADE = "Green-Flame Blade"
    GUIDANCE = "Guidance"
    GUST = "Gust"
    HAND_OF_RADIANCE = "Hand of Radiance"
    INFESTATION = "Infestation"
    LIGHT = "Light"
    LIGHTNING_LURE = "Lightning Lure"
    MAGE_HAND = "Mage Hand"
    MAGIC_STONE = "Magic Stone"
    MENDING = "Mending"
    MESSAGE = "Message"
    MIND_SLIVER = "Mind Sliver"
    MINOR_ILLUSION = "Minor Illusion"
    MOLD_EARTH = "Mold Earth"
    ON_OFF = "On-Off"
    POISON_SPRAY = "Poison Spray"
    PRESTIDIGITATION = "Prestidigitation"
    PRIMAL_SAVAGERY = "Primal Savagery"
    PRODUCE_FLAME = "Produce Flame"
    RAY_OF_FROST = "Ray of Frost"
    RESISTANCE = "Resistance"
    SACRED_FLAME = "Sacred Flame"
    SAPPING_STING = "Sapping Sting"
    SHAPE_WATER = "Shape Water"
    SHILLELAGH = "Shillelagh"
    SHOCKING_GRASP = "Shocking Grasp"
    SPARE_THE_DYING = "Spare the Dying"
    SWORD_BURST = "Sword Burst"
    THAUMATURGY = "Thaumaturgy"
    THORN_WHIP = "Thorn Whip"
    THUNDERCLAP = "Thunderclap"
    TOLL_THE_DEAD = "Toll the Dead"
    TRUE_STRIKE = "True Strike"
    VICIOUS_MOCKERY = "Vicious Mockery"
    VIRTUE = "Virtue"
    WORD_OF_RADIANCE = "Word of Radiance"


class FirstLevel(Spell):
    ABSORB_ELEMENTS = "Absorb Elements"
    ACID_STREAM = "Acid Stream (UA)"
    ALARM = "Alarm"
    ANIMAL_FRIENDSHIP = "Animal Friendship"
    ARCANE_WEAPON = "Arcane Weapon (UA)"
    ARMOR_OF_AGATHYS = "Armor of Agathys"
    ARMS_OF_HADAR = "Arms of Hadar"
    BANE = "Bane"
    BEAST_BOND = "Beast Bond"
    BLESS = "Bless"
    BURNING_HANDS = "Burning Hands"
    CATAPULT = "Catapult"
    CAUSE_FEAR = "Cause Fear"
    CEREMONY = "Ceremony"
    CHAOS_BOLT = "Chaos Bolt"
    CHARM_PERSON = "Charm Person"
    CHROMATIC_ORB = "Chromatic Orb"
    COLOR_SPRAY = "Color Spray"
    COMMAND = "Command"
    COMPELLED_DUEL = "Compelled Duel"
    COMPREHEND_LANGUAGES = "Comprehend Languages"
    CREATE_OR_DESTROY_WATER = "Create or Destroy Water"
    CURE_WOUNDS = "Cure Wounds"
    DETECT_EVIL_AND_GOOD = "Detect Evil and Good"
    DETECT_MAGIC = "Detect Magic"
    DETECT_POISON_AND_DISEASE = "Detect Poison and Disease"
    DISGUISE_SELF = "Disguise Self"
    DISSONANT_WHISPERS = "Dissonant Whispers"
    DISTORT_VALUE = "Distort Value"
    DIVINE_FAVOR = "Divine Favor"
    EARTH_TREMOR = "Earth Tremor"
    ENSNARING_STRIKE = "Ensnaring Strike"
    ENTANGLE = "Entangle"
    EXPEDITIOUS_RETREAT = "Expeditious Retreat"
    FAERIE_FIRE = "Faerie Fire"
    FALSE_LIFE = "False Life"
    FEATHER_FALL = "Feather Fall"
    FIND_FAMILIAR = "Find Familiar"
    FOG_CLOUD = "Fog Cloud"
    FROST_FINGERS = "Frost Fingers"
    GIFT_OF_ALACRITY = "Gift of Alacrity"
    GOODBERRY = "Goodberry"
    GREASE = "Grease"
    GUIDING_BOLT = "Guiding Bolt"
    GUIDING_HAND = "Guiding Hand (UA)"
    HAIL_OF_THORNS = "Hail of Thorns"
    HEALING_ELIXIR = "Healing Elixir (UA)"
    HEALING_WORD = "Healing Word"
    HELLISH_REBUKE = "Hellish Rebuke"
    HEROISM = "Heroism"
    HEX = "Hex"
    HUNTERS_MARK = "Hunter's Mark"
    ICE_KNIFE = "Ice Knife"
    ID_IN_SINUATION = "Id Insinuation (UA)"
    IDENTIFY = "Identify"
    ILLUSORY_SCRIPT = "Illusory Script"
    INFALLIBLE_RELAY = "Infallible Relay (UA)"
    INFLICT_WOUNDS = "Inflict Wounds"
    JIMS_MAGIC_MISSILE = "Jim's Magic Missile"
    JUMP = "Jump"
    LONGSTRIDER = "Longstrider"
    MAGE_ARMOR = "Mage Armor"
    MAGIC_MISSILE = "Magic Missile"
    MAGNIFY_GRAVITY = "Magnify Gravity"
    PROTECTION_FROM_EVIL_AND_GOOD = "Protection from Evil and Good"
    PUPPET = "Puppet (UA)"
    PURIFY_FOOD_AND_DRINK = "Purify Food and Drink"
    RAY_OF_SICKNESS = "Ray of Sickness"
    REMOTE_ACCESS = "Remote Access (UA)"
    SANCTUARY = "Sanctuary"
    SEARING_SMITE = "Searing Smite"
    SENSE_EMOTION = "Sense Emotion (UA)"
    SHIELD = "Shield"
    SHIELD_OF_FAITH = "Shield of Faith"
    SILENT_IMAGE = "Silent Image"
    SILVERY_BARBS = "Silvery Barbs"
    SLEEP = "Sleep"
    SNARE = "Snare"
    SPEAK_WITH_ANIMALS = "Speak with Animals"
    SUDDEN_AWAKENING = "Sudden Awakening (UA)"
    TASHAS_CAUSTIC_BREW = "Tasha's Caustic Brew"
    TASHAS_HIDEOUS_LAUGHTER = "Tasha's Hideous Laughter"
    TENSERS_FLOATING_DISK = "Tenser's Floating Disk"
    THUNDEROUS_SMITE = "Thunderous Smite"
    THUNDERWAVE = "Thunderwave"
    UNEARTHLY_CHORUS = "Unearthly Chorus (UA)"
    UNSEEN_SERVANT = "Unseen Servant"
    WILD_CUNNING = "Wild Cunning (UA)"
    WITCH_BOLT = "Witch Bolt"
    WRATHFUL_SMITE = "Wrathful Smite"
    ZEPHYR_STRIKE = "Zephyr Strike"


class SecondLevel(Spell):
    AGANAZZARS_SCORCHER = "Aganazzar's Scorcher"
    AID = "Aid"
    AIR_BUBBLE = "Air Bubble"
    ALTER_SELF = "Alter Self"
    ANIMAL_MESSENGER = "Animal Messenger"
    ARCANE_HACKING_UA = "Arcane Hacking (UA)"
    ARCANE_LOCK = "Arcane Lock"
    AUGURY = "Augury"
    BARKSKIN = "Barkskin"
    BEAST_SENSE = "Beast Sense"
    BLINDNESS_DEAFNESS = "Blindness-Deafness"
    BLUR = "Blur"
    BORROWED_KNOWLEDGE = "Borrowed Knowledge"
    BRANDING_SMITE = "Branding Smite"
    CALM_EMOTIONS = "Calm Emotions"
    CLOUD_OF_DAGGERS = "Cloud of Daggers"
    CONTINUAL_FLAME = "Continual Flame"
    CORDON_OF_ARROWS = "Cordon of Arrows"
    CROWN_OF_MADNESS = "Crown of Madness"
    DARKNESS = "Darkness"
    DARKVISION = "Darkvision"
    DETECT_THOUGHTS = "Detect Thoughts"
    DIGITAL_PHANTOM_UA = "Digital Phantom (UA)"
    DRAGONS_BREATH = "Dragon's Breath"
    DUST_DEVIL = "Dust Devil"
    EARTHBIND = "Earthbind"
    ENHANCE_ABILITY = "Enhance Ability"
    ENLARGE_REDUCE = "Enlarge-Reduce"
    ENTHRALL = "Enthrall"
    FIND_STEED = "Find Steed"
    FIND_TRAPS = "Find Traps"
    FIND_VEHICLE_UA = "Find Vehicle (UA)"
    FLAME_BLADE = "Flame Blade"
    FLAMING_SPHERE = "Flaming Sphere"
    FLOCK_OF_FAMILIARS = "Flock of Familiars"
    FORTUNES_FAVOR = "Fortune's Favor"
    GENTLE_REPOSE = "Gentle Repose"
    GIFT_OF_GAB = "Gift of Gab"
    GUST_OF_WIND = "Gust of Wind"
    HEALING_SPIRIT = "Healing Spirit"
    HEAT_METAL = "Heat Metal"
    HOLD_PERSON = "Hold Person"
    IMMOVABLE_OBJECT = "Immovable Object"
    INVISIBILITY = "Invisibility"
    JIMS_GLOWING_COIN = "Jim's Glowing Coin"
    KINETIC_JAUNT = "Kinetic Jaunt"
    KNOCK = "Knock"
    LESSER_RESTORATION = "Lesser Restoration"
    LEVITATE = "Levitate"
    LOCATE_ANIMALS_OR_PLANTS = "Locate Animals or Plants"
    LOCATE_OBJECT = "Locate Object"
    MAGIC_MOUTH = "Magic Mouth"
    MAGIC_WEAPON = "Magic Weapon"
    MAXIMILLIANS_EARTHEN_GRASP = "Maximillian's Earthen Grasp"
    MELFS_ACID_ARROW = "Melf's Acid Arrow"
    MENTAL_BARRIER_UA = "Mental Barrier (UA)"
    MIND_SPIKE = "Mind Spike"
    MIND_THRUST_UA = "Mind Thrust (UA)"
    MIRROR_IMAGE = "Mirror Image"
    MISTY_STEP = "Misty Step"
    MOONBEAM = "Moonbeam"
    NATHAIRS_MISCHIEF = "Nathair's Mischief"
    NATHAIRS_MISCHIEF_UA = "Nathair's Mischief (UA)"
    NYSTULS_MAGIC_AURA = "Nystul's Magic Aura"
    PASS_WITHOUT_TRACE = "Pass Without Trace"
    PHANTASMAL_FORCE = "Phantasmal Force"
    PRAYER_OF_HEALING = "Prayer of Healing"
    PROTECTION_FROM_POISON = "Protection from Poison"
    PYROTECHNICS = "Pyrotechnics"
    RAY_OF_ENFEEBLEMENT = "Ray of Enfeeblement"
    RIMES_BINDING_ICE = "Rime's Binding Ice"
    ROPE_TRICK = "Rope Trick"
    SCORCHING_RAY = "Scorching Ray"
    SEE_INVISIBILITY = "See Invisibility"
    SHADOW_BLADE = "Shadow Blade"
    SHATTER = "Shatter"
    SILENCE = "Silence"
    SKYWRITE = "Skywrite"
    SNILLOCS_SNOWBALL_STORM = "Snilloc's Snowball Storm"
    SPIDER_CLIMB = "Spider Climb"
    SPIKE_GROWTH = "Spike Growth"
    SPIRITUAL_WEAPON = "Spiritual Weapon"
    SPRAY_OF_CARDS = "Spray Of Cards"
    SPRAY_OF_CARDS_UA = "Spray of Cards (UA)"
    SUGGESTION = "Suggestion"
    SUMMON_BEAST = "Summon Beast"
    TASHAS_MIND_WHIP = "Tasha's Mind Whip"
    THOUGHT_SHIELD_UA = "Thought Shield (UA)"
    VORTEX_WARP = "Vortex Warp"
    WARDING_BOND = "Warding Bond"
    WARDING_WIND = "Warding Wind"
    WARP_SENSE = "Warp Sense"
    WEB = "Web"
    WITHER_AND_BLOOM = "Wither and Bloom"
    WRISTPOCKET = "Wristpocket"
    ZONE_OF_TRUTH = "Zone of Truth"


class ThirdLevel(Spell):
    ANIMATE_DEAD = "Animate Dead"
    ANTAGONIZE = "Antagonize"
    ANTAGONIZE_UA = "Antagonize (UA)"
    ASHARDALONS_STRIDE = "Ashardalon's Stride"
    AURA_OF_VITALITY = "Aura of Vitality"
    BEACON_OF_HOPE = "Beacon of Hope"
    BESTOW_CURSE = "Bestow Curse"
    BLINDING_SMITE = "Blinding Smite"
    BLINK = "Blink"
    CALL_LIGHTNING = "Call Lightning"
    CATNAP = "Catnap"
    CLAIRVOYANCE = "Clairvoyance"
    CONJURE_ANIMALS = "Conjure Animals"
    CONJURE_BARRAGE = "Conjure Barrage"
    CONJURE_LESSER_DEMON_UA = "Conjure Lesser Demon (UA)"
    COUNTERSPELL = "Counterspell"
    CREATE_FOOD_AND_WATER = "Create Food and Water"
    CRUSADERS_MANTLE = "Crusader's Mantle"
    DAYLIGHT = "Daylight"
    DISPEL_MAGIC = "Dispel Magic"
    ELEMENTAL_WEAPON = "Elemental Weapon"
    ENEMIES_ABOUND = "Enemies Abound"
    ERUPTING_EARTH = "Erupting Earth"
    FAST_FRIENDS = "Fast Friends"
    FEAR = "Fear"
    FEIGN_DEATH = "Feign Death"
    FIREBALL = "Fireball"
    FLAME_ARROWS = "Flame Arrows"
    FLAME_STRIDE_UA = "Flame Stride (UA)"
    FLY = "Fly"
    GALDERS_TOWER = "Galder's Tower"
    GASEOUS_FORM = "Gaseous Form"
    GLYPH_OF_WARDING = "Glyph of Warding"
    HASTE = "Haste"
    HAYWIRE_UA = "Haywire (UA)"
    HUNGER_OF_HADAR = "Hunger Of Hadar"
    HYPNOTIC_PATTERN = "Hypnotic Pattern"
    INCITE_GREED = "Incite Greed"
    INTELLECT_FORTRESS = "Intellect Fortress"
    INVISIBILITY_TO_CAMERAS_UA = "Invisibility To Cameras (UA)"
    LEOMUNDS_TINY_HUT = "Leomund's Tiny Hut"
    LIFE_TRANSFERENCE = "Life Transference"
    LIGHTNING_ARROW = "Lightning Arrow"
    LIGHTNING_BOLT = "Lightning Bolt"
    MAGIC_CIRCLE = "Magic Circle"
    MAJOR_IMAGE = "Major Image"
    MASS_HEALING_WORD = "Mass Healing Word"
    MELD_INTO_STONE = "Meld into Stone"
    MELFS_MINUTE_METEORS = "Melf's Minute Meteors"
    MOTIVATIONAL_SPEECH = "Motivational Speech"
    NONDETECTION = "Nondetection"
    PHANTOM_STEED = "Phantom Steed"
    PLANT_GROWTH = "Plant Growth"
    PROTECTION_FROM_BALLISTICS_UA = "Protection from Ballistics (UA)"
    PROTECTION_FROM_ENERGY = "Protection from Energy"
    PSIONIC_BLAST_UA = "Psionic Blast (UA)"
    REMOVE_CURSE = "Remove Curse"
    REVIVIFY = "Revivify"
    SENDING = "Sending"
    SLEET_STORM = "Sleet Storm"
    SLOW = "Slow"
    SPEAK_WITH_DEAD = "Speak with Dead"
    SPEAK_WITH_PLANTS = "Speak with Plants"
    SPIRIT_GUARDIANS = "Spirit Guardians"
    SPIRIT_SHROUD = "Spirit Shroud"
    STINKING_CLOUD = "Stinking Cloud"
    SUMMON_FEY = "Summon Fey"
    SUMMON_LESSER_DEMONS = "Summon Lesser Demons"
    SUMMON_SHADOWSPAWN = "Summon Shadowspawn"
    SUMMON_UNDEAD = "Summon Undead"
    SUMMON_WARRIOR_SPIRIT_UA = "Summon Warrior Spirit (UA)"
    THUNDER_STEP = "Thunder Step"
    TIDAL_WAVE = "Tidal Wave"
    TINY_SERVANT = "Tiny Servant"
    TONGUES = "Tongues"
    VAMPIRIC_TOUCH = "Vampiric Touch"
    WALL_OF_SAND = "Wall of Sand"
    WALL_OF_WATER = "Wall of Water"
    WATER_BREATHING = "Water Breathing"
    WATER_WALK = "Water Walk"
    WIND_WALL = "Wind Wall"


class FourthLevel(Spell):
    ARCANE_EYE = "Arcane Eye"
    AURA_OF_LIFE = "Aura of Life"
    AURA_OF_PURITY = "Aura of Purity"
    BANISHMENT = "Banishment"
    BLIGHT = "Blight"
    CHARM_MONSTER = "Charm Monster"
    COMPULSION = "Compulsion"
    CONFUSION = "Confusion"
    CONJURE_BARLGURA_UA = "Conjure Barlgura (UA)"
    CONJURE_KNOWBOT_UA = "Conjure Knowbot (UA)"
    CONJURE_MINOR_ELEMENTALS = "Conjure Minor Elementals"
    CONJURE_SHADOW_DEMON_UA = "Conjure Shadow Demon (UA)"
    CONJURE_WOODLAND_BEINGS = "Conjure Woodland Beings"
    CONTROL_WATER = "Control Water"
    DEATH_WARD = "Death Ward"
    DIMENSION_DOOR = "Dimension Door"
    DIVINATION = "Divination"
    DOMINATE_BEAST = "Dominate Beast"
    EGO_WHIP_UA = "Ego Whip (UA)"
    ELEMENTAL_BANE = "Elemental Bane"
    EVARDS_BLACK_TENTACLES = "Evard's Black Tentacles"
    FABRICATE = "Fabricate"
    FIND_GREATER_STEED = "Find Greater Steed"
    FIRE_SHIELD = "Fire Shield"
    FREEDOM_OF_MOVEMENT = "Freedom of Movement"
    GALDERS_SPEEDY_COURIER = "Galder's Speedy Courier"
    GATE_SEAL = "Gate Seal"
    GIANT_INSECT = "Giant Insect"
    GRASPING_VINE = "Grasping Vine"
    GRAVITY_SINKHOLE = "Gravity Sinkhole"
    GREATER_INVISIBILITY = "Greater Invisibility"
    GUARDIAN_OF_FAITH = "Guardian of Faith"
    GUARDIAN_OF_NATURE = "Guardian of Nature"
    HALLUCINATORY_TERRAIN = "Hallucinatory Terrain"
    ICE_STORM = "Ice Storm"
    LEOMUNDS_SECRET_CHEST = "Leomund's Secret Chest"
    LOCATE_CREATURE = "Locate Creature"
    MORDENKAINENS_FAITHFUL_HOUND = "Mordenkainen's Faithful Hound"
    MORDENKAINENS_PRIVATE_SANCTUM = "Mordenkainen's Private Sanctum"
    OTILUKES_RESILIENT_SPHERE = "Otiluke's Resilient Sphere"
    PHANTASMAL_KILLER = "Phantasmal Killer"
    POLYMORPH = "Polymorph"
    RAULOTHIMS_PSYCHIC_LANCE = "Raulothim's Psychic Lance"
    RAULOTHIMS_PSYCHIC_LANCE_UA = "Raulothim's Psychic Lance (UA)"
    SHADOW_OF_MOIL = "Shadow of Moil"
    SICKENING_RADIANCE = "Sickening Radiance"
    SPIRIT_OF_DEATH = "Spirit of Death"
    SPIRIT_OF_DEATH_UA = "Spirit of Death (UA)"
    STAGGERING_SMITE = "Staggering Smite"
    STONE_SHAPE = "Stone Shape"
    STONESKIN = "Stoneskin"
    STORM_SPHERE = "Storm Sphere"
    SUMMON_ABERRATION = "Summon Aberration"
    SUMMON_CONSTRUCT = "Summon Construct"
    SUMMON_ELEMENTAL = "Summon Elemental"
    SUMMON_GREATER_DEMON = "Summon Greater Demon"
    SYNCHRONICITY_UA = "Synchronicity (UA)"
    SYSTEM_BACKDOOR_UA = "System Backdoor (UA)"
    VITRIOLIC_SPHERE = "Vitriolic Sphere"
    WALL_OF_FIRE = "Wall of Fire"
    WATERY_SPHERE = "Watery Sphere"
    WIDOGASTS_VAULT_OF_AMBER_HB = "Widogast's Vault of Amber (HB)"
    WIDOGASTS_WEB_OF_FIRE_HB = "Widogast's Web of Fire (HB)"


class FifthLevel(Spell):
    ANIMATE_OBJECTS = "Animate Objects"
    ANTILIFE_SHELL = "Antilife Shell"
    AWAKEN = "Awaken"
    BANISHING_SMITE = "Banishing Smite"
    BIGBYS_HAND = "Bigby's Hand"
    CIRCLE_OF_POWER = "Circle of Power"
    CLOUDKILL = "Cloudkill"
    COMMUNE = "Commune"
    COMMUNE_WITH_CITY_UA = "Commune with City (UA)"
    COMMUNE_WITH_NATURE = "Commune with Nature"
    CONE_OF_COLD = "Cone of Cold"
    CONJURE_ELEMENTAL = "Conjure Elemental"
    CONJURE_VOLLEY = "Conjure Volley"
    CONJURE_VROCK_UA = "Conjure Vrock (UA)"
    CONTACT_OTHER_PLANE = "Contact Other Plane"
    CONTAGION = "Contagion"
    CONTROL_WINDS = "Control Winds"
    CREATE_SPELLJAMMING_HELM = "Create Spelljamming Helm"
    CREATION = "Creation"
    DANSE_MACABRE = "Danse Macabre"
    DAWN = "Dawn"
    DESTRUCTIVE_WAVE = "Destructive Wave"
    DISPEL_EVIL_AND_GOOD = "Dispel Evil and Good"
    DOMINATE_PERSON = "Dominate Person"
    DREAM = "Dream"
    ENERVATION = "Enervation"
    FAR_STEP = "Far Step"
    FLAME_STRIKE = "Flame Strike"
    FREEDOM_OF_THE_WINDS_HB = "Freedom of the Winds (HB)"
    GEAS = "Geas"
    GREATER_RESTORATION = "Greater Restoration"
    HALLOW = "Hallow"
    HOLD_MONSTER = "Hold Monster"
    HOLY_WEAPON = "Holy Weapon"
    IMMOLATION = "Immolation"
    INFERNAL_CALLING = "Infernal Calling"
    INSECT_PLAGUE = "Insect Plague"
    LEGEND_LORE = "Legend Lore"
    MAELSTROM = "Maelstrom"
    MASS_CURE_WOUNDS = "Mass Cure Wounds"
    MISLEAD = "Mislead"
    MODIFY_MEMORY = "Modify Memory"
    NEGATIVE_ENERGY_FLOOD = "Negative Energy Flood"
    PASSWALL = "Passwall"
    PLANAR_BINDING = "Planar Binding"
    RAISE_DEAD = "Raise Dead"
    RARYS_TELEPATHIC_BOND = "Rary's Telepathic Bond"
    REINCARNATE = "Reincarnate"
    SCRYING = "Scrying"
    SEEMING = "Seeming"
    SHUTDOWN_UA = "Shutdown (UA)"
    SKILL_EMPOWERMENT = "Skill Empowerment"
    STEEL_WIND_STRIKE = "Steel Wind Strike"
    SUMMON_CELESTIAL = "Summon Celestial"
    SUMMON_DRACONIC_SPIRIT = "Summon Draconic Spirit"
    SUMMON_DRACONIC_SPIRIT_UA = "Summon Draconic Spirit (UA)"
    SWIFT_QUIVER = "Swift Quiver"
    SYNAPTIC_STATIC = "Synaptic Static"
    TELEKINESIS = "Telekinesis"
    TELEPORTATION_CIRCLE = "Teleportation Circle"
    TEMPORAL_SHUNT = "Temporal Shunt"
    TRANSMUTE_ROCK = "Transmute Rock"
    TREE_STRIDE = "Tree Stride"
    WALL_OF_FORCE = "Wall of Force"
    WALL_OF_LIGHT = "Wall of Light"
    WALL_OF_STONE = "Wall of Stone"
    WRATH_OF_NATURE = "Wrath Of Nature"


class SixthLevel(Spell):
    ARCANE_GATE = "Arcane Gate"
    BLADE_BARRIER = "Blade Barrier"
    BONES_OF_THE_EARTH = "Bones of the Earth"
    CHAIN_LIGHTNING = "Chain Lightning"
    CIRCLE_OF_DEATH = "Circle of Death"
    CONJURE_FEY = "Conjure Fey"
    CONTINGENCY = "Contingency"
    CREATE_HOMUNCULUS = "Create Homunculus"
    CREATE_UNDEAD = "Create Undead"
    DISINTEGRATE = "Disintegrate"
    DRAWMIJS_INSTANT_SUMMONS = "Drawmij's Instant Summons"
    DRUID_GROVE = "Druid Grove"
    EYEBITE = "Eyebite"
    FIND_THE_PATH = "Find the Path"
    FIZBANS_PLATINUM_SHIELD = "Fizban's Platinum Shield"
    FIZBANS_PLATINUM_SHIELD_UA = "Fizban's Platinum Shield (UA)"
    FLESH_TO_STONE = "Flesh to Stone"
    FORBIDDANCE = "Forbiddance"
    GLOBE_OF_INVULNERABILITY = "Globe of Invulnerability"
    GRAVITY_FISSURE = "Gravity Fissure"
    GUARDS_AND_WARDS = "Guards and Wards"
    HARM = "Harm"
    HEAL = "Heal"
    HEROES_FEAST = "Heroes' Feast"
    INVESTITURE_OF_FLAME = "Investiture of Flame"
    INVESTITURE_OF_ICE = "Investiture of Ice"
    INVESTITURE_OF_STONE = "Investiture of Stone"
    INVESTITURE_OF_WIND = "Investiture of Wind"
    MAGIC_JAR = "Magic Jar"
    MASS_SUGGESTION = "Mass Suggestion"
    MENTAL_PRISON = "Mental Prison"
    MOVE_EARTH = "Move Earth"
    OTHERWORLDLY_FORM_UA = "Otherworldly Form (UA)"
    OTIULKES_FREEZING_SPHERE = "Otiluke's Freezing Sphere"
    OTTOS_IRRESISTIBLE_DANCE = "Otto's Irresistible Dance"
    PLANAR_ALLY = "Planar Ally"
    PRIMORDIAL_WARD = "Primordial Ward"
    PROGRAMMED_ILLUSION = "Programmed Illusion"
    PSYCHIC_CRUSH_UA = "Psychic Crush (UA)"
    SCATTER = "Scatter"
    SOUL_CAGE = "Soul Cage"
    SUMMON_FIEND = "Summon Fiend"
    SUNBEAM = "Sunbeam"
    TASHAS_OTHERWORLDLY_GUISE = "Tasha's Otherworldly Guise"
    TENSERS_TRANSFORMATION = "Tenser's Transformation"
    TRANSPORT_VIA_PLANTS = "Transport via Plants"
    TRUE_SIGHT = "True Seeing"
    WALL_OF_ICE = "Wall of Ice"
    WALL_OF_THORNS = "Wall of Thorns"
    WIDOGASTS_TRANSMOGRIFICATION_HB = "Widogast's Transmogrification (HB)"
    WIND_WALK = "Wind Walk"
    WORD_OF_RECALL = "Word of Recall"


class SeventhLevel(Spell):
    CONJURE_CELESTIAL = "Conjure Celestial"
    CONJURE_HEZROU_UA = "Conjure Hezrou (UA)"
    CREATE_MAGEN = "Create Magen"
    CROWN_OF_STARS = "Crown of Stars"
    DELAYED_BLAST_FIREBALL = "Delayed Blast Fireball"
    DIVINE_WORD = "Divine Word"
    DRACONIC_TRANSFORMATION = "Draconic Transformation"
    DRACONIC_TRANSFORMATION_UA = "Draconic Transformation (UA)"
    DREAM_OF_THE_BLUE_VEIL = "Dream of the Blue Veil"
    ETHEREALNESS = "Etherealness"
    FINGER_OF_DEATH = "Finger of Death"
    FIRE_STORM = "Fire Storm"
    FORCECAGE = "Forcecage"
    MIRAGE_ARCANE = "Mirage Arcane"
    MORDENKAINENS_MAGNIFICENT_MANSION = "Mordenkainen's Magnificent Mansion"
    MORDENKAINENS_SWORD = "Mordenkainen's Sword"
    PLANE_SHIFT = "Plane Shift"
    POWER_WORD_PAIN = "Power Word: Pain"
    PRISMATIC_SPRAY = "Prismatic Spray"
    PROJECT_IMAGE = "Project Image"
    REGENERATE = "Regenerate"
    RESURRECTION = "Resurrection"
    REVERSE_GRAVITY = "Reverse Gravity"
    SEQUESTER = "Sequester"
    SIMULACRUM = "Simulacrum"
    SYMBOL = "Symbol"
    TELEPORT = "Teleport"
    TEMPLE_OF_THE_GODS = "Temple of the Gods"
    TETHER_ESSENCE = "Tether Essence"
    WHIRLWIND = "Whirlwind"


class EighthLevel(Spell):
    ABI_DALZIMS_HORRID_WILTING = "Abi-Dalzim's Horrid Wilting"
    ANIMAL_SHAPES = "Animal Shapes"
    ANTIMAGIC_FIELD = "Antimagic Field"
    ANTIPATHY_SYMPATHY = "Antipathy/Sympathy"
    CLONE = "Clone"
    CONTROL_WEATHER = "Control Weather"
    DARK_STAR = "Dark Star"
    DEMIPLANE = "Demiplane"
    DOMINATE_MONSTER = "Dominate Monster"
    EARTHQUAKE = "Earthquake"
    FEEBLEMIND = "Feeblemind"
    GLIBNESS = "Glibness"
    HOLY_AURA = "Holy Aura"
    ILLUSORY_DRAGON = "Illusory Dragon"
    INCENDIARY_CLOUD = "Incendiary Cloud"
    MADDENING_DARKNESS = "Maddening Darkness"
    MAZE = "Maze"
    MIGHTY_FORTRESS = "Mighty Fortress"
    MIND_BLANK = "Mind Blank"
    POWER_WORD_STUN = "Power Word: Stun"
    REALITY_BREAK = "Reality Break"
    SUNBURST = "Sunburst"
    TELEPATHY = "Telepathy"
    TSUNAMI = "Tsunami"


class NinthLevel(Spell):
    ASTRAL_PROJECTION = "Astral Projection"
    BLADE_OF_DISASTER = "Blade of Disaster"
    FORESIGHT = "Foresight"
    GATE = "Gate"
    IMPRISONMENT = "Imprisonment"
    INVULNERABILITY = "Invulnerability"
    MASS_HEAL = "Mass Heal"
    MASS_POLYMORPH = "Mass Polymorph"
    METEOR_SWARM = "Meteor Swarm"
    POWER_WORD_HEAL = "Power Word: Heal"
    POWER_WORD_KILL = "Power Word: Kill"
    PRISMATIC_WALL = "Prismatic Wall"
    PSYCHIC_SCREAM = "Psychic Scream"
    RAVENOUS_VOID = "Ravenous Void"
    SHAPECHANGE = "Shapechange"
    STORM_OF_VENGEANCE = "Storm of Vengeance"
    TIME_RAVAGE = "Time Ravage"
    TIME_STOP = "Time Stop"
    TRUE_POLYMORPH = "True Polymorph"
    TRUE_RESURRECTION = "True Resurrection"
    WEIRD = "Weird"
    WISH = "Wish"


all_spells = [
    Cantrip,
    FirstLevel,
    SecondLevel,
    ThirdLevel,
    FourthLevel,
    FifthLevel,
    SixthLevel,
    SeventhLevel,
    EighthLevel,
    NinthLevel,
]


def filter_accessible(
    spell_type: Type[Spell], main_class: MainClass, config: Config
) -> Type[Enum]:
    return Spell(
        f"{main_class.value}{spell_type.__name__}",
        dict(
            (spell, spell.value)
            for spell in spell_type
            if main_class.value
            in config.spells_root.joinpath(spell_type.__name__.lower())
            .joinpath(spell.value.replace("/", "-").replace(":", ""))
            .read_text()
            .split(",")
        ),
    )
