import csv

# Open the CSV file
file_name = "data.csv"
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    row_count = 0

# Count rows
for row in reader:
    row_count += 1
    print("Total number of rows in the CSV file:", row_count)

#Write a Python program to convert the JSON array into a CSV file

import json
import csv

# Open and read the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Open CSV file for writing
with open('data.csv', 'w', newline='') as csv_file:

# Get field names (keys from JSON objects)
    fieldnames = data[0].keys()

writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

# Write header
writer.writeheader()

# Write rows
writer.writerows(data)

print("JSON data successfully converted to CSV.")