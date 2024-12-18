from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]
move_dis = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for p in pos:
            self.add_segment(p)

    def add_segment(self, position):
        seg = Turtle(shape='square')
        seg.color('white')
        seg.penup()
        seg.goto(position)
        self.segment.append(seg)
    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            x = self.segment[i - 1].xcor()
            y = self.segment[i - 1].ycor()
            self.segment[i].goto(x, y)
            # time.sleep(1)

        self.head.forward(move_dis)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def wall_x(self):
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(-x, y)

    def wall_y(self):
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(x, -y)
