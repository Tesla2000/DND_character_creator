from __future__ import annotations

import sys
from collections import ChainMap
from pathlib import Path
from typing import Any
from typing import Optional
from typing import Type

import toml
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from .choices.alignment import Alignment
from .choices.background_creatrion.background import Background
from .choices.class_creation.character_class import MainClass
from .choices.class_creation.character_class import WizardSubclass
from .choices.equipment_creation.armor import ArmorName
from .choices.equipment_creation.weapons import WeaponName
from .choices.health_creation.health_creation_method import (
    HealthCreationMethod,
)
from .choices.invocations.eldritch_invocation import WarlockPact
from .choices.race_creation.main_race import MainRace
from .choices.race_creation.sub_race_sources import DNDResource
from .choices.race_creation.sub_races import get_sub_races
from .choices.sex import Sex
from .choices.spell_slots.spell_slots import Cantrip
from .choices.spell_slots.spell_slots import EighthLevel
from .choices.spell_slots.spell_slots import FifthLevel
from .choices.spell_slots.spell_slots import FirstLevel
from .choices.spell_slots.spell_slots import FourthLevel
from .choices.spell_slots.spell_slots import NinthLevel
from .choices.spell_slots.spell_slots import SecondLevel
from .choices.spell_slots.spell_slots import SeventhLevel
from .choices.spell_slots.spell_slots import SixthLevel
from .choices.spell_slots.spell_slots import ThirdLevel
from .choices.stats_creation.statistic import Statistic
from .choices.stats_creation.stats_creation_method import StatsCreationMethod
from .custom_argument_parser import CustomArgumentParser
from .feats import Feat

load_dotenv()


class Config(BaseModel):
    _root: Path = Path(__file__).parent
    configuration_file: Optional[Path] = None
    characters_output_dir: Path = _root / "characters_output"

    pdf_creator: Path = _root / "pdf_creator"
    tex_prototype: Path = pdf_creator / "prototype.tex"

    scraped_path: Path = _root / "wiki_scraper/scraped_data"
    main_class_root: Path = scraped_path / "main_class"
    background_root: Path = scraped_path / "background"
    sub_races_root: Path = scraped_path / "sub_races"
    spells_root: Path = scraped_path / "spells"
    feats_root: Path = scraped_path / "feats"
    race_abilities_root: Path = scraped_path / "abilities"
    main_class_abilities_root: Path = scraped_path / "main_class_abilities"
    sub_class_abilities_root: Path = scraped_path / "sub_class_abilities"

    pos_args: list[str] = Field(default_factory=list)
    n_instances: int = 1
    level: Optional[PositiveInt] = 8
    main_class: Optional[MainClass] = MainClass.WIZARD
    base_description: str = "battlefield control war mage"
    stats_creation_method: StatsCreationMethod = (
        StatsCreationMethod.STANDARD_ARRAY
    )
    health_creation_method: HealthCreationMethod = HealthCreationMethod.AVERAGE
    backstory_prompt: str = "About 10 sentence long"
    appearance_prompt: str = "The character's general appearance"
    height_prompt: str = "Height in centimeters"
    weight_prompt: str = "Weight in kilograms"
    sex: Optional[Sex] = None
    backstory: Optional[str] = ""
    age: Optional[PositiveInt] = None
    first_most_important_stat: Optional[Statistic] = None
    second_most_important_stat: Optional[Statistic] = None
    third_most_important_stat: Optional[Statistic] = None
    forth_most_important_stat: Optional[Statistic] = None
    fifth_most_important_stat: Optional[Statistic] = None
    sixth_most_important_stat: Optional[Statistic] = None
    main_race: Optional[MainRace] = MainRace.HUMAN
    name: Optional[str] = None
    background: Optional[Background] = None
    alignment: Optional[Alignment] = None
    height: Optional[PositiveInt] = None
    weight: Optional[PositiveInt] = None
    eye_color: Optional[str] = None
    skin_color: Optional[str] = None
    hairstyle: Optional[str] = None
    appearance: Optional[str] = None
    subclass_sources: list[DNDResource] = Field(
        default_factory=lambda: list(DNDResource)
    )
    character_llm: str = "gpt-4o"
    character_llm_temp: float = 0.7
    details_llm: str = "gpt-4o-mini"
    details_llm_temp: float = 0
    cantrips: Optional[list[Cantrip]] = None
    first_level_spells: Optional[list[FirstLevel]] = None
    second_level_spells: Optional[list[SecondLevel]] = None
    third_level_spells: Optional[list[ThirdLevel]] = None
    fourth_level_spells: Optional[list[FourthLevel]] = None
    fifth_level_spells: Optional[list[FifthLevel]] = None
    sixth_level_spells: Optional[list[SixthLevel]] = None
    seventh_level_spells: Optional[list[SeventhLevel]] = None
    eighth_level_spells: Optional[list[EighthLevel]] = None
    ninth_level_spells: Optional[list[NinthLevel]] = None
    feats: Optional[list[Feat]] = None
    sub_race: Optional[str] = "Variant Human"
    sub_class: Optional[str] = WizardSubclass.WAR_MAGIC
    character_traits: Optional[str] = None
    ideals: Optional[str] = None
    bonds: Optional[str] = None
    weaknesses: Optional[str] = None
    amount_of_gold_for_equipment: Optional[int] = sys.maxsize
    warlock_pact: Optional[WarlockPact] = None
    armor: Optional[ArmorName] = None
    uses_shield: Optional[bool] = None
    weapons: Optional[list[WeaponName]] = None
    other_equipment: Optional[list[str]] = None

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        if self.sub_race:
            assert (
                self.main_race
            ), "If sub-race is provided the race must be provided first"
            assert self.sub_race in get_sub_races(self.main_race, self), (
                f"Sub-race must be in sub-races "
                f"{get_sub_races(self.main_race, self)}"
            )
        if self.sub_class:
            assert (
                self.main_class
            ), "If sub-class is provided the class must be provided first"


def parse_arguments(config_class: Type[Config]):
    parser = CustomArgumentParser(
        description="Configure the application settings."
    )

    for name, value in config_class.model_fields.items():
        if name.startswith("_"):
            continue
        parser.add_argument(
            f"--{name}" if name != "pos_args" else name,
            type=value.annotation,
            default=value.default,
            help=f"Default: {value}",
            value=value,
        )

    return parser.parse_args()


def create_config_with_args(config_class: Type[Config], args) -> Config:
    arg_dict = {
        name: getattr(args, name) for name in config_class.model_fields
    }
    if (
        arg_dict.get("configuration_file")
        and Path(arg_dict["configuration_file"]).exists()
    ):
        config = config_class(
            **dict(
                ChainMap(
                    toml.load(arg_dict.get("configuration_file")), arg_dict
                )
            )
        )
    else:
        config = config_class(**arg_dict)
    for variable in config.model_fields:
        value = getattr(config, variable)
        if (
            isinstance(value, Path)
            and value.suffix == ""
            and not value.exists()
        ):
            value.mkdir(parents=True)
    return config
