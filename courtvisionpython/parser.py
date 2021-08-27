import pandas as pd
import numpy as np
import json


class InfoSys:
    """A parser for the InfoSys tennis data format."""

    def __init__(self, match_file):
        self.points_data = None
        self.event_type = None
        self.court_name = None
        self.court_id = None
        self.players_data = None
        self.sets_completed = None
        self.parse_data(match_file)

    def parse_data(self, match_file) -> pd.DataFrame:
        """
        Parse the InfoSys match output.

        Parameters
        ----------
        match_file: str
            Json input file

        """
        with open(match_file) as f:
            raw_data = json.load(f)["courtVisionData"][0]

        self.event_type = raw_data["eventType"]
        self.court_name = raw_data["courtName"]
        self.court_id = raw_data["courtId"]
        self.players_data = raw_data["playersData"]
        self.sets_completed = raw_data["setsCompleted"]

        vetoed_columns = ["trajectoryData", "ballHitCordinate", "ballPeakCordinate", "ballNetCordinate",
                          "ballBounceCordinate", "ballLastCordinate", "serverCordinate", "receiverCordinate",
                          "serveBounceCordinate"]

        points_data = raw_data["pointsData"]

        point_df_list = []

        for point in points_data.keys():
            point_data = points_data[point]
            dct = {k: [v] for k, v in point_data.items()}
            df = pd.DataFrame(dct)
            df = df.drop(vetoed_columns, axis=1)
            df.set_index("pointId", inplace=True)

            trajectory_data = point_data["trajectoryData"]
            trajectory_df = pd.DataFrame.from_dict(trajectory_data)
            trajectory_df["pointId"] = point_data["pointId"]
            trajectory_df.set_index("pointId", inplace=True)

            data_df = df.join(trajectory_df)
            data_df['order'] = np.arange(data_df.shape[0])

            point_df_list.append(data_df)

        final_df = pd.concat(point_df_list)

        self.points_data = final_df

    def return_points_data(self):
        """Return points data"""
        return self.points_data

    def return_event_type(self):
        """Return event type"""
        return self.event_type

    def return_court_name(self):
        """Return court_name"""
        return self.court_name

    def return_court_id(self):
        """Return court_id"""
        return self.court_id

    def return_players_data(self):
        """Return players_data"""
        return self.players_data

    def return_sets_completed(self):
        """Return sets_completed"""
        return self.sets_completed
