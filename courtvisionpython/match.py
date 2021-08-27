
import courtvisionpython as cvp
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_match(match_file: str):

    return Match(match_file)


class Match:
    """
    A match object contexulizing all data and providing easy-to-acess properties.
    """

    _points_data: pd.DataFrame
    """
    Data frame with all points data.
    """
    _players_data: dict
    """
    Data frame with all players data.
    """

    def __init__(self, match_file: str):

        self._points_data = None
        self._players_data = None

        self._parse_data(match_file)

    def _parse_data(self, match_file):
        parsed = cvp.InfoSys(match_file)
        self._points_data = parsed.return_points_data()
        self._players_data = parsed.return_players_data()

    @property
    def points_data(self):
        """Property to return the points/trajectory data."""
        return self._points_data

    @property
    def players_data(self):
        """Property to return the players data."""
        return self._players_data

    @property
    def player1_name(self):
        """Get first player name"""
        name = self._players_data["playerTeam"][0]["name"]
        return name

    @property
    def player1_id(self):
        """Get first player ID"""
        name = self._players_data["playerTeam"][0]["id"]
        return name

    @property
    def player1_seed(self):
        """Get first player seed"""
        name = self._players_data["playerTeam"][0]["seed"]
        return name

    @property
    def player2_name(self):
        """Get second player name"""
        name = self._players_data["opponentTeam"][0]["name"]
        return name

    @property
    def player2_id(self):
        """Get second player ID"""
        name = self._players_data["opponentTeam"][0]["id"]
        return name

    @property
    def player2_seed(self):
        """Get second player seed"""
        name = self._players_data["opponentTeam"][0]["seed"]
        return name
