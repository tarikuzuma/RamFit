import json
import os

def read_json_files():
    profiles_folder = "profiles"
    active_profile = None
    for file in os.listdir(profiles_folder):
        if file.endswith(".json"):
            with open(os.path.join(profiles_folder, file)) as f:
                profile = json.load(f)
                if profile["status"] == "active":
                    active_profile = file
    return active_profile


active_profile = read_json_files()
if active_profile is not None:
    print("The active profile is:", active_profile)
else:
    print("No active profile found.")
