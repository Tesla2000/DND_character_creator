from __future__ import annotations

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilitiesTemplate,
)

url = "https://dnd5e.wikidot.com/{}"


def scraper_wiki_class(main_class: MainClass, output_dir: Path, llm):
    main_class_path = output_dir.joinpath(f"{main_class.value}")
    if main_class_path.exists():
        return
    response = requests.get(url.format(main_class.value.lower()))
    if response.status_code != 200:
        raise ValueError("Wrong status code")
    main_class_path.mkdir()
    content = response.content.decode()
    soup = BeautifulSoup(content, "html.parser")

    page_struct = str(soup.find("div", id="page-content"))
    abilities_result = llm.invoke(
        "Extract data about abilities of a class from page content:\n\n"
        + page_struct
    )
    for ability in abilities_result.abilities:
        ability.name = ability.name.replace("/", "-")
        ability_path = main_class_path.joinpath(f"{ability.name}.json")
        if ability_path.exists():
            continue
        ability_path.write_text(
            json.dumps(json.loads(ability.model_dump_json()), indent=2)
        )


if __name__ == "__main__":
    llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(
        AbilitiesTemplate
    )
    for main_class in MainClass:
        scraper_wiki_class(
            main_class, Path("scraped_data/main_class_abilities"), llm=llm
        )
