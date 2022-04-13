import ast

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
    reader = open("Roster.txt")
    lines = reader.readlines()
    keepGoing = True
    while keepGoing:
        new_edit = input("Please enter player's name in which you would like to edit or type 'quit' if finished editing: ")
        if(new_edit == 'quit'):
            keepGoing = False
        else:
            for line in lines:  # I need to figure out how to make loop skip blank lines or just make the program exactly that amount of text lines needed, this is because it is trying to make the blank line a dict which wont work
                if line == '':
                    pass
                else:
                    player_dict = ast.literal_eval(line)
                    print(player_dict)



def remove_items():
    pass



edit_items()








