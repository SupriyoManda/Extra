import random

# Define a dictionary to store player stats
players = {
    "Lionel Messi": {"pace": 80, "shooting": 84, "passing": 88, "dribbling": 92, "defending": 36, "physicality": 63},
    "Cristiano Ronaldo": {"pace": 76, "shooting": 88, "passing": 77, "dribbling": 80, "defending": 39, "physicality": 79},
    "Kylian Mbappé": {"pace": 97, "shooting": 88, "passing": 78, "dribbling": 90, "defending": 41, "physicality": 79},
    "Neymar Jr.": {"pace": 89, "shooting": 83, "passing": 86, "dribbling": 94, "defending": 37, "physicality": 58},
    "Robert Lewandowski": {"pace": 75, "shooting": 91, "passing": 79, "dribbling": 85, "defending": 44, "physicality": 82},
    "Kevin De Bruyne": {"pace": 74, "shooting": 85, "passing": 93, "dribbling": 87, "defending": 64, "physicality": 78},
    "Mohamed Salah": {"pace": 93, "shooting": 87, "passing": 82, "dribbling": 90, "defending": 45, "physicality": 75},
    "Harry Kane": {"pace": 70, "shooting": 91, "passing": 83, "dribbling": 81, "defending": 47, "physicality": 82},
    "Virgil van Dijk": {"pace": 79, "shooting": 60, "passing": 71, "dribbling": 70, "defending": 90, "physicality": 86},
    "Luka Modric": {"pace": 72, "shooting": 76, "passing": 89, "dribbling": 88, "defending": 69, "physicality": 67},
    "Sadio Mané": {"pace": 89, "shooting": 84, "passing": 80, "dribbling": 90, "defending": 50, "physicality": 75},
    "Karim Benzema": {"pace": 79, "shooting": 90, "passing": 83, "dribbling": 87, "defending": 40, "physicality": 82},
    "Raheem Sterling": {"pace": 91, "shooting": 80, "passing": 77, "dribbling": 86, "defending": 45, "physicality": 69},
    "Bruno Fernandes": {"pace": 76, "shooting": 84, "passing": 89, "dribbling": 83, "defending": 65, "physicality": 72},
    "Phil Foden": {"pace": 84, "shooting": 79, "passing": 82, "dribbling": 89, "defending": 45, "physicality": 60},
    "Ederson": {"pace": 61, "shooting": 20, "passing": 55, "dribbling": 50, "defending": 87, "physicality": 90},
    "Manuel Neuer": {"pace": 60, "shooting": 28, "passing": 50, "dribbling": 50, "defending": 50, "physicality": 87},
    "Alisson Becker": {"pace": 62, "shooting": 30, "passing": 55, "dribbling": 50, "defending": 90, "physicality": 88},
    "Erling Haaland": {"pace": 89, "shooting": 93, "passing": 65, "dribbling": 80, "defending": 45, "physicality": 88},
    "Sergio Ramos": {"pace": 72, "shooting": 62, "passing": 71, "dribbling": 70, "defending": 89, "physicality": 84},
    "Achraf Hakimi": {"pace": 96, "shooting": 70, "passing": 75, "dribbling": 80, "defending": 70, "physicality": 73},
    "João Cancelo": {"pace": 85, "shooting": 68, "passing": 83, "dribbling": 82, "defending": 79, "physicality": 71},
    "Antonio Rudiger": {"pace": 82, "shooting": 45, "passing": 64, "dribbling": 66, "defending": 88, "physicality": 85},
    "Joshua Kimmich": {"pace": 70, "shooting": 70, "passing": 86, "dribbling": 85, "defending": 82, "physicality": 78},
    "Giorgio Chiellini": {"pace": 65, "shooting": 50, "passing": 60, "dribbling": 55, "defending": 89, "physicality": 90},
    "Thiago Silva": {"pace": 60, "shooting": 45, "passing": 65, "dribbling": 60, "defending": 90, "physicality": 88},
    "Alphonso Davies": {"pace": 96, "shooting": 69, "passing": 75, "dribbling": 85, "defending": 75, "physicality": 77},
    "Ruben Dias": {"pace": 70, "shooting": 50, "passing": 70, "dribbling": 55, "defending": 90, "physicality": 85},
    "Jules Kounde": {"pace": 80, "shooting": 55, "passing": 75, "dribbling": 70, "defending": 85, "physicality": 75},
    "Frenkie de Jong": {"pace": 81, "shooting": 70, "passing": 83, "dribbling": 86, "defending": 76, "physicality": 72},
    "Memphis Depay": {"pace": 84, "shooting": 79, "passing": 76, "dribbling": 87, "defending": 40, "physicality": 68},
    "Christian Pulisic": {"pace": 90, "shooting": 75, "passing": 80, "dribbling": 88, "defending": 37, "physicality": 66},
    "Ciro Immobile": {"pace": 70, "shooting": 88, "passing": 74, "dribbling": 81, "defending": 42, "physicality": 80},
    "Gini Wijnaldum": {"pace": 78, "shooting": 70, "passing": 82, "dribbling": 75, "defending": 66, "physicality": 72},
    "Angel Di Maria": {"pace": 86, "shooting": 83, "passing": 85, "dribbling": 88, "defending": 38, "physicality": 70},
    "Youri Tielemans": {"pace": 77, "shooting": 78, "passing": 83, "dribbling": 80, "defending": 60, "physicality": 73},
    "David Silva": {"pace": 70, "shooting": 75, "passing": 87, "dribbling": 80, "defending": 41, "physicality": 65},
    "Mikel Oyarzabal": {"pace": 81, "shooting": 74, "passing": 82, "dribbling": 85, "defending": 49, "physicality": 72},
    "Domenico Berardi": {"pace": 83, "shooting": 78, "passing": 79, "dribbling": 85, "defending": 36, "physicality": 68},
    "Pelé": {"pace": 95, "shooting": 99, "passing": 90, "dribbling": 98, "defending": 40, "physicality": 80},
    "Diego Maradona": {"pace": 88, "shooting": 94, "passing": 91, "dribbling": 99, "defending": 36, "physicality": 70},
    "Zinedine Zidane": {"pace": 75, "shooting": 89, "passing": 92, "dribbling": 88, "defending": 65, "physicality": 78},
    "Johan Cruyff": {"pace": 86, "shooting": 90, "passing": 88, "dribbling": 97, "defending": 50, "physicality": 72},
    "Ronaldinho": {"pace": 92, "shooting": 87, "passing": 85, "dribbling": 99, "defending": 30, "physicality": 65},
    "Michel Platini": {"pace": 78, "shooting": 91, "passing": 94, "dribbling": 82, "defending": 55, "physicality": 70},
    "Franz Beckenbauer": {"pace": 82, "shooting": 75, "passing": 88, "dribbling": 80, "defending": 95, "physicality": 85},
    "Ronaldo Nazário": {"pace": 90, "shooting": 95, "passing": 80, "dribbling": 98, "defending": 30, "physicality": 75},
    "George Best": {"pace": 92, "shooting": 90, "passing": 80, "dribbling": 99, "defending": 35, "physicality": 70},
    "Gerd Müller": {"pace": 80, "shooting": 99, "passing": 75, "dribbling": 80, "defending": 30, "physicality": 82},
    "Alfredo Di Stéfano": {"pace": 85, "shooting": 90, "passing": 87, "dribbling": 92, "defending": 60, "physicality": 80},
}

