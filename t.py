import tkinter as tk
import random

colors = [
    "black", "purple", "cyan", "brown", "green", "red", "pink"
]

class Figure:
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
    def __init__(self, root, height=20, width=10):
        self.root = root
        self.level = 2
        self.score = 0
        self.state = "start"
        self.height = height
        self.width = width
        self.zoom = 20
        self.canvas = tk.Canvas(root, width=width * self.zoom + 5, height=height * self.zoom + 5, bg="white")
        self.canvas.pack()
        self.field = [[0 for _ in range(width)] for _ in range(height)]
        self.figure = None
        self.root.bind("<KeyPress>", self.control)
        self.game_tick()

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if (i + self.figure.y >= self.height or j + self.figure.x >= self.width or j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0):
                        return True
        return False

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self):
        lines = 0
        for i in range(self.height - 1, -1, -1):
            if all(self.field[i]):
                del self.field[i]
                self.field.insert(0, [0 for _ in range(self.width)])
                lines += 1
        self.score += lines ** 2

    def move_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def move_side(self, dx):
        self.figure.x += dx
        if self.intersects():
            self.figure.x -= dx

    def rotate(self):
        prev_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = prev_rotation

    def control(self, event):
        if self.state == "gameover":
            return
        if event.keysym == "Left":
            self.move_side(-1)
        elif event.keysym == "Right":
            self.move_side(1)
        elif event.keysym == "Down":
            self.move_down()
        elif event.keysym == "Up":
            self.rotate()
        elif event.keysym == "space":
            while not self.intersects():
                self.figure.y += 1
            self.figure.y -= 1
            self.freeze()
        self.draw()

    def game_tick(self):
        if self.state == "start":
            if self.figure is None:
                self.new_figure()
            self.move_down()
            self.draw()
        self.root.after(300, self.game_tick)

    def draw(self):
        self.canvas.delete("all")
        for i in range(self.height):
            for j in range(self.width):
                color = colors[self.field[i][j]] if self.field[i][j] else "gray"
                self.canvas.create_rectangle(j * self.zoom, i * self.zoom, (j + 1) * self.zoom, (i + 1) * self.zoom, outline="black", fill=color)
        if self.figure:
            for i in range(4):
                for j in range(4):
                    if i * 4 + j in self.figure.image():
                        x, y = (j + self.figure.x) * self.zoom, (i + self.figure.y) * self.zoom
                        self.canvas.create_rectangle(x, y, x + self.zoom, y + self.zoom, outline="black", fill=colors[self.figure.color])
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="black")
        if self.state == "gameover":
            self.canvas.create_text(100, 200, text="Game Over", fill="red", font=("Arial", 20))


root = tk.Tk()
root.title("Tetris in Tkinter")
game = Tetris(root)
root.mainloop()шщ