PLAYER_ONE=1
PLAYER_TWO=2

class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
    
    def set_pick(self, player, place):
        self.board[int(place/3)][place%3] = player

    def print(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])