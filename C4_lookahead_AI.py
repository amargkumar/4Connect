# C4_lookahead_AI
# Name: Amar Kumar

import random

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]
        
        # do not need to return inside a constructor!


    def __repr2__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '-'*(self.width*2) + '-\n'
        for col in range(self.width):
            s += ' ' + str(col%10)
        

        return s


        
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it

    def set_board(self, LoS):
        """ this method returns a string representation
            for an object of type Board
        """
        for row in range( self.height ):
            for col in range( self.width ):
                self.data[row][col] = LoS[row][col]

    def setBoard( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print(self)    

    def set( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print(self)

    def clear( self ):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1


    def winsFor( self, ox ):
        for row in range(self.height - 3 ):
            for col in range(self.width - 3 ):
                if self.data[row][col] == ox and\
                   self.data[row+1][col+1] == ox and\
                   self.data[row+2][col+2] == ox and\
                   self.data[row+3][col+3] == ox:
                    return True

        return False
                
        

    def addMove2( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove( self, col ):
        """ removes the checker from column col """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return
        

    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull( self ):
        """ returns True if the board is completely full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True

    def gameOver( self ):
        """ returns True if the game is over... """
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX( self, row, col, ox ):
        """ checks if the spot at row, col is legal and ox """
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor( self, ox ):
        """ checks if the board self is a win for ox """
        for row in range( self.height ):
            for col in range( self.width ):
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col, ox ) and \
                   self.isOX( row+2, col, ox ) and \
                   self.isOX( row+3, col, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row, col+1, ox ) and \
                   self.isOX( row, col+2, ox ) and \
                   self.isOX( row, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col+1, ox ) and \
                   self.isOX( row+2, col+2, ox ) and \
                   self.isOX( row+3, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col-1, ox ) and \
                   self.isOX( row+2, col-2, ox ) and \
                   self.isOX( row+3, col-3, ox ):
                    return True
        return False

# Here is a version of hostGame for use in your Board class
#
# it simply alternates moves in the game and checks if
# the game is over at each move


    def hostGame( self ):
        """ hosts a game of Connect Four """

        nextCheckerToMove = 'X'

class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ 
        This is a constructor for Player objects that takes three arguments. 
        This constructor first takes in a one-character string ox: this will be either 'X' or 'O'. 
        Second, it takes in tbt, a string representing the tiebreaking type of the player. 
        It will be one of 'LEFT', 'RIGHT', or 'RANDOM'. 
        The third input ply will be a nonnegative integer representing the number of moves that the 
        player should look into the future when evaluating where to go next.
        """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string
        This method returns a string representing the Player object that calls it. 
        Prints the three important characteristics of the object: its checker string, its tiebreaking type, and its ply.  
        """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s
    
    def oppCh(self):
        """
        This method should return the other kind of checker or playing piece, i.e., the piece being played by self's opponent. 
        In particular, if self is playing 'X', this method returns 'O' and vice-versa. 
        """
        if self.ox == 'X':
            return 'O'
        else:
            return 'X'
        
    def scoreBoard(self, b):
        """
        Return a single float value representing the score of the input b, 
        This should return 100.0 if the board b is a win for self. 
        Returns 50.0 if it is neither a win nor a loss for self, and 
        Returns 0.0 if it is a loss for self (i.e., the opponent won).
        """

        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0
        
    def tiebreakMove(self, scores):
        """
        This method takes in scores, which will be a nonempty list of floating-point numbers. 
        If there is only one highest score in that scores list, returns its COLUMN number, 
        If there is more than one highest score because of a tie, returns the COLUMN number of the highest score 
        appropriate to the player's tiebreaking type.
        """

        maxval = max(scores)
        listind = []
        for c in range(len(scores)):
            if scores[c] == maxval:
                listind = listind + [c]

        if self.tbt == 'LEFT':
            return listind[0]
        elif self.tbt == 'RIGHT':
            return listind[-1]
        else:
            return random.choice(listind)
        

    def scoresFor(self, b):
        """
        Returns a list of scores, with the cth score representing the "goodness" of the input board after the player moves
        to column c. Goodness is measured by what happens in the game after self.ply moves.
        """
        scores = [50]*b.width
        for i in range(b.width):
            if not b.allowsMove(i):
                scores[i] = -1.0
            if b.winsFor(self.ox):
                scores[i] = 100.0
            if b.winsFor(self.oppCh()):
                scores[i] = 0.0
            if self.ply == 0:
                scores[i] = 50.0
            
    # Need Some Help!
    
    def nextMove(self, b):
        """
        This method takes in b, an object of type Board and returns an integer -- 
        namely, the column number that the calling object (of class Player) chooses to move to.
        """
        scores = self.scoreFor(b)
        return self.tiebreakMove(scores)
        
        
