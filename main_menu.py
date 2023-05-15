import settings

while True:
    #Initialize main Menu
    print("Ramfit Main Menu")
    print("1. Choose Profile")
    print("2. Create Profile")
    print("3. Settings")
    print("4. Quit\n")

    choice = int(input("Choose an option: "))
    if choice == 1:
        #Initialize Profile Menu
        print ("Profile1")
        pass
    elif choice == 2:
        #Initialize Profile Menu
        print ("Profile2")
        pass
    elif choice == 3:
        #Calls Settings
        settings.main()
    elif choice == 4:
        #Quit
        print ("Good Bye!")
        exit()
    else:
        #Invalid option
        print("Invalid option.")