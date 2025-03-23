import json
import csv

# Read JSON
with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

# CSV
with open('chacon.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'html_url', 'updated_at', 'visibility'])  # Header

    for entry in data[:5]:  # Only first 5
        name = entry.get('name', 'N/A')
        html_url = entry.get('html_url', 'N/A')
        updated_at = entry.get('updated_at', 'N/A')
        visibility = entry.get('visibility', 'N/A')
        writer.writerow([name, html_url, updated_at, visibility])
