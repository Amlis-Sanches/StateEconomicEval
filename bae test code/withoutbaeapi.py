import requests
import json

# Your BEA API Key
beakey = "your-api-key-here"

# API URL for state GDP
url = f"https://apps.bea.gov/api/data?UserID={beakey}&method=GetData&datasetname=Regional&TableName=SQGDP2&GeoFips=STATE&Year=2023&ResultFormat=JSON"

# Make request
response = requests.get(url)

# Parse JSON
data = response.json()

# Extract GDP values
if "BEAAPI" in data and "Results" in data["BEAAPI"]:
    gdp_results = data["BEAAPI"]["Results"]["Data"]
    for entry in gdp_results:
        print(f"State: {entry['GeoName']}, GDP: {entry['DataValue']} ({entry['TimePeriod']})")
else:
    print("Error retrieving data:", data)
