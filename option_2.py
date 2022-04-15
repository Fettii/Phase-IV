### SEARCH PLAYERS SECTION

import main

def menu():
    user_input = input("\nSearch Players - Please type a number or type quit to exit\n\n1. Add filter\n\n")
    if(user_input == "1"):
        add_filter()
    elif(user_input == "quit"):
        main.central()
    else:
        print("Sorry thats not a known command, try again")   
        menu() 
    
def add_filter(): 
    word = input("Please enter phrase to filter for:    ")
    doggy = [line for line in open('Roster.txt') if word in line]
    print(doggy)    
    
    
    



    menu()
    


