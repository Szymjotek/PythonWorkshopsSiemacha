# Papier, Kamien, Nozyce

from random import randint

def papier_kamien_nozyce():

    #create a list of play options
    t = ["kamien", "papier", "nozyce"]

    #assign a random play to the computer
    computer = t[randint(0,2)]

    #set player to False
    player = True
    player_score, computer_score = 0,0

    while player:

        player = input("Kamien, Papier, Nozyce? ").lower()
        if player == computer:
            print("Remis!")
        elif player.lower() == "kamien":
            if computer == "papier":
                print("Przegralas/przegrales...!", computer, "pokrywa", player)
                computer_score+=1
            else:
                print("Wygralas/wygrales!", player, "niszczy", computer)
                player_score+=1
        elif player.lower()  == "papier":
            if computer == "nozyce":
                print("Przegralas/przegrales...", computer, "tna", player)
                computer_score+=1
            else:
                print("Wygralas/wygrales!", player, "pokrywa", computer)
                player_score+=1
        elif player.lower()  == "nozyce":
            if computer == "kamien":
                print("Przegralas/przegrales...", computer, "niszczy", player)
                computer_score+=1
            else:
                print("Wygralas/wygrales!", player, "tna", computer)
                player_score+=1
        else:
            print("Cos poszlo nie tak - sprawdz czy nie ma literowki!")

        #player was set to True, but we want it to be False so the loop continues
        print(f"Jest {player_score}:{computer_score}. Czy grasz dalej? Nacisnij T lub N.")
        player = True if input().lower()[0] == 't' else False
        computer = t[randint(0,2)]

if __name__ == "__main__":
    papier_kamien_nozyce()