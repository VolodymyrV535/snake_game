from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.score = 0
        self.write_score()
        
        
    def add_score(self):
        self.score += 1
        self.write_score()
        
    
    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        