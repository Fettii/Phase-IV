import option_1 as opt1
import option_2 as opt2
import option_3 as opt3

rosterList = []
stats = {}

###################################################this is where the general info about a basketball player
class Players:
    def __init__(self, name,age,pos,height,weight):
        self.name = name
        self.age = age
        self.pos = pos 
        self.height = height
        self.weight = weight

###################################################this is where the genreal info about how that player performs on the basketball court
class Roster:
    def __init__(self,points,blocks,steals,rebounds,assists):
        self.points = points
        self.blocks = blocks
        self.steals = steals
        self.rebounds = rebounds
        self.assists = assists


###################################################This is the main menu section, will put all options in here
def central():
    
    print(" MAIN MENU ")
    print("\n1.  Read\Edit Roster\n2.  Search Players\n3.   Sort Players\n8.  Quit\n")
    option_select = input()
    if(option_select == "1"):
        opt1.add_search_menu()
    elif(option_select == "2"):
        opt2.menu()
    elif(option_select == "3"):
        opt3.menu()
    elif(option_select == "8"):
        print("Goodbye")
        quit()
    else:
        print("try a valid command please")
        central()
# End of Main Menu section   

central()