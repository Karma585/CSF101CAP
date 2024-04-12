################################
# Name: Karma Rangjung Dorji
# Course: 1st yesr BE.in ECE
# Student ID Number: 02230096
################################
# References
# https://www.w3schools.com/python/python_file_open.asp
# https://chat.openai.com/
# https://www.python.org/,
################################
# 50223
################################
def read_input(f_path):
    # The function read_input was defined to read input from a file
    game_rounds = []
    # to store game rounds, an empty list name game_round was initialized
    with open(f_path, 'r') as doc:
        # Iteration over each line in the file was done to read the file
        for line in doc:
            # After each iteration, the line was splited into structure and game result
            structure, game_result = line.strip().split()
            # Then this appends a tuple containing structure and game result to the game_rounds list
            game_rounds.append((structure, game_result))
    # Finally after the completion of iteration, it will return the list stored in game_rounds
    return game_rounds
# To calculate the total score based on game rounds, function below is defined
def calculate_score(game_rounds):
    # The score is initialized to 0 so later it can be updated
    score = 0
    # Iteration over each game round
    for structure, game_result in game_rounds:
        # Determine the score for the current structure and game_result through comparison of possible combination
        if structure == "A":
            if game_result == "X":
                structure_score = 3
            elif game_result == "Y":
                structure_score = 4
            else:
                structure_score = 8
        elif structure == "B":
            if game_result == "X":
                structure_score = 1
            elif game_result == "Y":
                structure_score = 5
            else:
                structure_score = 9
        else:
            if game_result == "X":
                structure_score = 2
            elif game_result == "Y":
                structure_score = 6
            else:
                structure_score = 7

        # Final score is calculated here
        score += structure_score

    # Then it return the total score
    return score

# game file name passed in variable f_path
f_path = "input_6_cap1.txt"  
# read_input function called and stored its value in game_rounds
game_rounds = read_input(f_path)
# calculate_score function called and stored its value in total score
total_score = calculate_score(game_rounds)
# Total score is printed
print("Total Score:", total_score)
