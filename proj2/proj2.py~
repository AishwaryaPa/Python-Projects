# File:        proj2.py
# Author:      Aishwarya Panchumarty
# Date:        05/02/16
# Section:     09
# E-mail:      aispan1@umbc.edu
# Description: This file contains code for a puzzle called "word search"

# validate_list():    Checks if the indices of the list are valid depending
#                     on the dimensions of the puzzle and uses those points 
#                     to check for the word in the puzzle
# Input:              Takes in the indicies, dimensions of the puzzle, and 
#                     the puzzle
# Output:             Returns a boolean value
def validate_list(row_list, column_list, width, length, word, two_d_list):
    counter = 0
    for row, column in zip(row_list, column_list):
        if row < width and row >= 0 and column < length and column >= 0:
            counter = counter + 1
    if counter == len(row_list):
        counter = 0
        for row, column in zip(row_list, column_list):
            if two_d_list[row][column] == word[counter]:
                counter = counter + 1
        if counter == len(word):
            return(True)
        else:
            return(False)
    else:
        return(False)

# create_list():      Creates a list of possible indices of the word for 
#                     the word_search function
# Input:              Takes in the word length, index of the first letter 
#                     in the puzzle, two empty lists, and a counter value
# Output:             Sends back the lists to word_search function
def create_list(word_len, static_character, static_character_match, revise_list, static_list, counter):
    if counter >= 1 and counter <= 4:
        for static_index in range(word_len):
            static_list.append(static_character)

    elif counter >= 5 and counter <= 8:
        dynamic_character = static_character
        for pair in range(word_len):
            static_list.append(dynamic_character)
            if counter == 5 or counter == 7:
                dynamic_character = dynamic_character - 1
            elif counter == 6 or counter == 8:
                dynamic_character = dynamic_character + 1

    for match in static_list:
        revise_list.append(static_character_match)
        if counter == 1 or counter == 3 or counter == 5 or counter == 8:
            static_character_match = static_character_match - 1
        elif counter == 2 or counter == 4 or counter == 6 or counter == 7:
            static_character_match = static_character_match + 1
    return(revise_list, static_list)

# word_search():      Searches for the word in the puzzle
# Input:              Takes in the index of first letter of the word, word, 
#                     length of word, puzzle, and the dimensions of the
#                     puzzle, counter value, and boolean value
# Output:             returns the word, index, counter, and boolean value
def word_search(row, column, word, word_len, two_d_list, width, length, counter, boolean_value):
    if counter < 9:
        row_list = []
        column_list = []

        # Goes up and down
        if counter == 1 or counter == 2:
            new_lists = create_list(word_len, column, row, column_list, row_list, counter)
            row_list, column_list = new_lists

        # Goes left backwards, right, diagonally upper left,
        # diagonally lower right, and diagonally lower left
        elif counter == 3 or counter == 4 or counter == 5 or counter == 6 or counter == 7 or counter == 8:
            new_lists = create_list(word_len, row, column, row_list, column_list, counter)
            column_list, row_list = new_lists

        # make sure lists contain correct values and
        # check if those values match the indices of
        # the word in the puzzle
        check_list = validate_list(row_list, column_list, width, length, word, two_d_list)
        if check_list == True:
            boolean_value = True
            return (row, column, word, counter, boolean_value)
        else:
            return word_search(row, column, word, word_len, two_d_list, width, length, counter + 1, boolean_value)

    elif boolean_value == False and counter >= 9:
        return(row, column, word, counter, boolean_value)


# letter_counter():   counts the number of times a letter is repeated
#                     in the entire puzzle
# Input:              takes in the first letter of the word and the 
#                     puzzle
# Output:             sends back counter to main 
def letter_counter(first_letter, two_d_list):
    counter = 0
    for row in two_d_list:
        for column in row:
            if column == first_letter:
                counter = counter + 1
    return(counter)

def main():
    # Intro
    print("Welcome to the Word Search")
    print("For this, you will import two files: 1. The puzzle board, and 2. The word list.")
    
    # Get puzzle
    puzzle_file = input("What is the puzzle file would like to import?: ")
    puzzle_open = open(puzzle_file)
       
    puzzle_list = []
    for line in puzzle_open:
        line = line.strip("\n")
        new_line = ""
        
        # Get rid of spaces between characters
        for character in range(0, len(line), 2):
            new_line = new_line + line[character]
        line = list(new_line)
        puzzle_list.append(line)
    puzzle_open.close()

    # Get word list
    word_list_file = input("What is the word list file you would like to import?: ")
    word_list_open = open(word_list_file)
    word_list = []
    for line in word_list_open:
        line = line.strip("\n")
        line = line.strip("\t")
        word_list.append(line)
    word_list_open.close()

    # Search the word
    for word in word_list:
        first_letter = word[0]

        # Dimensions of the puzzle
        width = len(puzzle_list) 
        length = len(puzzle_list[0])
        
        num_letter_repeated = letter_counter(first_letter, puzzle_list)
        recursive_counter = 0

        for row in range(width):
            for column in range(length):
                if puzzle_list[row][column] == first_letter:
                    counter = 1
                    boolean_value = False
                    find_word = word_search(row, column, word, len(word), puzzle_list, width, length, counter, boolean_value)
                    
                    # Final Statement
                    if find_word[-1] == False:
                        recursive_counter = recursive_counter + 1
                        if recursive_counter == num_letter_repeated:
                            print("The word", word, "does not appear in the puzzle.")
                    elif find_word[-1] == True:
                        row, column, word, counter, boolean_value = find_word
                        if counter == 1:
                            print("The word", word, "starts in", row, ",", column, "and goes up")
                        elif counter == 2:
                            print("The word", word, "starts in", row, ",", column, "and goes down")
                        elif counter == 3:
                            print("The word", word, "starts in", row, ",", column, "and goes backwards left")
                        elif counter == 4:
                            print("The word", word, "starts in", row, ",", column, "and goes right")
                        elif counter == 5:
                            print("The word", word, "starts in", row, ",", column, "and goes diagonally up and left")
                        elif counter == 6:
                            print("The word", word, "starts in", row, ",", column, "and goes diagonally down and right")
                        elif counter == 7:
                            print("The word", word, "starts in", row, ",", column, "and goes diagonally up and right")
                        elif counter == 8:
                            print("The word", word, "starts in", row, ",", column, "and goes diagonally down and left")

main()
