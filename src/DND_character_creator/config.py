from __future__ import annotations

from pathlib import Path
from typing import Optional
from typing import Type

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from .choices.alignment import Alignment
from .choices.background_creatrion.background import Background
from .choices.class_creation.character_class import MainClass
from .choices.health_creation.health_creation_method import (
    HealthCreationMethod,
)
from .choices.main_race import MainRace
from .choices.sex import Sex
from .choices.stats_creation.statistic import Statistic
from .choices.stats_creation.stats_creation_method import StatsCreationMethod
from .custom_argument_parser import CustomArgumentParser

load_dotenv()


class Config(BaseModel):
    _root: Path = Path(__file__).parent
    pos_args: list[str] = Field(default_factory=list)
    level: Optional[PositiveInt] = None
    class_: Optional[MainClass] = None
    description: str = (
        "Create a character obsessed with protecting forests for any cost."
    )
    stats_creation_method: StatsCreationMethod = (
        StatsCreationMethod.STANDARD_ARRAY
    )
    health_creation_method: HealthCreationMethod = HealthCreationMethod.AVERAGE
    backstory_prompt: str = "About 10 sentence long"
    appearance_prompt: str = "The character's general appearance"
    height_prompt: str = "Height in centimeters"
    weight_prompt: str = "Weight in kilograms"
    sex: Optional[Sex] = None
    backstory: Optional[str] = None
    age: Optional[PositiveInt] = None
    first_most_important_stat: Optional[Statistic] = None
    second_most_important_stat: Optional[Statistic] = None
    third_most_important_stat: Optional[Statistic] = None
    forth_most_important_stat: Optional[Statistic] = None
    fifth_most_important_stat: Optional[Statistic] = None
    sixth_most_important_stat: Optional[Statistic] = None
    race: Optional[MainRace] = None
    name: Optional[str] = None
    background: Optional[Background] = None
    alignment: Optional[Alignment] = None
    height: Optional[PositiveInt] = None
    weight: Optional[PositiveInt] = None
    eye_color: Optional[str] = None
    skin_color: Optional[str] = None
    hairstyle: Optional[str] = None
    appearance: Optional[str] = None


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
    config = config_class(
        **{name: getattr(args, name) for name in config_class.model_fields}
    )
    for variable in config.model_fields:
        value = getattr(config, variable)
        if (
            isinstance(value, Path)
            and value.suffix == ""
            and not value.exists()
        ):
            value.mkdir(parents=True)
    return config
