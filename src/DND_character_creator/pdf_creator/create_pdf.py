from __future__ import annotations

import os
import shutil

from src.DND_character_creator.character_wrapper import CharacterWrapper
from src.DND_character_creator.config import Config
from src.DND_character_creator.pdf_creator.remove_blank_page import (
    remove_blank_page,
)
from src.DND_character_creator.pdf_creator.run_lunatex import run_lualatex
from src.DND_character_creator.pdf_creator.update_prototype import (
    update_prototype,
)


def create_pdf(
    character_wrapper: CharacterWrapper,
    config: Config,
):
    character_full = character_wrapper.character
    prototype = update_prototype(
        character_wrapper, character_full, config.tex_prototype.read_text()
    )
    character_path = config.pdf_creator.joinpath(f"{character_full.name}.tex")
    character_path.write_text(prototype)
    try:
        run_lualatex(character_path.name, config.pdf_creator)
    except Exception as e:
        raise e
    else:
        pdf_path = character_path.with_suffix(".pdf")
        shutil.move(pdf_path, config.characters_output_dir / pdf_path.name)
        shutil.move(
            character_path, config.characters_output_dir / character_path.name
        )
        remove_blank_page(config.characters_output_dir / pdf_path.name)
    finally:
        os.remove(character_path.with_suffix(".aux"))
        os.remove(character_path.with_suffix(".log"))
