import json
import requests
import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_match(year: int, matchid: str, event: str = "ao", return_single_dict: bool = False) -> json:
    """
    Download court vision data in json format.

    If matchid = "all", download all matches. Otherwise use codes as below.
    Roland Garros
        Men's Singles   	SM### 	SM001 (Final match)
        Women's Singles 	SD### 	SD127 (First match)
        Men's Doubles   	DM### 	DM001 (Final)
        Women's Doubles 	DD### 	DD001 (Final)
        Mixed Doubles    	MX### 	MX001 (Final)
    Australian Open
        Men's Singles 	    MS### 	MS701 (Final match)
        Women's Singles 	WS### 	WS001 (First match)
        Men's Doubles 	    MD### 	MD601 (Final)
        Women's Doubles 	WD### 	WD001 (Final)
        Mixed Doubles 	    XD### 	XD501 (Final)

    Parameters
    ----------
    year: float
        Year of match
    matchid: str
        Match ID. See description. "all" to download everything.
    event: str
        ao or rg for australian open or roland garros
    return_single_dict: bool
        Used in conjunction with a single match. Return the data directly.

    Returns
    -------
    The python dict and a json file saved to the current dir

    """
    event_dict = {"rg": "roland_garros", "ao": "australian_open"}
    savedir = os.path.join("courtvision_data", event_dict[event], str(year))
    Path(savedir).mkdir(parents=True, exist_ok=True)

    match_codes = [matchid]

    draws = {"rg": ["SM", "SD", "DM", "DD", "MX"],
             "ao": ["MS", "WS", "MD", "WD", "XD"]
             }

    if matchid == "all":
        logger.info(f"Downloading all of {event}. Sit tight...")
        match_codes = []

        # For Roland Garros the digit is the match number starting from the biggest number
        # and working toward 1 for the final.
        if event == "rg":
            for draw in draws[event]:
                for i in range(1, 128):
                    if i < 10:
                        prefix = "00"
                    elif i < 100:
                        prefix = "0"
                    else:
                        prefix = ""
                    match_code = draw+prefix+str(i)
                    match_codes.append(match_code)

        # For the Australian Open, the first digit is the round (beginning with 1 and working up) and
        # then a 2-digit match number starting at 1 and working up within each round.
        elif event == "ao":
            rounds = [1, 2, 3, 4, 5, 6, 7]
            matches = [64, 32, 16, 8, 4, 2, 1]
            for draw in draws[event]:
                for round, match in zip(rounds, matches):
                    for m in range(1, match+1):
                        if m < 10:
                            prefix = "0"
                        else:
                            prefix = ""
                        match_code = draw+str(round)+prefix+str(m)
                        match_codes.append(match_code)
        else:
            logger.error("Unknown tournament. Select ao or rg.")
            return 1

    for m in match_codes:
        logger.info(f"Downloading {m}...")
        if event == "rg":
            url = f"https://itp-rg-sls.infosys-platforms.com/prod/api/court-vision/year/{year}/eventId/520/matchId/{m}/pointId/0_0_0"
        else:
            url = f"https://itp-ao.infosys-platforms.com/api/court-vision/year/{year}/eventId/580/matchId/{m}/pointId/0_0_0"

        try:
            data = requests.get(url).json()
        except Exception:
            logger.warning(f'Issue downloading {m} for {event}')
            continue
        # Check if returned object is empty. Don't need to save it if it is.
        if len(data["courtVisionData"]) == 0:
            continue
        filename = os.path.join(savedir, f'{year}-{m}-{event}.json')
        with open(filename, 'w') as f:
            json.dump(data, f)

        if return_single_dict:
            return data
