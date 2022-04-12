

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
    final = [{"Name" : playerbio[0],"Age": playerbio[1],"Position": playerbio[2],"Height": playerbio[3],"Weight": playerbio[4],"Number": playerbio[5]},{"Points" : statbio[0],"Rebounds": statbio[1],"Assists": statbio[2],"Blocks": statbio[3],"FG%": statbio[4],"3point%": statbio[5],"FT%": statbio[6],"Turnovers": statbio[7],"PlusMinus": statbio[8]}]
    reader.write(str(final))
    reader.close()

    


def edit_items():
    pass
def remove_items():
    pass



add_items()
read_roster()








