from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")
FONT2 = ("Arial", 24, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        #Initialize the ScoreBoard object.
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        #Adding a new highscore attribute now
        with open("highscore.txt","r") as file:
            self.highscore = int(file.read())
        self.update_score()

    def update_score(self):
        #Update current score
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            #print('new highscore')
            with open("highscore.txt", "w") as file:
                self.highscore = self.score
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", align=ALIGN, font=FONT2)
    #     self.goto(0, -50)
    #     self.write(f"Your score was: {self.score}", align=ALIGN, font=FONT)


    def increment_score(self):
        #Increment the score
        self.score += 1
        self.update_score()
