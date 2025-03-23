#!/bin/bash

# Fetch METAR data from NOAA 
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

# Print the first 6 receiptTime values
echo "Timestamps:"
jq -r '.[].receiptTime' aviation.json | head -n 6

# Calculate average temperature
temps=$(jq '.[].temp' aviation.json)
sum=0
count=0

for t in $temps; do
  if [[ $t != "null" ]]; then
    sum=$(awk "BEGIN {print $sum + $t}")
    count=$((count + 1))
  fi
done

if [ "$count" -gt 0 ]; then
  avg=$(awk "BEGIN {print $sum / $count}")
  echo "Average Temperature: $avg"
else
  echo "Average Temperature: N/A"
fi

# cloudiness
cloudy_count=$(jq -r '.[].clouds' aviation.json | grep -v 'CLR' | wc -l)
total_entries=$(jq length aviation.json)
half=$((total_entries / 2))
mostly_cloudy=false
if [ "$cloudy_count" -gt "$half" ]; then
  mostly_cloudy=true
fi
echo "Mostly Cloudy: $mostly_cloudy"

