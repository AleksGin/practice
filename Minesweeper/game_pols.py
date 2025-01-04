from cells import Cell
import random


class GamePole:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for i_ in range(N)]
        self.init()

    def init(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.around_mines = 0
                cell.mine = False
                cell.fl_open = False

        mines_placed = 0
        while mines_placed < self.M:
            x = random.randint(0, self.N - 1)
            y = random.randint(0, self.N - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                mines_placed += 1
                self._update_around_mines(x, y)

    def _update_around_mines(self, x: int, y: int) -> None:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.N and 0 <= ny < self.N and not (dx == 0 and dy == 0):
                    self.pole[nx][ny].around_mines += 1

    def show(self) -> None:
        for row in self.pole:
            print(
                " ".join(
                    "*"
                    if cell.mine and cell.fl_open
                    else str(cell.around_mines)
                    if cell.fl_open
                    else "#"
                    for cell in row
                )
            )


pole_game = GamePole(10, 12)
