import csv

export_data = []

# File reading
with open('sample_data.csv', 'rb') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Condition
        if row['Gender'] == 'Male':
            export_data.append(row)

# File writing
with open('sample_data_export.csv', 'wb') as file:
    fieldnames = ['Name', 'Relation', 'Gender']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in export_data:
        writer.writerow(row)
        print row