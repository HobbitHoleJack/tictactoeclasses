class board():
  board = {
    1:" ",
    2:" ",
    3:" ",
    4:" ",
    5:" ",
    6:" ",
    7:" ",
    8:" ",
    9:" "
  }

  def move(self, player, square):
    if self.board[square] == " ":
      self.board[square] = player

  def reset(self):
    self.board = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
  }

  def print(self):
    print(self.board[1], "|", self.board[2], "|", self.board[3])
    print("---------")
    print(self.board[4], "|", self.board[5], "|", self.board[6])
    print("---------")
    print(self.board[7], "|", self.board[8], "|", self.board[9], "\n")

  def testmove(self, player, move):
    temp = self.board
    if temp[move] == " ":
      if temp

  def state(self):
    if self.board[1] == "x" and self.board[2] == "x" and self.board[3] == "x":
      return "x"
    if self.board[4] == "x" and self.board[5] == "x" and self.board[6] == "x":
      return "x"
    if self.board[7] == "x" and self.board[8] == "x" and self.board[9] == "x":
      return "x"
    if self.board[1] == "x" and self.board[5] == "x" and self.board[9] == "x":
      return "x"
    if self.board[3] == "x" and self.board[5] == "x" and self.board[7] == "x":
      return "x"
    if self.board[1] == "x" and self.board[4] == "x" and self.board[7] == "x":
      return "x"
    if self.board[2] == "x" and self.board[5] == "x" and self.board[8] == "x":
      return "x"
    if self.board[3] == "x" and self.board[6] == "x" and self.board[9] == "x":
      return "x"

    if self.board[1] == "o" and self.board[2] == "o" and self.board[3] == "o":
      return "o"
    if self.board[4] == "o" and self.board[5] == "o" and self.board[6] == "o":
      return "o"
    if self.board[7] == "o" and self.board[8] == "o" and self.board[9] == "o":
      return "o"
    if self.board[1] == "o" and self.board[5] == "o" and self.board[9] == "o":
      return "o"
    if self.board[3] == "o" and self.board[5] == "o" and self.board[7] == "o":
      return "o"
    if self.board[1] == "o" and self.board[4] == "o" and self.board[7] == "o":
      return "o"
    if self.board[2] == "o" and self.board[5] == "o" and self.board[8] == "o":
      return "o"
    if self.board[3] == "o" and self.board[6] == "o" and self.board[9] == "o":
      return "o"

    filled = 0
    for x in self.board:
      if self.board[x] != " ":
        filled += 1
    if filled == 9:
      return "draw" 
    else:
      return "playing"
        
board = board()
