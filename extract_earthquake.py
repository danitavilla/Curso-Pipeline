import requests
import pandas as pd
from datetime import datetime, timedelta
import os

# testing change

def process_earthquake_data():

    today_date = datetime.now()
    timeDelta = timedelta(days=1)
    #Date 15 days ago
    fifteen_days_ago = today_date - timedelta(days=15)
    start_time = fifteen_days_ago.strftime("%Y-%m-%d")
    end_time = today_date.strftime("%Y-%m-%d")

    # Define the API endpoint (Follow the link (cmd + click)). Consider Pagination of the specific page
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_time}&endtime={end_time}"

    #Send a GET request to the API endpoint
    response = requests.get(url)

   # print(response.json())
    print(response.status_code)

    #Create a list of dictionaries containing relevant data
    earthquakes = []

    #Check if the request was successful
    # 200 code means everything is OK with the URL
    if response.status_code == 200:
        #Parse the response content as JSON
        data = response.json()

        #   Extract earthquake features
        features = data["features"]
        date = today_date.strftime("%Y_%m_%d")
        filename = f"earthquake_{date}.csv"

        for feature in features:
            properties = feature["properties"]
            geometry = feature["geometry"]
            earthquake = {
                "time": properties["time"],
                "place": properties["place"],
                "magnitude": properties["mag"],
                "longitude": geometry["coordinates"][0],
                "latitude": geometry["coordinates"][1],
                "depth": geometry["coordinates"][2],
                "file_name": filename,
            }
            earthquakes.append(earthquake)
# Converrt the list of dictionaries to a data frame
        df = pd.DataFrame(earthquakes)

#Check if the file exist. If it exists, remove it
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File {filename} removed.")

# Now create a new file
        df.to_csv(filename, index=False)
        print(f"File {filename} created and written to.")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

def main():
    process_earthquake_data()


if __name__ == "__main__":
    main()