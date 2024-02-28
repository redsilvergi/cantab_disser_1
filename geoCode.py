import json
import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv("ID")
api_key = os.getenv("KEY")

# addresses = ["자양로 104", "남부순환로356길 70"]
addresses = [
    "개포로109길 5",
    "언주로 103",
    "언주로 3",
    "개포로 311",
    "개포로 264",
    "개포로 307",
    "개포로109길 69",
    "삼성로 14",
    "삼성로4길 17",
    "개포로 516",
    "언주로 110",
    "삼성로 11",
    "선릉로 8",
    "개포로109길 21",
    "논현로2길 38",
    "개포로109길 9",
    "개포로 411",
    "개포로31길 9-5",
    "개포로 303",
    "언주로 107",
    "개포로 409",
    "봉은사로11길 12",
    "강남대로112길 41",
    "학동로38길 22",
    "논현로111길 39",
    "학동로46길 32",
    "학동로30길 21",
    "언주로116길 6",
    "언주로130길 30",
    "언주로146길 18",
    "학동로46길 38",
    "논현로124길 8",
    "봉은사로51길 36",
    "학동로 165",
    "강남대로146길 28",
    "도산대로50길 43",
    "언주로 604",
    "언주로136길 21",
    "강남대로120길 58",
    "학동로43길 30",
    "도산대로 232",
    "언주로 641",
    "언주로 720",
    "논현로124길 28",
    "봉은사로29길 35",
]
url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
headers = {
    "X-NCP-APIGW-API-KEY-ID": api_id,
    "X-NCP-APIGW-API-KEY": api_key,
}

cord_file_path = os.path.join(os.getcwd(), "cord2.csv")
with open(cord_file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["address1", "lon", "lat"])

    for qry in addresses:
        params = {"query": qry}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.content)
            if data["addresses"]:
                lon = data["addresses"][0]["x"]
                lat = data["addresses"][0]["y"]
                # addressR = (
                #     data["addresses"][0]["addressElements"][4]["longName"]
                #     + " "
                #     + data["addresses"][0]["addressElements"][5]["longName"]
                # )
                # print(f"lon: {lon}, lat: {lat}")
                writer.writerow([qry, lon, lat])
            else:
                print(f"no data found for {qry}")
        else:
            print(f"Error: {response.status_code}")
print(f"path: {cord_file_path}")
