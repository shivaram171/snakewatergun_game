def snakewatergun(input): 
    result={ 
        ("snake" , "water" ): 'A', 
        ("snake" , "gun" ): 'B', 
        ("snake" , "snake" ): 'None', 
        ("water" , "gun" ): 'A', 
        ("water" , "snake" ): 'B', 
        ("water" , "water" ): 'None', 
        ("gun" , "water" ): 'B', 
        ("gun" , "snake" ): 'A', 
        ("gun" , "gun" ): 'None', 
    } 
    A_win=0 
    moves = game_move(input) 
    for i in range(0, len(moves) - 1, 2): 
        A_move=moves[i]  
        B_move=moves[i+1] 
        winner = result.get((A_move,B_move)) 
        if winner == 'A': 
            A_win += 1 
    return A_win 
 
def game_move(input): 
    moves=[] 
    i =0 
    while i < len(input): 
        if input[i]=="s": 
            move = "snake" 
            moves.append(move) 
            i=i+5 
        elif input[i]=="w": 
            move = "water" 
            moves.append(move) 
            i=i+5 
        elif input[i]=="g": 
            move="gun" 
            moves.append(move) 
            i=i+3 
        else: 
            i=i+1 
    return moves 
 
 
input1 = "snakewater" 
print(snakewatergun(input1)) 
 
input2 = "snakewatergunwater" 
print(snakewatergun(input2)) 
 
input3 = "snakesnakewatergunwatergun" 
print(snakewatergun(input3)) 
 
input4 = "snakewaterwatergunsnakegunwatersnake" 
print(snakewatergun(input4))