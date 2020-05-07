def load():
    file_open = open("tic.txt")
    new_game_list = []
    for line in file_open:
        line = line.strip("\n")
        line = list(line)
        new_game_list.append(line)
    print(new_game_list)
    file_open.close()
    return(new_game_list)

def save(board):
    file_open = open("tic.txt", "w")
    for line in board:
        my_string = ""
        for character in line:
            my_string = my_string + str(character)
        file_open.write(my_string)
    file_open.close()
    

