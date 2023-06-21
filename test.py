import json

workout_names = []

def read_program(difficulty, program):

    filepath = None #Flag Case. File path of JSON. Example: "program_files/beginner/arms.json"
    workout_type = None #Flag Case. Type of workout. Example: "beginner_arms"
    if difficulty == 1 and program =="arms":
        workout_type = "beginner_arms"
        filepath = "program_files/beginner/arms.json"
    else:
        print("Unreadable")
        return

    print ("File path: ", filepath, " : ", workout_type)
    try:
        with open(filepath, "r") as f:
            json_object = json.load(f)

            print (json_object)
            workout = json_object[workout_type]  #GAGOO WHU IS IT INVERTEDDD

            #Print the name of each exercise in the workout
            for exercise in workout:
                exercise_name = exercise["name"]
                workout_names.append(exercise_name)

    except FileNotFoundError:
        print("File not found:", filepath)

    except json.JSONDecodeError:
        print("Invalid JSON format in file:", filepath)

read_program(1, "arms")
print(*workout_names)