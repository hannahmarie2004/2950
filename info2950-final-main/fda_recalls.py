# Downloads FDA food recall records from the FDA iRES API
# and saves the raw data used in this project.

import requests
import pandas as pd
import json
import time
from getpass import getpass

authorization_user = input("FDA Authorization-User: ")
authorization_key = getpass("FDA Authorization-Key: ")

url = "https://www.accessdata.fda.gov/rest/iresapi/recalls/"

headers = {
    "Authorization-User": authorization_user,
    "Authorization-Key": authorization_key,
    "Content-Type": "application/x-www-form-urlencoded"
}

columns = [
    "productid",
    "recalleventid",
    "producttypeshort",
    "firmlegalnam",
    "recallinitiationdt",
    "centerclassificationtypetxt",
    "productdescriptiontxt",
    "productshortreasontxt",
    "recallnum",
    "phasetxt",
    "enforcementreportdt"
]

all_records = []

start = 1
rows = 4000

print("\nStarting FDA recall download...\n")

while True:
    payload = {
        "displaycolumns": ",".join(columns),
        "filter": "[{'centercd':['CFSAN','HFP']}]",
        "start": start,
        "rows": rows,
        "sort": "productid",
        "sortorder": "asc"
    }

    signature = str(time.time_ns())

    response = requests.post(
        url,
        headers=headers,
        params={"signature": signature},
        data={"payLoad": json.dumps(payload)},
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    if result.get("MESSAGE", "").lower() != "success":
        print("FDA API error:")
        print(result)
        break

    batch = result.get("RESULT", [])

    if not batch:
        break

    all_records.extend(batch)

    print(f"Downloaded {len(all_records):,} records")

    if len(batch) < rows:
        break

    start += len(batch)

    time.sleep(0.5)

df = pd.DataFrame(all_records)

df.to_csv(
    "phase2/data/fda_food_recalls_raw.csv",
    index=False
)

print("\nDONE")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFile created:")
print("phase2/data/fda_food_recalls_raw.csv")