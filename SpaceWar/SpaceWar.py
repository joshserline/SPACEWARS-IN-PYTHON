import os
import random
import time



#Importing Turtle FRFR
import turtle
#required by macos or soemthing
turtle.fd(0)
#set the animation spped to the brrrrrrrrrrrrrrrrrrr
turtle.speed(0)
#background or something
turtle.bgcolor("black")
#title or something
turtle.title("Space War")
#BACKGROUND  WHHEHEHHEHE
turtle.bgpic("MOON.gif")
#hide the tortoise
turtle.ht()
#save the madafuckin memory
turtle.setundobuffer(1)
#this speeds the drawing frfr
turtle.tracer(0)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)

        self.speed = 1

    def move(self):
        self.fd(self.speed)

        #making my player know its boundries
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() >290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
         (self.xcor() <= (other.xcor() + 20)) and \
         (self.xcor() >= (other.ycor() - 20)) and \
         (self.xcor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1



#the enemy of my enemy is my freind
class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        #making my player know its boundries
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() >290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)



class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "firing":
            self.fd(self.speed)

        #xheking da bodeh
        if self.xcor() < -290 or self.xcor() >290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, 1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
         self.fd(10)
         self.frame += 1

        if self.frame >15:
            self.frame = 0
            self.goto(-1000, 1000)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #BUilldiong the wall/border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for sode in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))


#creat the game jobjection
game = Game()

#Drawing the wall again
game.draw_border()

#SHOWING THE STATUS OF THE GAME
game.show_status()

#sprites ONG
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
#ally = Ally("square", "blue", 0, 0)

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 0, 0))

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

#Key board bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#main game loop
while True:
    turtle.update()
    time.sleep(0.02)

    player.move()
    missile.move()


    for enemy in enemies:
        enemy.move()

        # Checking if my player doesnt know his bonderies
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score -= 100
            game.show_status()

        # checking the collision of the missile on the enemy
        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # increasing the score UWU
            game.score += 100
            game.show_status()
            #BOOM
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())


    for ally in allies:
        ally.move()

        # checking the collision of the missile on the on da freind
        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            #DEEEECREAAAAAESE THE SCORE
            game.score -= 50
            game.show_status()

        for particle in particles:
            particle.move

delay = input("press enter to finish. >")
























