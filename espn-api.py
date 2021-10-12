import requests
import json

# LEAGUE INFO
league_id = 684262176
year = 2021
url = f"https://fantasy.espn.com/apis/v3/games/ffl/seasons/{year}/segments/0/leagues/{league_id}"
# url = f"https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{str(league_id)}?seasonId={str(year)}"
# espn_s2_decoded = "AEBqic7Z99AhbhyuSH4T4K2uGtKtwKRDhpXDUlcI0hRFykc6jY7NAdCAq8CKnBqxXICDc8cq8rUWXRkt71X8+4kKgWEgimvXcDwz7Dadd5Nq2o1jl/KV2MycSgOyyNcb4sLcHI1JaJQIBEEjt/K6Ijs5LmJ86RnW9FCmErT48VM4oxITflAJDMoLlt+6gA4lgAHozcDgom8Y75Ww07fIPb6AyRJ/ksU+BmvFBLlz/cp3JHw5dR/rPz4ljcJqU94/8GvX/CANF+WCTKkeh+zeolxKYdoCi/DRWXWM2rY2OLDAgQ=="

# COOKIES
espn_s2 = "AEBqic7Z99AhbhyuSH4T4K2uGtKtwKRDhpXDUlcI0hRFykc6jY7NAdCAq8CKnBqxXICDc8cq8rUWXRkt71X8%2B4kKgWEgimvXcDwz7Dadd5Nq2o1jl%2FKV2MycSgOyyNcb4sLcHI1JaJQIBEEjt%2FK6Ijs5LmJ86RnW9FCmErT48VM4oxITflAJDMoLlt%2B6gA4lgAHozcDgom8Y75Ww07fIPb6AyRJ%2FksU%2BBmvFBLlz%2Fcp3JHw5dR%2FrPz4ljcJqU94%2F8GvX%2FCANF%2BWCTKkeh%2BzeolxKYdoCi%2FDRWXWM2rY2OLDAgQ%3D%3D"
swid = "{351EA1B1-965A-44FE-9EA1-B1965AC4FE6A}"


r = requests.get(url, cookies={"swid": f"{swid}", "espn_s2": f"{espn_s2}"})
# r = requests.get(url)
data = r.json()

with open("data.json", "w") as f:
    f.write(json.dumps(data))
