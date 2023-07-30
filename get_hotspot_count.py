import csv
SEARCH_CSV_FILES = ["wifi-map-hk.csv"]

def get_count():
    added = 0
    not_added = 0
    for file in SEARCH_CSV_FILES:
        csv_file = open(file, "r", encoding="utf-8")
        csv_input = csv.DictReader(csv_file)

        for obj in csv_input:
            added += 1 if obj["InWifiMap"] == "True" else 0
            not_added += 0 if obj["InWifiMap"] == "True" else 1
    
    return added, not_added

if __name__ == "__main__":
    added, not_added = get_count()
    total = added + not_added
    added_percentage = round(added/total*100, 2)
    not_added_percentage = round(not_added/total*100, 2)

    print(f"**Total:** {total}\n\n**Added:** {added} ({added_percentage}%)\n\n**Not Added:** {not_added} ({not_added_percentage}%)")
