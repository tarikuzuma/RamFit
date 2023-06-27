#A file where the defaults of the application are listed.
#This includes the icons, color theme of the application, and etc.
import json

#Function changes color scheme depending on dark or light mode.
def read_theme(): 
    with open("settings/theme.json", 'r') as f:
        data = json.load(f)
        theme = data['theme']
        if theme == "light":
            return "#F5F5F5", "#67B678", "#C34C4C", "#7EDBB4", "#DCB349", "#A25EC3", "#ffffff", "#cccccc"
        elif theme == "dark":
            return "#2c4c3b", "#516f55", "#885a57", "#455a50", "#9f8f6f", "#b1a1b7", "#427258", "#243f30"
        
THEME_COLOR, BUTTON_COLOR, BUTTON_COLOR1, BUTTON_COLOR2,  BUTTON_COLOR3, BUTTON_COLOR4, LIST_COLOR, LIST_HIGHLIGHT = read_theme()

ICON = "program_files\images\logo.png"

'''
THEME_COLOR = "#F5F5F5"    #Sets background color
BUTTON_COLOR = "#67B678"    #Sets button color
BUTTON_COLOR1 = "#C34C4C"   #Sets button1 color
BUTTON_COLOR2 = "#7EDBB4"
BUTTON_COLOR3 = "#DCB349"
BUTTON_COLOR4 = "#A25EC3"
'''

FONT = "Poppins"

# Height is based on Nexus 5X viewport
HEIGHT = 732
WIDTH = 412

''' 
    Dont forget to add:

    MainWindow.resize(WIDTH, HEIGHT)
    MainWindow.setFixedWidth(WIDTH)
    MainWindow.setFixedHeight(HEIGHT)
    MainWindow.setMaximumWidth(WIDTH)
    MainWindow.setMaximumHeight(HEIGHT)
'''

