import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        "data/raw/live_nav_hdfc_top100.csv",
        index=False
    )

    print("Live NAV saved successfully!")

else:
    print("API request failed")