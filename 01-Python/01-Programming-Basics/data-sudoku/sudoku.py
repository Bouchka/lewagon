# pylint: disable=missing-docstring

# $DELETE_BEGIN

# A valid set of Sudoku values: numbers 1 through 9
VALID_SET = list(range(1, 10))

def valid_rows(grid):
    # Check each row in the grid
    for row in grid:
        # A valid row must contain all digits from 1 to 9 once (regardless of order)
        if sorted(row) != VALID_SET:
            return False
    return True

def valid_columns(grid):
    # Check each column (there are 9 columns)
    for j in range(0, 9):
        col = []
        # Build the column by collecting the j-th element from each row
        for i in range(0, 9):
            col.append(grid[i][j])
        # A valid column must also contain all digits from 1 to 9
        if sorted(col) != VALID_SET:
            return False
    return True


def valid_boxes(grid):
    # Check each 3x3 sub-grid (box), starting from top-left corner
    for box_row in range(0, 9, 3):  # 0, 3, 6 → top row of each box
        for box_col in range(0, 9, 3):  # 0, 3, 6 → left column of each box
            square = []
            # Loop through each cell inside the 3x3 box
            for i in range(0, 3):
                i += box_row  # adjust for box row offset
                for j in range(0, 3):
                    j += box_col  # adjust for box column offset
                    square.append(grid[i][j])
            # A valid box must also contain all digits from 1 to 9
            if sorted(square) != VALID_SET:
                return False
    return True

# $DELETE_END

def sudoku_validator(grid):
    # $CHALLENGIFY_BEGIN
    # A Sudoku grid is valid only if all rows, columns, and boxes are valid
    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)
    # $CHALLENGIFY_END

grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]

print(sudoku_validator(grid))

# Other ways to implement the same logic:

# def valid_rows(grid):
#     # Each row must contain all digits from 1 to 9
#     return all(set(row) == VALID_SET for row in grid)

# def valid_columns(grid):
#     # Transpose grid to get columns as rows using zip(*grid)
#     return all(set(col) == VALID_SET for col in zip(*grid))

# def valid_boxes(grid):
#     # Extract each 3x3 box and check it contains all digits from 1 to 9
#     for row in range(0, 9, 3):
#         for col in range(0, 9, 3):
#             box = [
#                 grid[r][c]
#                 for r in range(row, row + 3)
#                 for c in range(col, col + 3)
#             ]
#             if set(box) != VALID_SET:
#                 return False
#     return True

# def sudoku_validator(grid):
#     return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)