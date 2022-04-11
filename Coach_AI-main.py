rosterList = []
stats = {}

###################################################this is where the general info about a basketball player
class Players:
    def __init__(self, name,number,age,pos,height,weight):
        self.name = name
        self.age = age
        self.pos = pos 
        self.height = height
        self.weight = weight
        self.number = number

###################################################this is where the genreal info about how that player performs on the basketball court
class Roster:
    def __init__(self,points,blocks,steals,rebounds,assists,fg,ft,threepointer,turnovers,plus_minus):
        self.points = points
        self.blocks = blocks
        self.steals = steals
        self.rebounds = rebounds
        self.assists = assists
        self.fg = fg
        self.ft = ft
        self.threepointer = threepointer
        self.turnovers = turnovers
        self.plus_minus = plus_minus

###################################################This is the main menu section, will put all options in here
def main_menu():
    
    print(" MAIN MENU ")
    print("1.   Read/Edit Roster\n2.    Search Players\n8.    Quit ")
    option_select = input()
    if(option_select == "1"):
        option_1()
    elif(option_select == "2"):
        option_2()

    elif(option_select == "8"):
        print("Goodbye")
        quit()
    else:
        print("try a valid command please")
        main_menu()
# End of Main Menu section   

main_menu()