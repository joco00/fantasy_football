import json
import pandas as pd
import matplotlib as plt

from espn_api import api_handle


# df = [[
#         game['matchupPeriodId'],
#         game['home']['teamId'], game['home']['totalPoints'],
#         game['away']['teamId'], game['away']['totalPoints']
#     ] for game in d['schedule']]
# df = pd.DataFrame(df, columns=['Week', 'Team1', 'Score1', 'Team2', 'Score2'])
# df['Type'] = ['Regular' if w<=14 else 'Playoff' for w in df['Week']]
# df.head()


def main():
    api = api_handle()
    url = f"{api.url}?view=mMatchup"
    params = {"view": "mMatchup"}
    data = api.make_request(url, params)

    df = [
        [
            game["matchupPeriodId"],
            game["home"]["teamId"],
            game["home"]["totalPoints"],
            game["away"]["teamId"],
            game["away"]["totalPoints"],
        ]
        for game in data["schedule"]
    ]
    df = pd.DataFrame(df, columns=["Week", "Team1", "Score1", "Team2", "Score2"])
    df["Type"] = ["Regular" if w <= 14 else "Playoff" for w in df["Week"]]
    print(df.head())

    df3 = df.assign(
        Margin1=df["Score1"] - df["Score2"], Margin2=df["Score2"] - df["Score1"]
    )
    df3 = (
        df3[["Week", "Team1", "Margin1", "Type"]]
        .rename(columns={"Team1": "Team", "Margin1": "Margin"})
        .append(
            df3[["Week", "Team2", "Margin2", "Type"]].rename(
                columns={"Team2": "Team", "Margin2": "Margin"}
            )
        )
    )
    print(df3.head())

    # fig, ax = plt.subplots(1, 1, figsize=(16, 6))
    # order = [14, 13, 9, 1, 15, 12, 3, 4, 2, 5]
    # sns.boxplot(
    #     x="Team", y="Margin", hue="Type", data=df3, palette="muted", order=order
    # )
    # ax.axhline(0, ls="--")
    # ax.set_xlabel("")
    # ax.set_title("Win/Loss margins")
    # plt.show()


if __name__ == "__main__":
    main()
