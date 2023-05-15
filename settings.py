class NightModeDetector:
    #OOP to detect if nightmode or not (for practice pruposes)
    def __init__(self, mode):
        self.mode = mode

    def is_night(self):
        if self.mode == "night":
            return True
        else:
            return False
        
def detectMode():
    #Function to detect if user is in night mode
    mode = input("Pseudocode to detect if app is in day or night: ")
    detect = NightModeDetector(mode)
    if detect.is_night():
        print ("You are in night mode")
    else:
        print("You are not in night mode")
    

def main():
    print ("1. Change to Night/Light Mode")
    print ("2. Delete All Data")
    print ("3. About Us")
    print ("4. Retrn to Main")

    while True:
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            detectMode()

        if ch == 2:
            #Delete all files in folder
            print("Test")

        if ch == 3:
            #About Us
            print("About Us.")

        if ch == 4:
            #Return to menu
            print ("")
            break