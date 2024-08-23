from __future__ import annotations

from pathlib import Path
from typing import Optional
from typing import Type

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic import Field
from pydantic import PositiveInt

from .choices.class_creation.character_class import CharacterClass
from .choices.health_creation.health_creation_method import (
    HealthCreationMethod,
)
from .choices.stats_creation.stats_creation_method import StatsCreationMethod
from .custom_argument_parser import CustomArgumentParser

load_dotenv()


class Config(BaseModel):
    _root: Path = Path(__file__).parent
    pos_args: list[str] = Field(default_factory=list)
    level: PositiveInt = 1
    class_: Optional[CharacterClass] = None
    description: str = (
        "Character obsessed with protecting forests for any cost"
    )
    stats_creation_method: StatsCreationMethod = (
        StatsCreationMethod.STANDARD_ARRAY
    )
    health_creation_method: HealthCreationMethod = HealthCreationMethod.AVERAGE
    backstory_prompt: str = "About 10 sentence long"
    looks_prompt: str = "Describe general looks of a character"


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
