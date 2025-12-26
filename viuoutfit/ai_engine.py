import csv

dataset = []
with open('fashion_dataset.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dataset.append(row)


user_input = {
    "gender": "female",
    "body_type": "hourglass",
    "occasion": "party",
    "weather": "summer",
    "style": "street",
    "color": "black"
}


matches = []
for row in dataset:
    if (
        row['gender'] == user_input['gender'] and
        row['body_type'] == user_input['body_type'] and
        row['occasion'] == user_input['occasion'] and
        row['weather'] == user_input['weather'] and
        row['style'] == user_input['style'] and
        (row['top_color'] == user_input['color'] or row['bottom_color'] == user_input['color'])
    ):
        matches.append(row)


if matches:
    print("Matching outfits found:")
    for match in matches:
        print(match)
else:
    print("No matching outfits found.")
