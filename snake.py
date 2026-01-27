from turtle import Turtle

# Initial positions for the snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distance to move the snake in each step
MOVE_DISTANCE = 20
# Turtle screen directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Initialize the snake with starting positions
        self.snake_segments = []
        self.create_snake()
        # Set the snake head as the first segment
        self.head = self.snake_segments[0]
        self.head.shape("circle")

    def create_snake(self):
        # Create the initial snake with three segments
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        # Add the new snake segment to the list
        self.snake_segments.append(snake)

    def extend_segment(self):
        self.add_segments(self.snake_segments[-1].position())

    def move(self):
        # Move the snake forward by updating the positions of each segment
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x_index = self.snake_segments[seg_num - 1].xcor()
            y_index = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x_index, y_index)
        # Move the head of the snake forward
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        # Turn the snake left
        self.head.left(90)

    def right(self):
        # Turn the snake right
        self.head.right(90)
