# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:37:38 2014

Game of Tic Tac Toe

TO DO:
- Allow for arbitrary dimensions!? (by changing board & directions)

"""

import re

class TicTacToe:
    
    # Directions for checking result
    directions = [(i,j) for i in [0,1] for j in [0,1]]
    directions.remove((0,0))
    
    def __init__(self, width=3, height=3, num_players=2, win_length=3):
        self.width = width
        self.height = height
        self.num_players = num_players
        self.win_length = win_length # Number of consecutive marks to win
        # Since lists are mutable, need to use list comprehension below
        self.board = [['-']*width for i in range(height)]       
        self.turn = 1
        self.winner = None
        
    def __repr__(self):
        # TO DO: Tie padding to max of width        
        col_display = '  %s  '*self.width % tuple([j for j in range(self.width)])
        board_display = '%s%s\n' % ('   ', col_display)
        for i, r in enumerate(self.board):
            row_display = '  %s  '*self.width % tuple(r)
            board_display += '%s%s\n' % (' %d '%i, row_display)
        return board_display
    
    def move(self, i, j, verbose=True):
        """ Make move at (i,j)
        """
        if self.winner:
            raise Exception('Player %d has already won the game!' % self.winner)
        else:
            if self.board[i][j] != '-':            
                raise Exception('That cell is already occupied!')
            else:
                self.board[i][j] = self.turn
                if verbose:
                    print 'Player %d played (%d, %d)' % (self.turn, i, j)
                    print 'Board is now: '
                    print self
                self.check_win(i, j, self.turn)
                self.turn = self.turn % self.num_players + 1 # Increment turn
    
    def possible_moves(self):
        """ List of possible moves
        """
        return [(i,j) for i in range(self.width) for j in range(self.height) if self.board[i][j] == '-']

    def check_win(self, i, j, player):
        """ Check for a win by looking in all directions from (i,j)
        """        
        for d in self.directions:            
            consec = 1
            
            for l in range(1,self.win_length):
                i_inc = i+d[0]*l
                j_inc = j+d[1]*l
                # Check if off the board
                if 0 <= i_inc < self.width and 0 <= j_inc < self.height:
                    pass                    
                else:
                    break
                # Count consecutive marks in forward direction
                if self.board[i_inc][j_inc] == player:
                    consec += 1
                else:                    
                    break
                
            for l in range(1,self.win_length):
                # Check if off the board
                i_inc = i-d[0]*l
                j_inc = j-d[1]*l
                if 0 <= i_inc < self.width and 0 <= j_inc < self.height:
                    pass
                else:
                    break
                # Count consecutive marks in backwards direction                
                if self.board[i_inc][j_inc] == player:
                    consec += 1
                else:
                    break
                
            # If more consecutive marks than self.win_length, then player wins
            if consec >= self.win_length:
                self.winner = player
                print 'Player %d wins!' % player
                break
            
        def check_cats_game(self):
            """ TO DO: Determine if the game is still winnable or not...
            """
            pass

def main():
    print 'Welcome to Tic-Tac-Toe!'
    default = input('Enter 1 to play with default settings, 0 otherwise: ')
    if default==1:
        ttc = TicTacToe()
    elif default==0:
        width = input('Enter the board width: ')
        height = input('Enter the board height: ')
        win_length = input('Enter the number of consecutive marks needed to win: ')
        num_players = input('Enter the number of players: ')
        ttc = TicTacToe(width=width, height=height, 
                        win_length=win_length,
                        num_players=num_players)
    print ttc
    while ttc.winner is None:        
        move_str = str(input('Player %d, enter your move as i,j (e.g. 1,2): ' % ttc.turn))        
        try:            
            i,j = re.sub('[^0-9,]','',move_str.strip()).split(',')
            ttc.move(int(i),int(j))
        except:
            print 'Cannot understand the move you entered'            
    
if __name__=='__main__':
    main()
    