import tkinter as tk
import random

# Constants
WIDTH = 10
HEIGHT = 20
BLOCK_SIZE = 30
DELAY = 500  # in milliseconds

# Colors
BG_COLOR = "black"
BLOCK_COLORS = ["cyan", "blue", "orange", "yellow", "green", "purple", "red"]

class TetrisGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tetris")

        self.canvas = tk.Canvas(self.root, width=WIDTH * BLOCK_SIZE, height=HEIGHT * BLOCK_SIZE, bg=BG_COLOR)
        self.canvas.pack()

        self.board = [[0] * WIDTH for _ in range(HEIGHT)]
        self.current_tetromino = None
        self.score = 0

        self.draw_board()
        self.spawn_tetromino()

        self.bind_keys()
        self.run()

    def bind_keys(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.rotate)

    def draw_board(self):
        self.canvas.delete("all")
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.board[y][x] != 0:
                    color = BLOCK_COLORS[self.board[y][x] - 1]
                    self.canvas.create_rectangle(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                                 (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE,
                                                 fill=color)

    def spawn_tetromino(self):
        tetrominoes = [[(0, 0), (1, 0), (2, 0), (3, 0)],  # I
                       [(1, 0), (0, 1), (1, 1), (2, 1)],  # O
                       [(0, 0), (0, 1), (1, 1), (2, 1)],  # L
                       [(2, 0), (0, 1), (1, 1), (2, 1)],  # J
                       [(1, 0), (2, 0), (0, 1), (1, 1)],  # S
                       [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
                       [(1, 0), (0, 1), (1, 1), (2, 1)]]  # T

        tetromino = random.choice(tetrominoes)
        self.current_tetromino = tetromino
        self.draw_tetromino()

    def draw_tetromino(self):
        for block in self.current_tetromino:
            x, y = block
            color = BLOCK_COLORS[len(BLOCK_COLORS) - 1]
            self.canvas.create_rectangle(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                         (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE,
                                         fill=color)

    def move_down(self, event=None):
        self.canvas.after_cancel(self.game_loop)
        self.clear_tetromino()
        if self.check_collision(0, 1):
            self.merge_tetromino()
            self.spawn_tetromino()
            self.draw_board()
            self.check_completed_lines()
        else:
            for block in self.current_tetromino:
                block[1] += 1
            self.draw_tetromino()
            self.game_loop = self.canvas.after(DELAY, self.move_down)

    def move_left(self, event=None):
        self.canvas.after_cancel(self.game_loop)
        self.clear_tetromino()
        if self.check_collision(-1, 0):
            for block in self.current_tetromino:
                block[0] -= 1
            self.draw_tetromino()
        else:
            self.draw_tetromino()
            self.game_loop = self.canvas.after(DELAY, self.move_down)

    def move_right(self, event=None):
        self.canvas.after_cancel(self.game_loop)
        self.clear_tetromino()
        if self.check_collision(1, 0):
            for block in self.current_tetromino:
                block[0] += 1
            self.draw_tetromino()
        else:
            self.draw_tetromino()
            self.game_loop = self.canvas.after(DELAY, self.move_down)

    def rotate(self, event=None):
        self.canvas.after_cancel(self.game_loop)
        self.clear_tetromino()
        # Rotate the tetromino
        # Add rotation logic here
        self.draw_tetromino()
        self.game_loop = self.canvas.after(DELAY, self.move_down)

    def clear_tetromino(self):
        for block in self.current_tetromino:
            x, y = block
            self.canvas.create_rectangle(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                         (x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE,
                                         fill=BG_COLOR)

    def check_collision(self, dx, dy):
        for block in self.current_tetromino:
            x, y = block
            if x + dx < 0 or x + dx >= WIDTH or y + dy >= HEIGHT:
                return False
            if self.board[y + dy][x + dx] != 0:
                return False
        return True

    def merge_tetromino(self):
        for block in self.current_tetromino:
            x, y = block
            self.board[y][x] = len(BLOCK_COLORS) - 1

    def check_completed_lines(self):
        completed_lines = [i for i, row in enumerate(self.board) if all(row)]
        for line in completed_lines:
            self.score += 1
            self.board.pop(line)
            self.board.insert(0, [0] * WIDTH)
        self.draw_board()

    def run(self):
        self.game_loop = self.canvas.after(DELAY, self.move_down)
        self.root.mainloop()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
