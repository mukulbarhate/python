import tkinter as tk
from tkinter import messagebox

# Sudoku puzzle (0 represents empty cells)
PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        
        self.grid = [[0] * 9 for _ in range(9)]
        self.cells = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            for j in range(9):
                if PUZZLE[i][j] != 0:
                    self.cells[i][j].set(PUZZLE[i][j])
                
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, textvariable=self.cells[i][j], width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j)
                if (i // 3 + j // 3) % 2 == 0:
                    entry['bg'] = 'light gray'

        solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        solve_button.grid(row=10, column=4, columnspan=2, pady=10)

    def solve(self):
        if self.solve_sudoku():
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].set(self.grid[i][j])
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku():
                    return True
                self.grid[row][col] = 0

        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def is_safe(self, row, col, num):
        return not self.used_in_row(row, num) and not self.used_in_col(col, num) and not self.used_in_box(row - row % 3, col - col % 3, num)

    def used_in_row(self, row, num):
        return num in self.grid[row]

    def used_in_col(self, col, num):
        return num in [self.grid[i][col] for i in range(9)]

    def used_in_box(self, start_row, start_col, num):
        return num in [self.grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]

def main():
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()







# ------------------------------------- SNAKE GAME ------------------------------

# import tkinter as tk
# import random
# import time

# # Constants
# WIDTH = 600
# HEIGHT = 400
# SNAKE_SIZE = 20
# DELAY = 0.1

# # Colors
# BG_COLOR = "white"
# SNAKE_COLOR = "green"
# FOOD_COLOR = "red"

# class SnakeGame:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Snake Game")
        
#         self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
#         self.canvas.pack()
        
#         self.snake = [(100, 100), (80, 100), (60, 100)]
#         self.food = self.create_food()
#         self.direction = "Right"
#         self.score = 0
        
#         self.bind_keys()
#         self.run()

#     def bind_keys(self):
#         self.root.bind("<KeyPress-Left>", self.go_left)
#         self.root.bind("<KeyPress-Right>", self.go_right)
#         self.root.bind("<KeyPress-Up>", self.go_up)
#         self.root.bind("<KeyPress-Down>", self.go_down)

#     def go_left(self, event):
#         if self.direction != "Right":
#             self.direction = "Left"

#     def go_right(self, event):
#         if self.direction != "Left":
#             self.direction = "Right"

#     def go_up(self, event):
#         if self.direction != "Down":
#             self.direction = "Up"

#     def go_down(self, event):
#         if self.direction != "Up":
#             self.direction = "Down"

#     def create_food(self):
#         x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
#         y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
#         return x, y

#     def move(self):
#         x, y = self.snake[0]
        
#         if self.direction == "Left":
#             x -= SNAKE_SIZE
#         elif self.direction == "Right":
#             x += SNAKE_SIZE
#         elif self.direction == "Up":
#             y -= SNAKE_SIZE
#         elif self.direction == "Down":
#             y += SNAKE_SIZE
        
#         self.snake.insert(0, (x, y))

#         if (x, y) == self.food:
#             self.score += 1
#             self.food = self.create_food()
#         else:
#             self.snake.pop()

#         if self.check_collision():
#             self.game_over()
#         else:
#             self.update_canvas()

#     def check_collision(self):
#         x, y = self.snake[0]
#         return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in self.snake[1:]

#     def update_canvas(self):
#         self.canvas.delete("all")

#         for segment in self.snake:
#             x, y = segment
#             self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR)

#         self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE, fill=FOOD_COLOR)

#         self.canvas.create_text(WIDTH / 2, 20, text=f"Score: {self.score}", fill="black")

#     def game_over(self):
#         self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", fill="red")
#         self.root.after_cancel(self.game_loop)

#     def run(self):
#         self.move()
#         self.game_loop = self.root.after(int(DELAY * 1000), self.run)

#     def start(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     game = SnakeGame()
#     game.start()





# --------------------------- TETRIS -------------------------------------------------
# import tkinter as tk
# import random
# import time

# # Constants
# WIDTH = 10
# HEIGHT = 20
# BLOCK_SIZE = 30
# DELAY = 0.5

# # Colors
# BG_COLOR = "black"
# BLOCK_COLORS = ["blue", "green", "red", "yellow", "orange", "purple", "cyan"]

# class TetrisGame:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Tetris")

#         self.canvas = tk.Canvas(self.root, width=WIDTH * BLOCK_SIZE, height=HEIGHT * BLOCK_SIZE, bg=BG_COLOR)
#         self.canvas.pack()

#         self.grid = [[0] * WIDTH for _ in range(HEIGHT)]
#         self.current_block = None
#         self.next_block = None
#         self.score = 0

#         self.generate_block()
#         self.bind_keys()
#         self.run()

#     def bind_keys(self):
#         self.root.bind("<Left>", self.move_left)
#         self.root.bind("<Right>", self.move_right)
#         self.root.bind("<Down>", self.move_down)
#         self.root.bind("<Up>", self.rotate_block)

#     def generate_block(self):
#         if self.next_block is None:
#             self.next_block = self.create_block()
#         self.current_block = self.next_block
#         self.next_block = self.create_block()
#         self.current_x = WIDTH // 2 - len(self.current_block[0]) // 2
#         self.current_y = 0
#         if self.check_collision(self.current_block, self.current_x, self.current_y):
#             self.game_over()
#         else:
#             self.draw_block(self.current_block, self.current_x, self.current_y)
#             self.draw_next_block()

