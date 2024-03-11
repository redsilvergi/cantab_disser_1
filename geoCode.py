import json
import requests
import csv
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import time

load_dotenv()
api_id = os.getenv("ID")
api_key = os.getenv("KEY")

# tmp = pd.read_csv('./cord3.csv',low_memory=False)
# tmp1 = pd.read_csv('./csv/mrgd/mrgd_flat23.csv',low_memory=False)
# tmp2 = pd.read_csv('./csv/mrgd/mrgd_officetel23.csv',low_memory=False)
# tmp3 = pd.read_csv('./csv/mrgd/mrgd_multi23.csv',low_memory=False)
# mrgd = pd.read_csv("./csv/mrgd/mrgd.csv", low_memory=False)
# addresses = mrgd["address"].unique()  # ["개포로109길 5","언주로 103","언주로 3"]

addresses = np.load('./csv/mrgd/addresses.npy')
# addresses = addresses[33178:]
url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
headers = {
    "X-NCP-APIGW-API-KEY-ID": api_id,
    "X-NCP-APIGW-API-KEY": api_key,
}
# print(addresses)

cord_file_path = os.path.join(os.getcwd(), "./res_tmp/cord.csv")
with open(cord_file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["address", "lon", "lat"])
    start_time = time.time()
    for idx, qry in enumerate(addresses, start=1):
        params = {"query": qry}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.content)
            if 'addresses' in data and data["addresses"]:
                lon = data["addresses"][0]["x"]
                lat = data["addresses"][0]["y"]
                # addressR = (
                #     data["addresses"][0]["addressElements"][4]["longName"]
                #     + " "
                #     + data["addresses"][0]["addressElements"][5]["longName"]
                # )
                # print(f"lon: {lon}, lat: {lat}")
                writer.writerow([qry, lon, lat])
                end_time = time.time()
                time_spent = end_time - start_time
                print(
                    f"{qry} found!!#! Current: {idx}/{len(addresses)}. {time_spent:.2f} seconds passed"
                )
            else:
                print(f"no data found for {qry}")
        else:
            print(f"Error: {response.status_code}")
print(f"path: {cord_file_path}")

# mrtst = pd.read_csv('./cord.csv',low_memory=False)
# mrtst.columns =['address','lon','lat']
# az = tmp2.merge(
#     mrtst,
#     on=["address"],
#     how="left",
#     suffixes=("_tmp", "_mrtst"),
# )

# scp -i C:/Users/eungi/Desktop/eungi_dt/pem/geoc.pem ubuntu@ec2-13-125-171-114.ap-northeast-2.compute.amazonaws.com:/home/ubuntu/apps/geoCode/cord.csv C:/Users/eungi/Desktop/eungi_dt/ec2dwnld/
