import json


def get_team_roster():
    with open("data2.json", "r") as f:
        data = json.load(f)

    teams = {
        team["id"] : [
            player["playerPoolEntry"]["player"]["fullName"]
            for player in team["roster"]["entries"]
        ]

        for team in data["teams"]
    }

    for t in teams:
        print(teams[t])


get_team_roster()






"""
{
    key : value
}
[

]

"""

# { x is odd -> {1,2,3} }

# {1,2,3}