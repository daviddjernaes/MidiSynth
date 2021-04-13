class Util:
    def mainMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\nMain Menu:\n")
            print("1 - Record Sample")
            print("2 - Sample Library")
            print("3 - Exit Program")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def recSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\nSampling Menu:\n")
            print("1 - Start recording")
            print("2 - Play sample with MIDI device")
            print("3 - Return to Main Menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def newSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 3 < menuOption):
            print("\n1 - Preview sample")
            print("2 - Save sample")
            print("3 - Discard sample")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 3 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def sampleLibMenu(self):
        menuOption = 0

        while(1 > menuOption or 4 < menuOption):
            print("\nSample Library Menu:\n")
            print("1 - Display sample list")
            print("2 - Select sample")
            print("3 - Delete sample")
            print("4 - Return to Main Menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 4 < menuOption):
                print("\n***Option out of range***")

        return menuOption

    def selectSampleMenu(self):
        menuOption = 0

        while(1 > menuOption or 4 < menuOption):
            print("\n1 - Preview current sample")
            print("2 - Load current sample to MIDI device")
            print("3 - Delete current sample")
            print("4 - Return to previous menu")

            menuOption = int(input("\nEnter menu option here: "))
            if(1 > menuOption or 4 < menuOption):
                print("\n***Option out of range***")

        return menuOption