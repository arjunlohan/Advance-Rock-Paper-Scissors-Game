# Write your code here
user_name = str(input("Enter your name: "))
print("Hello,", str(user_name))
rating_file = open('rating.txt', 'r+')
lines = rating_file.readlines()
sno = 1
ratings = 0
ratings = str(ratings)
empty = [user_name+" "+ratings]
if len(lines) == 0:
    rating_file.writelines(empty)
for i in lines:
    i = i.strip()
    name, score = i.strip().split(" ")
    sno +=1
    if user_name == name:
        ratings = score
    else:
        pass
ratings = int(ratings)
# Code below is to create a custom option game.
# game_option = [item for item in input("Enter the game items : ").split(',')]
# if len(game_option) < 3:
# game_option = ['rock', 'paper', 'scissors']

game_type = str(input("Enter the game type:\n"
                      "Enter 1 for classic rock paper scissors\n"
                      "Enter 2 for rock paper scissors spock lizard\n"
                      "Enter 3 for 15 options rock paper scissor game\n"
                      "Or Press Enter to just start the f__king game\n"))

print("Okay, let's start")

if "1" in game_type:
    game_map = {0: "rock", 1: "paper", 2: "scissors"}
    game_option = ["rock", "paper", "scissors"]
    rps_table = [[-1, 1, 0],
                 [1, -1, 2],
                 [0, 2, -1]]
elif "2" in game_type:
    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "spock"}
    game_option = ["rock", "paper", "scissors", "lizard", "spock"]
    rps_table = [[-1, 1, 0, 0, 4],
             [1, -1, 2, 3, 1],
             [0, 2, -1, 2, 4],
             [0, 3, 2, -1, 3],
             [4, 1, 4, 3, -1]]
elif "3" in game_type:
    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "fire", 4: "snake", 5: "human", 6: "tree", 7: "wolf",
                8: "sponge", 9: "air", 10: "water", 11: "dragon", 12: "devil", 13: "lightning", 14: "gun"}
    game_option = ["rock", "paper", "scissors", "fire", "snake", "human", "tree", "wolf",
                   "sponge", "air", "water", "dragon", "devil", "lightning", "gun"]
    rps_table = [[-1, 1, 0, 0, 0, 0, 0, 0, 0, 9, 10, 11, 12, 13, 14],
                [1, -1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 1, 1, 1],
                [0, 2, -1, 3, 2, 2, 2, 2, 2, 2, 10, 11, 12, 13, 14],
                [0, 3, 3, -1, 3, 3, 3, 3, 3, 9, 10, 11, 12, 13, 14],
                [0, 4, 2, 3, -1, 4, 4, 4, 4, 4, 4, 11, 12, 13, 14],
                [0, 5, 2, 3, 4, -1, 5, 5, 5, 5, 5, 5, 12, 13, 14],
                [0, 6, 2, 3, 4, 5, -1, 6, 6, 6, 6, 6, 6, 13, 14],
                [0, 7, 2, 3, 4, 5, 6, -1, 7, 7, 7, 7, 7, 7, 14],
                [0, 8, 2, 3, 4, 5, 6, 7, -1, 8, 8, 8, 12, 8, 8],
                [9, 1, 2, 9, 4, 5, 6, 7, 8, -1, 9, 9, 9, 9, 9],
                [10, 1, 10, 10, 4, 5, 6, 7, 8, 9, -1, 10, 10, 10, 10],
                [11, 1, 11, 11, 11, 5, 6, 7, 8, 9, 10, -1, 11, 11, 11],
                [12, 1, 12, 12, 12, 12, 6, 7, 8, 9, 10, 11, -1, 12, 12],
                [13, 1, 13, 13, 13, 13, 13, 7, 8, 9, 10, 11, 12, -1, 13],
                [14, 1, 14, 14, 14, 14, 14, 14, 8, 9, 10, 11, 12, 13, -1]]
else:
    game_map = {0: "rock", 1: "paper", 2: "scissors"}
    game_option = ["rock", "paper", "scissors"]
    rps_table = [[-1, 1, 0],
                 [1, -1, 2],
                 [0, 2, -1]]


def get_key(val):
    for key, value in game_map.items():
        if val == value:
            return key
    return "key doesn't exist"

while True:
    user_input = str(input("Enter your choice (rock, paper, etc): \n"
                           "(Remember - type rating to check your score or type exit to leave the game)\n"
                           "Your choice: "))
    user_input = user_input.lower()
    if user_input == "exit":
        print("Bye!")
        break
    elif user_input == "rating":
        print("Your score is : ",ratings)
    else:
        import random
        random.seed()
        if user_input not in game_option:
            print("Invalid Input")
            print("\n")
        else:
            x = random.choice(game_option)
            winner = rps_table[get_key(user_input)][get_key(x)]
            if winner == get_key(x):
                print("Sorry, but the computer chose " + x)
                print("\n")
            elif winner == get_key(user_input):
                print("Well done. The computer chose " + x + " and failed")
                ratings += 100
                print("\n")
            else:
                print("There is a draw ", x)
                ratings += 50
                print("\n")
sno = sno-1
ratings = str(ratings)
rating_file.write('\n')
rating_file.write(str(user_name+" "+ratings))
rating_file.close()