import requests
import json

from jsonStucture import pullStructure

##BASED ON https://stmorse.github.io/journal/espn-fantasy-v3.html


class api_handle:
    def __init__(self):
        # Read in keys
        with open("sensitive_info.json") as f:
            sensitive_data = json.load(f)

        with open("metadata.json") as f:
            self.metadata = json.load(f)

        league_id = sensitive_data["league_id"]
        year = 2021
        self.url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"
        # self.url = f"https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?seasonId={year}"

        # COOKIES
        espn_s2 = sensitive_data["espn_s2"]
        swid = sensitive_data["swid"]
        self.cookies = {
            "swid": f"{sensitive_data['swid']}",
            "espn_s2": f"{sensitive_data['espn_s2']}",
        }

    def make_request(self, url=None, params=None):
        if not url:
            url = self.url
        return requests.get(url, cookies=self.cookies, params=params).json()

    def download_views(self):
        for view in self.metadata["view_enpoints"]:
            data = self.make_request(params={"view": view})
            save_data(view, data)
            save_data(view + "_structure", pullStructure(data))


def save_data(file_name, data):
    with open(f"{file_name}.json", "w") as f:
        f.write(json.dumps(data))


def main():
    api = api_handle()
    # url = f"{api.url}?view=mMatchup"
    # params = {"view": "mMatchup"}
    # save_data("data2", api.make_request(url, params))
    api.download_views()


if __name__ == "__main__":
    main()
