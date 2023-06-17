import json

name_numbers = {}

for i in range(1, 5):
    file_path = f"profiles/mydata{i}.json"

    try:
        with open(file_path, 'r') as f:
            json_object = json.load(f)
            name = json_object['info']['name']
            print("Name:", name)

            name_numbers[f"name_number{i}"] = name  # Store name in the dictionary

    except FileNotFoundError:
        print(f"File {file_path} not found. Continuing to the next file.")
        continue

# Print all name_numbers
for i in range(1, 5):
    var_name = f"name_number{i}"
    value = name_numbers.get(var_name)
    if value is not None:
        print(f"{var_name}: {value}")
    else:
        value = None
        print(f"{var_name} is not defined. Therefore: {value}")
