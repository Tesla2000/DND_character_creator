from __future__ import annotations

from collections import defaultdict

from src.DND_character_creator.choices.class_creation.character_class import (
    MainClass,
)

fighter_ability_score_improvements = [4, 6, 8, 12, 14, 16, 19]
normal_ability_score_improvements = [4, 8, 12, 16, 19]
rogue_ability_score_improvements = [4, 8, 10, 12, 16, 19]
main_class2ability_score_improvements = defaultdict(
    lambda: normal_ability_score_improvements,
    {
        MainClass.FIGHTER: fighter_ability_score_improvements,
        MainClass.ROGUE: rogue_ability_score_improvements,
    },
)
