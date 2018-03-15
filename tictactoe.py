'''
    Tic Tac Toe

    Each player an x or o.
    In a 3x3 board until board is full or one player connects three pieces.

    1)  Create a new board.
    2)  Xs place their piece.
        a) check if the cell is valid first
    3)  Check for win
        a) check for current row
        b) check current column
        c) if on either diagonal, check diagonal

    4)  Os place their piece.
        a) Check if the cell is valid.
    5)  check for win
    6)  Reapeat until win or all 9 slots filled.

'''



class Board():
    def __init__(self):
        self.board=[[1,2,3],[4,5,6],[7,8,9]]
        self.player=0
        self.start()

    def print1(self):
        #print self.player

        print ""
        print ""
        print "#####################################################################"
        print ""
        print "Curent Board:"
        print " ---","---","---"
        print "|",self.board[0][0],"|",self.board[0][1],"|",self.board[0][2],"|"
        print " ---","---","---"
        print "|",self.board[1][0],"|",self.board[1][1],"|",self.board[1][2],"|"
        print " ---","---","---"
        print "|",self.board[2][0],"|",self.board[2][1],"|",self.board[2][2],"|"
        print " ---","---","---"
        print ''
        print ""

    def won(self,index):
        piece=self.board[(index-1)/3][(index-1)%3]

        #count frequency horizontally
        count=0
        for i in range(3):
            if self.board[(index-1)/3][i] == piece:
                count+=1
        if count == 3:
            return True

        #count frequency vertically
        count=0
        for i in range(3):
            if self.board[i][(index-1)%3] == piece:
                count+=1
        if count == 3:
            return True

        #count frequency 1 diagonally
        count=0
        for i in range(3):
            if self.board[i][i] == piece:
                count+=1
        if count == 3:
            return True

        #count frequency 2 diagonally
        count=0
        for i in range(2,-1,-1):
            if self.board[2-i][i] == piece:
                count+=1
        if count == 3:
            return True

        #.....#

        return False

    def place(self):
        p=raw_input("Player1 write the cell number for X! : ")
        index=int(p)
        while (self.board[(index-1)/3][(index-1)%3] == "X" or self.board[(index-1)/3][(index-1)%3] == "o"):
            p=raw_input("Player1 write the cell number for X! : ",)
            index=int(p)
        self.board[(index-1)/3][(index-1)%3] = "X"
        self.player+=1
        self.print1()

        if self.won(index):
            return True,1

        if self.player == 9:
            return False,3

        p=raw_input("Player2 write the cell number for o! : ")
        index=int(p)
        while (self.board[(index-1)/3][(index-1)%3] == "X" or self.board[(index-1)/3][(index-1)%3] == "X"):
            p=raw_input("Wrong Cell! Player2 write the cell number for o! : ")
            index=int(p)
        self.board[(index-1)/3][(index-1)%3] = "o"
        self.player+=1
        self.print1()
        if self.won(index):
            return True,2

        return False,0

    def start(self):
        self.print1()
        a1=False
        count=0
        pl=0
        while(not a1 and pl!=3):
            a1,pl=self.place()

        if pl==3:
            print "Ooops! Match Draw!!"
            return
        print "Congrats!! Player",pl,"won the match!"

    def turn(self):
        return self.player%2

a=Board()

