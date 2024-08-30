from __future__ import annotations

from enum import Enum
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)
from src.DND_character_creator.choices.class_creation.character_class import (
    subclasses,
)  # noqa: E501
from src.DND_character_creator.wiki_scraper.AbilityTemplate import (
    AbilitiesTemplate,
)

url = "https://dnd5e.wikidot.com/{}:{}"


def scraper_wiki_subclass_class(
    main_class: MainClass, sub_class: Enum, output_dir: Path, llm
):
    main_class_path = output_dir.joinpath(main_class.value)
    if not main_class_path.exists():
        main_class_path.mkdir()
    sub_class_path = main_class_path.joinpath(sub_class.value)
    if sub_class_path.exists():
        return
    request_url = url.format(
        main_class.value.lower(),
        sub_class.value.lower()
        .replace("path of the ", "")
        .replace("path of ", "")
        .replace("college of ", "")
        .replace(" domain", "")
        .replace("circle of the ", "")
        .replace("circle of ", "")
        .replace("way of the ", "")
        .replace("oath of the ", "")
        .replace("oath of ", "")
        .replace(" conclave", "")
        .replace("school of ", "")
        .replace("way of ", "")
        .replace(" ", "-"),
    )
    response = requests.get(request_url)
    if response.status_code != 200:
        raise ValueError(f"Wrong status code {request_url}")
    sub_class_path.mkdir()
    content = response.content.decode()
    soup = BeautifulSoup(content, "html.parser")

    page_struct = str(soup.find("div", id="page-content"))
    abilities_result = llm.invoke(
        "Extract data about abilities of a sub_class from page content:\n\n"
        + page_struct
    )
    for ability in abilities_result.abilities:
        ability_path = sub_class_path.joinpath(f"{ability.name}.json")
        if ability_path.exists():
            continue
        ability_path.write_text(ability.model_dump_json(indent=2))


if __name__ == "__main__":
    llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(
        AbilitiesTemplate
    )
    for main_class in MainClass:
        for sub_class in subclasses[main_class]:
            scraper_wiki_subclass_class(
                main_class,
                sub_class,
                Path("scraped_data/sub_class_abilities"),
                llm=llm,
            )
