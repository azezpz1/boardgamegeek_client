from dataclasses import dataclass


@dataclass
class BoardGame:
    bgg_id: int
    name: str
    description: str
    year_published: int
    min_players: int
    max_players: int
    playing_time: int
    min_play_time: int
    max_play_time: int
    age: int
    image: str
    thumbnail: str
