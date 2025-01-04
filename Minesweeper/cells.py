class Cell:
    def __init__(self, mine: bool = False, around_mines: int = 0) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False