import ast
import sys 
import fileinput

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
    print("\n1.  Read\Edit Roster\n2.  Search Players\n3.   Sort Players\nEnter 'quit' to exit program\n")
    option_select = input()
    if(option_select == "1"):
        opt1_menu()
    elif(option_select == "2"):
        opt2_menu()
    elif(option_select == "3"):
        opt3_menu()
    elif(option_select == "quit"):
        print("Goodbye")
        quit()
    else:
        print("try a valid command please")
        central()
# End of Main Menu section   

#################################################################### OPTION 1 SECTION STARTS HERE

def opt1_menu():
    user_input = input("\nPlease enter a number to select a command or type quit to exit this section\n1. Read roster\n2. Add Items\n3. Edit Items\nQuit\n")
    if(user_input == "1"):
        read_roster()
    elif(user_input == "2"):
        add_items()
    elif(user_input == "3"):
        edit_items()
    elif(user_input == "quit"):
        central()
    else:
        print("Not a option, try again buddy")
        opt1_menu()

def read_roster():
    reader = open("Roster.txt","r")
    #print(reader.readlines(),"\n")
    for line in reader.readlines():
        print("\n"+line)
    reader.close()
    opt1_menu()
    

    
def add_items():

    reader = open("Roster.txt","a")
    playerbio = input(("Please enter the asked info in this format example (Name,Age,Primary Position,Height,Weight): ") or "0")
    statbio = input(("Okay, now enter stats in a similar format ex.(Points,Rebounds,Assists,Blocks,steals): ") or "0")
    playerbio = playerbio.split(",")
    statbio = statbio.split(",")
    final = {playerbio[0] :{ "age": playerbio[1],"position": playerbio[2],"height": playerbio[3],"weight": playerbio[4],"points" : statbio[0],"rebounds": statbio[1],"assists": statbio[2],"blocks": statbio[3],"steals":statbio[4]}}
    reader.write("\n"+str(final))
    reader.close()
    opt1_menu()

    


def edit_items():
    counter = 0
    reader = open("Roster.txt","r+")
    lines = reader.readlines()
    keepGoing = True
    while keepGoing:
        new_edit = input("Please enter player's name in which you would like to edit or type 'quit' if finished editing: ")
        if(new_edit == 'quit'):
            keepGoing = False
            reader.close()
        else:
            for line in lines:  # I need to figure out how to make loop skip blank lines or just make the program exactly that amount of text lines needed, this is because it is trying to make the blank line a dict which wont work
                statChanging = True
                if line == '': #this tells program, since emtpy line is false, to skip it
                    pass
                else:
                    player_dict = ast.literal_eval(line)
                    
                    if player_dict.get(new_edit) == None:
                        print("not found")
                    else:
                        print("Found!")
                        print(player_dict.get(new_edit))
                        while statChanging:
                            stat_key = input("Which stat would you like to change? Or would you like to stop editing this playing (type 'quit')?: ")
                            if stat_key == "quit":
                                break
                            elif player_dict[new_edit].get(stat_key) == None:
                                print("This stat doesnt exsist, make sure you captitalize the first letter of what stat you want to edit (ex. 'Age')")
                            else:                               
                                new_val = input("ENTER NEW VALUE: ")
                                player_dict[new_edit].update({stat_key:new_val})                                
                                print(player_dict)
                                for line in lines:
                                    if new_edit in line:
                                        new_line = line.replace(line,str(player_dict)) + "\n"
                                        reader.write(new_line)

                                        


                                

                    counter += 1
                                
    opt1_menu()



#################################################################### OPTION 2 SECTION STARTS HERE

def opt2_menu():
    user_input = input("\nSearch Players - Please type a number or type quit to exit\n\n1. Add filter\n\n")
    if(user_input == "1"):
        add_filter()
    elif(user_input == "quit"):
        central()
    else:
        print("Sorry thats not a known command, try again")   
        opt2_menu() 
    
def add_filter(): 
    word = input("Please enter phrase to filter for:    ")
    doggy = [line for line in open('Roster.txt') if word in line]
    print(doggy)    
    
    
    opt2_menu()
    
#################################################################### OPTION 3 SECTION STARTS HERE ***OPTION 3 IS INCOMPLETE***

def opt3_menu():
    print("\nSORT MENU:\nYou can sort by typing in these filters (name,age,position,height,weight,points,rebounds,assists,blocks,steals,)) or type quit to exit ")
    user_input = input("ENTER SORT FILTER: ")
    if user_input == "name":
        writer = open('Roster.txt','r+')
        lines = writer.readlines()
        for line in lines:
            print(line)
        


central()