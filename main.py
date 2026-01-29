from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create a snake object
snake = Snake()

# Create a food object
food = Food()

# Create a ScoreBoard object to keep track of the score
score_board = ScoreBoard()

# Set up key bindings for snake movement
screen.listen()
# Changed to onkeypress for faster input
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

game_on = True  # Flag to control the game loop

while game_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Introduce a delay to control the speed of the game
    snake.move()  # Move the snake

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        score_board.increment_score()  # Increase the score
        food.refresh()  # Move the food to a new random location
        snake.extend_segment()  # Extend the snake by adding a new segment

    # Detect collision with the wall and let snake appear from opposite side
    if snake.head.xcor() > 280:
        snake.head.setpos(-280,snake.head.ycor())
    if snake.head.xcor() < -280:
        snake.head.setpos(280,snake.head.ycor())
    if snake.head.ycor() > 280:
        snake.head.setpos(snake.head.xcor(),-280)
    if snake.head.ycor() < -280:
        snake.head.setpos(snake.head.xcor(),280)


    # Detect collision with the snake's tail
    for segment in snake.snake_segments[1:]: #list slicing used
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            snake.reset()


# Close the window when clicked
screen.exitonclick()
