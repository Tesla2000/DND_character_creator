from __future__ import annotations

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from langchain_openai import ChatOpenAI

from src.DND_character_creator.choices.main_race import MainRace
from src.DND_character_creator.wiki_scraper.MainRaceTemplate import (
    MainRaceTemplate,
)

url = "https://dnd5e.wikidot.com/lineage:{}"


def scraper_wiki_race(race: MainRace, output_dir: Path):
    race_path = output_dir.joinpath("race.value")
    if race_path.exists():
        return
    race_path.mkdir()
    response = requests.get(url.format(race.value.lower()))
    if response.status_code != 200:
        raise ValueError("Wrong status code")
    content = response.content.decode()
    soup = BeautifulSoup(content, "html.parser")

    page_struct = str(soup.find("div", id="page-content"))
    llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(
        MainRaceTemplate
    )
    result = llm.invoke(
        "Extract data about the class from page content:\n\n" + page_struct
    )
    for sub_race in result.sub_races:
        race_path.joinpath(f"{sub_race.name}.json").write_text(
            json.dumps(json.loads(sub_race.model_dump_json()), indent=2)
        )


if __name__ == "__main__":
    scraper_wiki_race(
        MainRace.HALF_ORC,
        Path("src/DND_character_creator/wiki_scraper/scraped_data/sub_races"),
    )
