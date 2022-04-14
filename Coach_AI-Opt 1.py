import ast
import fileinput

def read_roster():
    reader = open("Roster.txt","r")
    print(reader.readlines())
    reader.close()
    

    
def add_items():

    reader = open("Roster.txt","a")
    playerbio = input("Please enter the asked info in this format example (Name,Age,Primary Position,Height,Weight,Jersey Number): ")
    statbio = input("Okay, now enter stats in a similar format ex.(Points,Rebounds,Assists,Blocks,FG%,3point%,FT%,Turnovers,PlusMinus): ")
    playerbio = playerbio.split(",")
    statbio = statbio.split(",")
    final = [{"name" : playerbio[0],"age": playerbio[1],"position": playerbio[2],"height": playerbio[3],"weight": playerbio[4],"number": playerbio[5]},{"points" : statbio[0],"rebounds": statbio[1],"assists": statbio[2],"blocks": statbio[3],"fg%": statbio[4],"3point%": statbio[5],"ft%": statbio[6],"turnovers": statbio[7],"plusMinus": statbio[8]}]
    reader.write(str(final))
    reader.close()

    


def edit_items():
    reader = open("Roster.txt","r+")
    lines = reader.readlines()
    keepGoing = True
    while keepGoing:
        new_edit = input("Please enter player's name in which you would like to edit or type 'quit' if finished editing: ")
        if(new_edit == 'quit'):
            keepGoing = False
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
                                
                                






def remove_items():
    pass



edit_items()