#     def create_block(self):
#         block_types = [
#             [[1, 1, 1, 1]],  # I-block
#             [[1, 1, 1], [0, 1, 0]],  # T-block
#             [[1, 1, 1], [1, 0, 0]],  # L-block
#             [[1, 1, 1], [0, 0, 1]],  # J-block
#             [[1, 1], [1, 1]],  # O-block
#             [[1, 1, 0], [0, 1, 1]],  # S-block
#             [[0, 1, 1], [1, 1, 0]]   # Z-block
#         ]
#         return random.choice(block_types)

#     def draw_block(self, block, x, y):
#         for i in range(len(block)):
#             for j in range(len(block[i])):
#                 if block[i][j] == 1:
#                     self.canvas.create_rectangle((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE,
#                                                  (x + j + 1) * BLOCK_SIZE, (y + i + 1) * BLOCK_SIZE,
#                                                  fill=random.choice(BLOCK_COLORS))

#     def draw_next_block(self):
#         self.canvas.delete("next_block")
#         for i in range(len(self.next_block)):
#             for j in range(len(self.next_block[i])):
#                 if self.next_block[i][j] == 1:
#                     self.canvas.create_rectangle((WIDTH + j) * BLOCK_SIZE, (i + 2) * BLOCK_SIZE,
#                                                  (WIDTH + j + 1) * BLOCK_SIZE, (i + 3) * BLOCK_SIZE,
#                                                  fill=random.choice(BLOCK_COLORS), tag="next_block")

#     def move_left(self, event):
#         if not self.check_collision(self.current_block, self.current_x - 1, self.current_y):
#             self.erase_block(self.current_block, self.current_x, self.current_y)
#             self.current_x -= 1
#             self.draw_block(self.current_block, self.current_x, self.current_y)

#     def move_right(self, event):
#         if not self.check_collision(self.current_block, self.current_x + 1, self.current_y):
#             self.erase_block(self.current_block, self.current_x, self.current_y)
#             self.current_x += 1
#             self.draw_block(self.current_block, self.current_x, self.current_y)

#     def move_down(self, event):
#         if not self.check_collision(self.current_block, self.current_x, self.current_y + 1):
#             self.erase_block(self.current_block, self.current_x, self.current_y)
#             self.current_y += 1
#             self.draw_block(self.current_block, self.current_x, self.current_y)
#         else:
#             self.merge_block()
#             self.check_lines()
#             self.generate_block()

#     def rotate_block(self, event):
#         rotated_block = list(zip(*self.current_block[::-1]))
#         if not self.check_collision(rotated_block, self.current_x, self.current_y):
#             self.erase_block(self.current_block, self.current_x, self.current_y)
#             self.current_block = rotated_block
#             self.draw_block(self.current_block, self.current_x, self.current_y)

#     def check_collision(self, block, x, y):
#         for i in range(len(block)):
#             for j in range(len(block[i])):
#                 if block[i][j] == 1:
#                     if x + j < 0 or x + j >= WIDTH or y + i >= HEIGHT or self.grid[y + i][x + j] == 1:
#                         return True
#         return False

#     def merge_block(self):
#         for i in range(len(self.current_block)):
#             for j in range(len(self.current_block[i])):
#                 if self.current_block[i][j] == 1:
#                     self.grid[self.current_y + i][self.current_x + j] = 1

#     def erase_block(self, block, x, y):
#         for i in range(len(block)):
#             for j in range(len(block[i])):
#                 if block[i][j] == 1:
#                     self.canvas.create_rectangle((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE,
#                                                  (x + j + 1) * BLOCK_SIZE, (y + i + 1) * BLOCK_SIZE,
#                                                  fill=BG_COLOR)

#     def check_lines(self):
#         lines_to_clear = []
#         for i in range(HEIGHT):
#             if all(self.grid[i]):
#                 lines_to_clear.append(i)
#         if lines_to_clear:
#             self.score += len(lines_to_clear)
#             for line in lines_to_clear:
#                 self.grid.pop(line)
#                 self.grid.insert(0, [0] * WIDTH)
#             self.update_score()

#     def update_score(self):
#         self.canvas.delete("score")
#         self.canvas.create_text(WIDTH * BLOCK_SIZE // 2, HEIGHT * BLOCK_SIZE // 2,
#                                 text=f"Score: {self.score}", fill="white", font=("Arial", 20), tag="score")

#     def game_over(self):
#         self.canvas.delete("game_over")
#         self.canvas.create_text(WIDTH * BLOCK_SIZE // 2, HEIGHT * BLOCK_SIZE // 2,
#                                 text="Game Over", fill="red", font=("Arial", 30), tag="game_over")
#         self.root.after_cancel(self.game_loop)

#     def run(self):
#         if not self.check_collision(self.current_block, self.current_x, self.current_y + 1):
#             self.erase_block(self.current_block, self.current_x, self.current_y)
#             self.current_y += 1
#             self.draw_block(self.current_block, self.current_x, self.current_y)
#         else:
#             self.merge_block()
#             self.check_lines()
#             self.generate_block()
#         self.game_loop = self.root.after(int(DELAY * 1000), self.run)

#     def start(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     game = TetrisGame()
#     game.start()
