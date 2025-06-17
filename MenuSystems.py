import Tools

class MainMenuSystem():
    def __init__(self):
        self.tool = Tools.Clean_Tool()

    def first_page(self):
        print("What would you like to do? (number only)") #L2
        print("1. Start Game") #L3
        print("2. Create a character") #L4
        print("3. View Help Guide") #L5
        print("4. Quit the game") #L6
        print("") #L7
        print("") #L8
        print("") #L9
        print("") #L10
        has_made_choice = False
        while(not has_made_choice):
            user_choice = input("Please enter only the number of your selection: ") #L11
            match(user_choice):
                case("1"):
                    has_made_choice = True
                case("2"):
                    has_made_choice = True
                case("3"):
                    has_made_choice = True
                case("4"):
                    has_made_choice = True
                    SystemExit(0)
                case _:
                    self.tool.Clean(2)
                    print("Unknown Choice") # Possible L10