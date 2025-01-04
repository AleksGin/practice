class Cell:
    def __init__(self, mine: bool, fl_open: bool = False, around_mines: int = 0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open