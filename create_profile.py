import json
import os


#TODO: Make it so that user can ONLY create max of 4 profiles.

class Create_Person: #create json file with data
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self): #prints name, age, and weight (test)
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")

    def add_weight(self, heavy): #adds weight with current weight
        current = self.weight + heavy
        return current
    
    def save_json(self, filename):
        folder = "profiles"
        os.makedirs(folder, exist_ok=True)  # Create the "profiles" folder if it doesn't exist
        file_path = os.path.join(folder, filename)  # Append folder path to the filename

        person_dict = {'name': self.name, 'age': self.age, 'weight': self.weight}
        with open(file_path, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))
    
    def load_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        
        self.name = data['name']
        self.age = data['age']
        self.weight = data['weight']


def main():
    # Parse command line arguments
    name = input("Input Name: ")
    age = int(input("Input Age: "))
    weight = int(input("Input weight: "))

    person = Create_Person(name, age, weight)
    person.print_info
    person.add_weight(500) #NOTE: TEST

    person.save_json("profile.json")  # The JSON file will be saved inside the "profiles" folder
    person.load_json("profiles/profile.json")  # Load the JSON file from the "profiles" folder

    person.print_info()