player_score = 0
computer_score = 0

def get_stat_value(player, stat):
    return players[player][stat]

def compare_stats(player1, player2, stat):
    value1 = get_stat_value(player1, stat)
    value2 = get_stat_value(player2, stat)

    if value1 > value2:
        return player1
    elif value2 > value1:
        return player2
    else:
        return "Draw"

# Main game loop
print("Welcome to the Football Player Card Game!")

while True:
    # Randomly select players for comparison
    player1 = random.choice(list(players.keys()))
    player2 = random.choice(list(players.keys()))
    while player1 == player2:
        player2 = random.choice(list(players.keys()))

    print(f"\nPlayer 1: {player1}")
    print(f"Player 2: {player2}")

    # Ask the user for the stat to compare
    print("\nChoose a stat to compare:")
    for stat in players[player1].keys():
        print(f"- {stat.capitalize()}")

    chosen_stat = input("Enter the stat you want to compare: ").strip().lower()

    while chosen_stat not in players[player1]:
        print("Invalid stat! Please choose from the following:")
        for stat in players[player1].keys():
            print(f"- {stat.capitalize()}")
        chosen_stat = input("Enter the stat you want to compare: ").strip().lower()

    winner = compare_stats(player1, player2, chosen_stat)

    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"The winner is: {winner}")
        if winner == player1:
            player_score += 1
            # Computer randomly chooses a stat to compare next
            computer_stat_choice = random.choice(list(players[player2].keys()))
            print(f"Computer chooses to compare on {computer_stat_choice.capitalize()} for the next round.")
        else:
            computer_score += 1
            # User can choose a stat next
            print(f"You will choose the next stat to compare.")

    # Display scores
    print(f"\nCurrent Score: You - {player_score}, Computer - {computer_score}")

    # Ask if the user wants to continue
    continue_game = input("Do you want to continue the game? (yes/no): ").strip().lower()
    if continue_game != 'yes':
        print("Thanks for playing! Goodbye!")
        break

# Final scores
print(f"\nFinal score: You: {player_score}, Computer: {computer_score}")
if player_score > computer_score:
    print("Congratulations! You win the game!")
elif player_score < computer_score:
    print("Sorry! The computer wins the game!")
else:
    print("It's a draw!")