from pre import Clean
Clean.cls()

import tkinter as tk

class DrawingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, bg="white", width=600, height=400)
        self.canvas.pack()

        self.bind("<B1-Motion>", self.draw_line)
        self.bind("<Button-3>", self.draw_rect)

    def draw_line(self, event):
        x1, y1 = (event.x), (event.y)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_line(x1, y1, x2, y2)

    def draw_rect(self, event):
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == "__main__":
    app = DrawingApp()
    app.mainloop()
