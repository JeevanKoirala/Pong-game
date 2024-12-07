import tkinter as tk

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()

      
        self.paddle_width = 20
        self.paddle_height = 100
        self.ball_size = 20
        
      
        self.left_paddle = self.canvas.create_rectangle(30, 150, 30 + self.paddle_width, 150 + self.paddle_height, fill="white")
        self.right_paddle = self.canvas.create_rectangle(750 - self.paddle_width, 150, 750, 150 + self.paddle_height, fill="white")
        self.ball = self.canvas.create_oval(390, 190, 390 + self.ball_size, 190 + self.ball_size, fill="white")
        
        
        self.ball_dx = 3
        self.ball_dy = 3
        
       
        self.left_paddle_dy = 0
        self.right_paddle_dy = 0
        
        
        self.left_score = 0
        self.right_score = 0
        self.score_display = self.canvas.create_text(400, 20, text=f"{self.left_score} - {self.right_score}", fill="white", font=('Arial', 24))

        
        self.root.bind("<w>", self.move_left_paddle_up)
        self.root.bind("<s>", self.move_left_paddle_down)
        self.root.bind("<Up>", self.move_right_paddle_up)
        self.root.bind("<Down>", self.move_right_paddle_down)
        
        self.update_game()

    def move_left_paddle_up(self, event):
        self.left_paddle_dy = -4

    def move_left_paddle_down(self, event):
        self.left_paddle_dy = 4

    def move_right_paddle_up(self, event):
        self.right_paddle_dy = -4

    def move_right_paddle_down(self, event):
        self.right_paddle_dy = 4

    def update_game(self):
        
        self.canvas.move(self.left_paddle, 0, self.left_paddle_dy)
        self.canvas.move(self.right_paddle, 0, self.right_paddle_dy)

        
        self.check_paddle_bounds(self.left_paddle)
        self.check_paddle_bounds(self.right_paddle)

        
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)

       
        ball_coords = self.canvas.coords(self.ball)

        
        if ball_coords[1] <= 0 or ball_coords[3] >= 400:
            self.ball_dy = -self.ball_dy
        
        
        if self.check_collision(self.left_paddle, ball_coords):
            self.ball_dx = -self.ball_dx
        if self.check_collision(self.right_paddle, ball_coords):
            self.ball_dx = -self.ball_dx
        
       
        if ball_coords[0] <= 0:
            self.right_score += 1
            self.reset_ball()
        if ball_coords[2] >= 800:
            self.left_score += 1
            self.reset_ball()

        
        self.canvas.itemconfig(self.score_display, text=f"{self.left_score} - {self.right_score}")

        
        self.root.after(10, self.update_game)

    def check_paddle_bounds(self, paddle):
        coords = self.canvas.coords(paddle)
        if coords[1] < 0:
            self.canvas.move(paddle, 0, 4)
        if coords[3] > 400:
            self.canvas.move(paddle, 0, -4)

    def check_collision(self, paddle, ball_coords):
        paddle_coords = self.canvas.coords(paddle)
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2] and
            ball_coords[3] >= paddle_coords[1] and ball_coords[1] <= paddle_coords[3]):
            return True
        return False

    def reset_ball(self):
        self.canvas.coords(self.ball, 390, 190, 390 + self.ball_size, 190 + self.ball_size)
        self.ball_dx = -self.ball_dx

root = tk.Tk()
game = PongGame(root)
root.mainloop()