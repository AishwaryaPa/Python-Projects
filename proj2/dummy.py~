def check_points(word, two_d_list, row_list, column_list):
    counter = 0
    for row, column in zip(row_list, column_list):
        if two_d_list[row][column] == word[counter]:
            counter = counter + 1
    if counter == len(word) - 1:
        return(True)
    else:
        return(False)

def validate_lists(row_list, column_list, width, length):
    counter = 0
    for row, column in zip(row_list, column_list):
        if row < width and row >= 0 and column < length and column >= 0:
            counter = counter + 1
    if counter == len(row_list):
        return(True)
    else:
        return(False)


def create_list(word_len, static_character, revise_list, static_list, counter):
    if counter >= 1 and counter <= 4:
    # creates the list of whichever character stays the same throught the list
        for static_index in range(word_len):
            static_list.append(static_character)

   # dynamic_character = static_character
    elif counter >= 5 and counter <= 8:
        dynamic_character = static_character
        for pair in range(word_len):
            static_list.append(dynamic_character)
            if counter == 5 or counter == 7:
                dynamic_character = dynamic_character - 1
            elif counter == 6 or counter == 8:
                dynamic_character = dynamic_character + 1

    diff = word_len - 1
    for match in static_list:
        revise_list.append(diff)
        if counter == 1 or counter == 3 or counter == 5 or counter == 8:
            diff = diff - 1
        elif counter == 2 or counter == 4 or counter == 6 or counter == 7:
            diff = diff + 1
    return(revise_list, static_list)


# check will take in row, column, word, word length, 2d list of the board, board demensions 

def check(row, column, word, word_len, two_d_list, width, length):    # counter is what makes this function recursive
    if counter < 9:
        # check in upwards direction
        if counter == 1:
            counter = 1
            row_list = []
            column_list = []
            new_lists = create_list(word_len, column, column_list, row_list, counter)
            row_list, column_list = new_lists
            print("row list", row_list)
            print("column list", column_list)

        elif counter == 2:
            # check in downwards direction
            counter = 2
            row_list = []
            column_list = []
            new_lists = create_list(word_len, column, column_list, row_list, counter)
            row_list, column_list = new_lists
            print("row list", row_list)
            print("column list", column_list)
            
        elif counter == 3:
            # check in left direction
            counter = 3
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)

        elif counter == 4:
            # check in left direction
            counter = 4
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)
            
        elif counter == 5:
            # checks in diagonally upper left 
            counter = 5
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)

        elif counter == 6:
            # checks in diagonally lower right
            counter = 6
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)

        elif counter == 7:
            # checks in diagonally upper right
            counter = 7
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)
            
        elif counter == 8:
            # checks in diagonally lower left
            counter = 8
            row_list = []
            column_list = []
            new_lists = create_list(word_len, row, row_list, column_list, counter)
            column_list, row_list = new_lists
            print("row list", row_list)
            print("column list", column_list)

check()

    
