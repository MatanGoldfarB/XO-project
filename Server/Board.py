PLAYER_ONE=1
PLAYER_TWO=2

class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
    
    def set_pick(self, player, place):
        self.board[int(place/3)][place%3] = player

    def checkBoard(self):
        for i in range(3):
            if(self.board[0][i]==self.board[1][i]==self.board[2][i]):
                return self.board[0][i]
            if(self.board[i][0]==self.board[i][1]==self.board[i][2]):
                return self.board[i][0]
        if(self.board[0][0]==self.board[1][1]==self.board[2][2] or
           self.board[0][2]==self.board[1][1]==self.board[2][0]):
            return self.board[1][1]

    def clear(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def print(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])