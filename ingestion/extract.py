import requests

BASE_URL = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole"
TIMEOUT_SECONDS = 30


def fetch_stations(endpoint: str) -> list[dict]:
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()["data"]["stations"]


status = fetch_stations("station_status.json")
info = fetch_stations("station_information.json")

print(len(status), status[0])
print(len(info), info[0])