

# Return over multiple lines "\x1B[2A" or "\x1B[3A" for 2 and 3 lines
# clear rest of carriage "\x1B[0K"

class Clean_Tool():
    def __init__(self):
        pass
        
    def Clean(self, lines_to_clean=11):
        #Clean Lines
        for i in range(0,lines_to_clean):
            print("\x1B[1A",end = "") # L1
            print("\x1B[0K",end = "")
