import json
import os

class ProfileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.profile_data = self.read_profile()

    def read_profile(self):
        with open(self.file_path, 'r') as f:
            json_data = json.load(f)

        return json_data
    
    def is_exist(self, choice):
        return choice == self.profile_data['name']


def main():
    try:
        file_path = os.path.join('profiles', 'profile.json')
        reader = ProfileReader(file_path)

        print("1. ", reader.profile_data['name'])

        choice = input("Choose a profile: ")
        if reader.is_exist(choice):
            print("True")
        else:
            print("False")
    except:
        print("\n No Profile Exists \n")

'''
if __name__ == '__main__':
    main()
'''