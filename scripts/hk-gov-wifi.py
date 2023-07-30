import os
from urllib.request import urlopen
import json
import csv

def get_info():
    """ returns an array of Wi-Fi Hotspot objects

    Returns:
        array: an array of Wi-Fi Hotspot Objects
    """
    url = "https://www.ogcio.gov.hk/en/our_work/community/common_wifi_branding/fixed-wi-fi-hk-locations.json"

    response = urlopen(url)

    return json.loads(response.read())

def create_csv(data):        
    with open("output.csv", "w", encoding="utf-8-sig", newline="") as csvfile:
        fieldnames = ["LocationID", "OrganisationCode", "LocationNameEN", "VenueTypeEN", "AddressEN", "Latitude", "Longitude", "SSID", "NumberOfHotspots", "MoreInformationEN", "MoreInformationLinkEN", "InWifiMap"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for info in data:
            info.update({"InWifiMap": False})
            writer.writerow(info)

def main():
    data = get_info()

    create_csv(data)

if __name__ == "__main__":
    main()