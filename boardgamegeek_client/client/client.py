import xml.etree.ElementTree as ET
from typing import Optional, Union, cast

import httpx

from ..models.boardgame import BoardGame


def _get_value(
    element: Optional[ET.Element],
    key: str,
    attribute: Optional[str] = None,
    default: Union[str, int] = "",
) -> Union[str, int]:
    if element is None:
        return default

    child = element.find(key)
    if child is None:
        return default

    if attribute:
        return child.attrib.get(attribute, default)

    return child.text or default


class BoardGameGeekClient:
    def __init__(self) -> None:
        self.base_url = "https://boardgamegeek.com/xmlapi2"

    def get_board_game(self, bgg_id: int) -> BoardGame:
        response = httpx.get(f"{self.base_url}/thing?id={bgg_id}")
        response.raise_for_status()

        root = ET.fromstring(response.content)
        game = root.find("item")

        return BoardGame(
            bgg_id=bgg_id,
            name=cast(str, _get_value(game, "name", attribute="value")),
            description=cast(str, _get_value(game, "description")),
            year_published=int(
                cast(str, _get_value(game, "yearpublished", attribute="value"))
            ),
            min_players=int(
                cast(str, _get_value(game, "minplayers", attribute="value"))
            ),
            max_players=int(
                cast(str, _get_value(game, "maxplayers", attribute="value"))
            ),
            playing_time=int(
                cast(str, _get_value(game, "playingtime", attribute="value"))
            ),
            min_play_time=int(
                cast(str, _get_value(game, "minplaytime", attribute="value"))
            ),
            max_play_time=int(
                cast(str, _get_value(game, "maxplaytime", attribute="value"))
            ),
            age=int(cast(str, _get_value(game, "minage", attribute="value"))),
            image=cast(str, _get_value(game, "image")),
            thumbnail=cast(str, _get_value(game, "thumbnail")),
        )
