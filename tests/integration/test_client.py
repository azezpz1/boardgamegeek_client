from boardgamegeek_client.client.client import BoardGameGeekClient


def test_get_board_game() -> None:
    client = BoardGameGeekClient()
    game = client.get_board_game(174430)  # Terraforming Mars
    assert game.name == "Gloomhaven"
