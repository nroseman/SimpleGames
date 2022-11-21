from random import random, choice

# Global Variables
BASE = 3
LINES = BASE * BASE  # num of rows and columns
CHOICES = [x + 1 for x in range(LINES)]
grid = {}
box_list = []
retry = True


class Cell:
    def __init__(self, x, y) -> None:
        self.value = 0
        self.row = y
        self.col = x
        self.set_box()

    def set_box(self):
        row = self.row // BASE
        col = self.col // BASE

        if col == 0:
            if row == 0:
                self.box = 0
            elif row == 1:
                self.box = 1
            else:
                self.box = 2
        elif col == 1:
            if row == 0:
                self.box = 3
            elif row == 1:
                self.box = 4
            else:
                self.box = 5
        else:
            if row == 0:
                self.box = 6
            elif row == 1:
                self.box = 7
            else:
                self.box = 8


class Box:
    def __init__(self) -> None:
        self.cells = []

    def add(self, cell):
        self.cells.append(cell)

    def get_cells(self):
        return self.cells

    def fill(self):
        avail_list = CHOICES.copy()
        for cell in self.cells:
            value = choice(avail_list)
            cell.value = value
            avail_list.remove(value)


class Grid:
    def __init__(self) -> None:
        self.board = [[] for rows in range(LINES)]
        self.box_list = [Box() for boxes in range(LINES)]
        self.cell_list = []
        self.new_grid()

    def new_grid(self):
        # generate empty board, boxes and cells
        for row in range(LINES):
            for col in range(LINES):
                cell = Cell(col, row)
                self.board[row].append(cell)
                self.box_list[cell.box].add(cell)
                self.cell_list.append(cell)

    def print_grid(self):
        final_string = ''
        for row in self.board:
            lists = []
            for cell in row:
                lists.append(cell.value)
                final_string += f'{cell.value}'
            print(lists)
        print(final_string)

    def fill_cell(self):
        for cell in self.cell_list:
            if not cell.value:
                avail_list = CHOICES.copy()
                filled_list = []
                filled_list.extend(self.check_row(cell))
                filled_list.extend(self.check_col(cell))
                filled_list.extend(self.check_box(cell))
                avail_list = [
                    num for num in avail_list if num not in filled_list]
                cell.value = choice(avail_list)

    def check_row(self, cell):
        filled_list = []
        for c in self.board[cell.row]:
            if c.value:
                filled_list.append(c.value)
        return filled_list

    def check_col(self, cell):
        filled_list = []
        for row in self.board:
            if row[cell.col].value:
                filled_list.append(row[cell.col].value)
        return filled_list

    def check_box(self, cell):
        filled_list = []
        for c in self.box_list[cell.box].cells:
            if c.value:
                filled_list.append(c.value)
        return filled_list


def main():
    tries = 0
    while tries < 10000:
        try:
            grid = Grid()
            grid.box_list[0].fill()
            grid.box_list[4].fill()
            grid.box_list[8].fill()
            grid.fill_cell()
        except:
            tries += 1
            print(f'Retry: {tries}')
        else:
            grid.print_grid()

            exit()


if __name__ == '__main__':
    main()
