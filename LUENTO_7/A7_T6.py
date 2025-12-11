import random      
random.seed(1234)       

ascii_art = {    
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" 
}

def options():      
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")

def main():
    player_wins = 0
    player_losses = 0 
    player_draws = 0        
    bot_wins = 0 
    bot_losses = 0
    bot_draws = 0
    
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")

    choices = {"1": "rock", "2": "paper", "3": "scissors"}
    while True:
        options()

        choice = input("Your choice: ").strip()

        if choice == "0":
            break
        elif choice not in choices:
            print("Invalid choice! Please choose 1, 2, 3, or 0.\n")
            continue

        player_choice = choices[choice]
        bot_choice_num = random.randint(1,3)
        bot_choice = choices[str(bot_choice_num)]

        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#"*25)
        print(f"{player_name} chose {player_choice}.\n{ascii_art[player_choice]}")
        print("#"*25)
        print(f"RPS-3PO chose {bot_choice}.\n{ascii_art[bot_choice]}")
        print("#"*25)

        if player_choice == bot_choice:
            print(f"Draw! Both players chose {player_choice}.\n")
            player_draws += 1
            bot_draws += 1

        elif (player_choice == "rock" and bot_choice == "scissors") \
            or (player_choice == "paper" and bot_choice == "rock") \
            or (player_choice == "scissors" and bot_choice == "paper"):
            print(f"{player_name} {player_choice} beats RPS-3PO {bot_choice}.\n")
            player_wins += 1
            bot_losses += 1
        else:
            print(f"RPS-3PO {bot_choice} beats {player_name} {player_choice}.\n")
            bot_wins += 1
            player_losses += 1

    print("\nResults:")
    print(f"{player_name} - wins ({player_wins}), losses ({player_losses}), draws ({player_draws})")
    print(f"RPS-3PO - wins ({bot_wins}), losses ({bot_losses}), draws ({bot_draws})")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()