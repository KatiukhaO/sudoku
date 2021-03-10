from random import randint


""" For sudoku table can be 5 change how don`t influence on corrected structure of table
    1. Transpose
    2. Change small string in border one area ( 1 horizontal line )
    3. Change small column in border one area ( 1 vertical line )
    4. Change bib string ( 3 horizontal line in  one area )
    5 . Change big column ( 3 vertical line in one area )

    *Table sudoku has three horizontal and three vertical area by three line in area:
        First area  : line and column from index 0 to 2
        Second area : line and column from index 3 to 5
        Third area  : line and column from index 6 to 9

    Then area line has name "big ..."

    Then I create functions for change sudoku table and shuffle table. 
"""


def create_base_sudoku_table():
    """Create correct full sudoku table """
    return [[int(((i * 3 + i / 3 + j) % 9 + 1)) for j in range(9)] for i in range(9)]


def show_board(table):
    for row in table:
        print('  '.join(map(str, row)))


def transpose(table):
    """ 1. Transpose table sudoku """
    for i in range(len(table)):
        for j in range(i, len(table[i])):
            table[i][j], table[j][i] = table[j][i], table[i][j]
    return table


def changed_string_one_area(table):
    """ 2. Change first line with second line in table sudoku, in one area """
    number_area = randint(0, 2)
    first_line, second_line = 0, 0
    while first_line == second_line:
        first_line, second_line = randint(3*number_area, 3 * number_area + 3 - 1), \
                                  randint(3*number_area, 3 * number_area + 3 - 1)
    table[first_line], table[second_line] = table[second_line], table[first_line]
    return table


def changed_column_one_area(table):
    """ 3. For changed column we can change string in transpose table"""
    return changed_string_one_area(transpose(table))


def changed_big_string_one_area(table):
    """ 4. Change first area line with second area line in table sudoku """
    first_row, second_row = 0, 0
    while first_row == second_row:
        first_row, second_row = randint(0, 2), randint(0, 2)
    index_line_first, index_line_second = max(first_row, second_row) * 3, min(first_row, second_row) * 3
    for i in range(3):
        table[index_line_first + i], table[index_line_second + i] = table[index_line_second + i], \
                                                                    table[index_line_first + i]
    return table


def changed_big_column_one_area(table):
    """ 5. For changed area column we can change area string in transpose table"""
    return changed_big_string_one_area(transpose(table))


def shuffle_table(table, quantity=10):
    """ Function shuffle table sudoku, default quantity shuffle is 10,
        In dictionary we have 'Key' is number, 'value' is call necessary function for table
    """
    functions = {1: transpose(table),
                 2: changed_string_one_area(table),
                 3: changed_column_one_area(table),
                 4: changed_big_string_one_area(table),
                 5: changed_big_column_one_area(table)
                 }
    for i in range(quantity):
        r = randint(1, 5)
        table = functions[r]
    return table


show_board(create_base_sudoku_table())
print("--------------------------------------------------------------------------------------------------")
show_board(shuffle_table(create_base_sudoku_table()))
