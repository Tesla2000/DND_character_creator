from __future__ import annotations

import json
from collections import ChainMap

from langchain_core.language_models import BaseChatModel
from pydantic import BaseModel

from src.DND_character_creator.character_base import CharacterBase
from src.DND_character_creator.character_full import CharacterFull
from src.DND_character_creator.character_full import (
    get_full_character_template,
)  # noqa: E501
from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.config import Config


class CharacterDetailsFiller:
    def __init__(
        self,
        character_base_template: BaseModel,
        base_pre_defined_fields: dict,
        config: Config,
        llm: BaseChatModel,
    ):
        self.config = config
        self.base_pre_defined_fields = base_pre_defined_fields
        self.character_base_template = character_base_template
        self.llm = llm

    def fill_details(self) -> CharacterWrapper:
        self._get_character_full()
        return self._fill_character_details()

    def _get_character_full(self):
        self.character_base = CharacterBase(
            **self.base_pre_defined_fields,
            **self.character_base_template.model_dump(),
        )
        character_full_template, self.full_pre_defined_fields = (
            get_full_character_template(self.config, self.character_base)
        )
        description_full = self.config.base_description.strip()
        pre_defined = json.dumps(
            dict(
                **ChainMap(
                    self.full_pre_defined_fields,
                    json.loads(self.character_base.model_dump_json()),
                )
            ),
            indent=2,
        )
        description_full += (
            f"\nThe following details about the character are given:\n"
            f"{pre_defined}"
        )
        full_template = self.llm.with_structured_output(
            character_full_template
        )
        self.character_full_template = full_template.invoke(description_full)

    def _fill_character_details(self) -> CharacterWrapper:
        character_full = CharacterFull(
            **self.full_pre_defined_fields,
            **self.character_full_template.model_dump(),
            **self.character_base.model_dump(),
        )
        print(character_full.model_dump_json(indent=2))
        return CharacterWrapper(character_full, self.config, self.llm)
