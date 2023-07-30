# Scripts
The following are scripts that help populate the [wifi-map-hk.csv](https://github.com/yilverdeja/wifi-map-tracker-hk/wifi-map-hk.csv).

## HK Gov WiFi
The Office of the Government Chief Information Officer provides a [Wi-Fi.HK data set](https://data.gov.hk/en-data/dataset/hk-ogcio-ogcio_hp-wi-fi-hk-locations) of all the fixed and non-fixed free Wi-Fi hotspots in Hong Kong. 

The `hk-gov-wifi.py` script retrieves information from the [fixed-wifi-locations.json](https://www.ogcio.gov.hk/en/our_work/community/common_wifi_branding/fixed-wi-fi-hk-locations.json) file, and adds it into a csv with only the english data columns:
* LocationID
* OrganisationCode
* LocationNameEN
* VenueTypeEN
* AddressEN
* Latitude
* Longitude
* SSID
* NumberOfHotspots
* MoreInformationEN
* MoreInformationLinkEN

In addition, it adds an additional `InWifiMap` data field initially set to False.