def check_result(opponent, player):
    
    player_point_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    outcome_point_dict = {
        "lost": 0,
        "draw": 3,
        "won": 6
    }

    match = 0

    # Opponent plays Rock
    if opponent == "A":

        # rock
        if player == "X":
            print("Draw!")
            match = int(player_point_dict[player] + outcome_point_dict["draw"])

        # paper
        elif player == "Y": 
            print("Player wins")
            match = int(player_point_dict[player] + outcome_point_dict["won"])

        # scissors
        elif player == "Z": 
            print("Opponent wins")
            match = int(player_point_dict[player] + outcome_point_dict["lost"])
    
    # Opponent plays Paper
    if opponent == "B":

        # rock
        if player == "X":
            print("Opponent wins")
            match = int(player_point_dict[player] + outcome_point_dict["lost"])

        # paper
        elif player == "Y": 
            print("Draw!")
            match = int(player_point_dict[player] + outcome_point_dict["draw"])
        
        # scissors
        elif player == "Z": 
            print("Player wins")
            match = int(player_point_dict[player] + outcome_point_dict["won"])
    
    # Opponent plays Scissors
    if opponent == "C":

        # rock
        if player == "X":
            print("Player wins")
            match = int(player_point_dict[player] + outcome_point_dict["won"])

        # paper
        elif player == "Y": 
            print("Opponent wins")
            match = int(player_point_dict[player] + outcome_point_dict["lost"])
        
        # scissors
        elif player == "Z": 
            print("Draw!")
            match = int(player_point_dict[player] + outcome_point_dict["draw"])
    
    return match 
    
def check_rigged_result(opponent, player):
    
    player_point_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    outcome_point_dict = {
        "lost": 0,
        "draw": 3,
        "won": 6
    }

    match = 0

    # Player plays Rock
    if player == "X":
        # Player needs to lose!
        
        # Opponent plays Rock
        if opponent == "A":
            # scissors
            print("Opponent wins")
            match = int(player_point_dict["Z"] + outcome_point_dict["lost"])
        
        # Opponent plays Paper
        if opponent == "B":

            # rock
            print("Opponent wins")
            match = int(player_point_dict["X"] + outcome_point_dict["lost"])

        # Opponent plays Scissors
        if opponent == "C":
            # paper
            print("Opponent wins")
            match = int(player_point_dict["Y"] + outcome_point_dict["lost"])
            

    # Player plays Paper
    if player == "Y":
        # Player needs a draw!

        # Opponent plays Rock
        if opponent == "A":
            print("Draw!")
            match = int(player_point_dict["X"] + outcome_point_dict["draw"])
    
        # Opponent plays Paper
        if opponent == "B":
            print("Draw!")
            match = int(player_point_dict["Y"] + outcome_point_dict["draw"])
        
        # Opponent plays Scissors
        if opponent == "C":
            print("Draw!")
            match = int(player_point_dict["Z"] + outcome_point_dict["draw"])
    

    # Player plays Scissors
    if player == "Z":
        # Player needs to win!

        # Opponent plays Rock
        if opponent == "A":
            print("Player wins")
            match = int(player_point_dict["Y"] + outcome_point_dict["won"])
        
        # Opponent plays Paper
        if opponent == "B":
            print("Player wins")
            match = int(player_point_dict["Z"] + outcome_point_dict["won"])
        
        # Opponent plays Scissors
        if opponent == "C":
            print("Player wins!")
            match = int(player_point_dict["X"] + outcome_point_dict["won"])
    
    return match 
    