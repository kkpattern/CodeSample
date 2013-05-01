# Problem
#
# Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts
# empty, except that a single 'T' symbol may appear in one of the 16 squares.
# There are two players: X and O. They take turns to make moves, with X
# starting. In each move a player puts her symbol in one of the empty squares.
# Player X's symbol is 'X', and player O's symbol is 'O'.
#
# After a player's move, if there is a row, column or a diagonal containing 4
# of that player's symbols, or containing 3 of her symbols and the 'T' symbol,
# she wins and the game ends. Otherwise the game continues with the other
# player's move. If all of the fields are filled with symbols and nobody won,
# the game ends in a draw. See the sample input for examples of various winning
# positions.
#
# Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters
# (where '.' represents an empty square), describing the current state of a
# game, determine the status of the Tic-Tac-Toe-Tomek game going on. The
# statuses to choose from are:
#
#     "X won" (the game is over, and X won)
#      "O won" (the game is over, and O won)
#      "Draw" (the game is over, and it ended in a draw)
#      "Game has not completed" (the game is not over yet)
#
# If there are empty cells, and the game is not over, you
# should output "Game has not completed", even if the outcome
# of the game is inevitable.
#
# Input
#
# The first line of the input gives the number of test cases,
# T. T test cases follow. Each test case consists of 4 lines
# with 4 characters each, with each character being 'X', 'O',
# '.' or 'T' (quotes for clarity only). Each test case is
# followed by an empty line.
#
# Output
#
# For each test case, output one line containing "Case #x: y",
# where x is the case number (starting from 1) and y is one of
# the statuses given above. Make sure to get the statuses
# exactly right. When you run your code on the sample input, it
# should create the sample output exactly, including the "Case
# #1: ", the capital letter "O" rather than the number "0", and
# so on.
#
# Limits
#
# The game board provided will represent a valid state that was
# reached through play of the game Tic-Tac-Toe-Tomek as
# described above.
#
# Small dataset
#
# 1 ≤ T ≤ 10.
#
# Large dataset
#
# 1 ≤ T ≤ 1000. 


def if_win(board, c):
    for ri in xrange(4):
        win = True
        for ci in xrange(4):
            if board[ri][ci] != c and board[ri][ci] != 'T':
                win = False
                break
        if win: return True
    for ci in xrange(4):
        win = True
        for ri in xrange(4):
            if board[ri][ci] != c and board[ri][ci] != 'T':
                win = False
                break
        if win: return True
    win = True
    for di in xrange(4):
        if board[di][di] != c and board[di][di] != 'T':
            win = False
            break
    if win: return True
    win = True
    for di in xrange(4):
        if board[3-di][di] != c and board[3-di][di] != 'T':
            win = False
            break
    if win: return True
    return False

def main():
    T = int(raw_input())
    for ti in xrange(T):
        print "Case #{0}:".format(ti+1),
        board = [raw_input() for i in xrange(4)]
        try:
            raw_input()
        except EOFError:
            pass

        if if_win(board, 'X'):
            print "X won"
        elif if_win(board, 'O'):
            print "O won"
        else:
            draw = True
            for ri in range(4):
                for ci in range(4):
                    if board[ri][ci] == '.':
                        draw = False
                        break
            if draw:
                print "Draw"
            else:
                print "Game has not completed"

    pass

if __name__ == "__main__":
    main()
