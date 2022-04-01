#Global
import ast

rosterList = []
stats = {}

#this is where the general info about a basketball player
class Players:
    def __init__(self, name,number,age,pos,height,weight):
        self.name = name
        self.age = age
        self.pos = pos 
        self.height = height
        self.weight = weight
        self.number = number
    
#this is where I will create player objects, at this time it will be limited to two players to represent a basketball player and for testing reasons
p1 = Players("", "0", "0", "", "", "0")
p2 = Players("", "0", "0", "", "", "0")


#this is where the genreal info about how that player performs on the basketball court
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
    
#This is the main menu section, will put all options in here
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
        
# Option 1 section
def option_1():
    print("     ROSTER  \n")
    print("1. Read Roster \n2. Add items \n5. Exit")
    option_select = input()
    if(option_select == "1"):
        reader = open("Roster.txt", "r")
        print(reader.read())
        reader.close
        option_1()
#Adds a player to the roster file
    elif(option_select == "2"):
        if(p1.name == ""):
            enter_info = input("Please Enter player basic info in the following format *dont forget commas!* : Name, Age, Position, Height, Weight, Number ")
            player_list = enter_info.split(",")
            p1.name = player_list[0]
            p1.age = player_list[1]
            p1.pos = player_list[2]
            p1.height = player_list[3]
            p1.weight = player_list[4]
            p1.number = player_list[5]
            w = open("Roster.txt","w")
            w.write (  "{Name: " + p1.name + ", Age: " + p1.age + ", Position: " + p1.pos + ", Height: " + p1.height + ", Weight: " + p1.weight + ", Number: " + p1.number + "}")
            w.flush()
            w.close()
            option_1()
        elif(p2.name == ""):
            enter_info = input("Please Enter player basic info in the following format *dont forget commas!* : Name, Age, Position, Height, Weight, Number ")
            player_list = enter_info.split(",")
            p2.name = player_list[0]
            p2.age = player_list[1]
            p2.pos = player_list[2]
            p2.height = player_list[3]
            p2.weight = player_list[4]
            p2.number = player_list[5]
            w = open("Roster.txt","a")
            w.write ("\n" + "{Name: " + p2.name + ", Age: " + p2.age + ", Position: " + p2.pos + ", Height: " + p2.height + ", Weight: " + p2.weight + ", Number: " + p2.number + "}")
            w.flush()
            w.close()
            option_1()
        else:
            print("No more players can be added at this time, the max is 2 players, returing to option 1 section....")
            option_1()

    elif(option_select == "5"):
        main_menu()


    else:
        print("option not availible")
        option_1()
#End of option 1 section    

#Start of Option 2 Section *THIS SECTION IS INCOMPLETE AT THIS TIME
def option_2():
    print("     SEARCH PLAYERS  \n")
    print("1.   Search for players info by name\n2. Exit")
    option_select = input()
    if(option_select == "1"):
        player_name = input("Please type player name: ")
        reader = open("Roster.txt","r")
        for line in reader.readlines():
            print(line)
    elif(option_select == "2"):
        main_menu()
    else:
        print("Unknown Command\n")

        

#End of Option 2 Section
    




main_menu()


       









