"""
CS241 "Pong 2 player"
Classes Written by: Nathan Taylor

File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCORE_HIT = 1
SCORE_MISS = 5

class Point:
    # This will initiate the point to be a float.
    def __init__ (self):
        self.x = float(0)
        self.y = float(0)
        self.t = float(0)
        self.z = float(0)
class Velocity:
    # This will initiate the velocity to be a float.
    
    def __init(self):
        self.dx = float(0)
        self.dy = float(0)
        
class Ball:
    # This initiates all the characteristics of the ball
    def __init__(self):
        
        self.center = Point()
        self.velocity = Velocity()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.velocity.dx = random.randint(3,5)
        self.velocity.dy = random.randint(-5,5)
        self.angle = 5
        
        
    def draw(self):
        """
        img = "Images/deathstar.png" #meteorGrey_big1
        texture = arcade.load_texture(img)
        
        width = texture.width / 10
        height = texture.height / 10
        alpha = 1
        
        #x = self.center.x
        #y = self.center.y
        angle = self.angle
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, angle, alpha)
        """
     # This will draw the ball on the screen
         
         
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.WHITE)
            
    def advance(self):
        # This will allow the ball to move.
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def bounce_horizontal(self):
        # This will move the ball across the x-axis
        self.velocity.dx = -self.velocity.dx
        if ((self.velocity.dx < 3)and (self.velocity.dx >= 0)):
            self.velocity.dx += 1
        elif ((self.velocity.dx > -3)and (self.velocity.dx < 0)):
            self.velocity.dx -= 1
        
    def bounce_vertical(self):
        # This will move the bal across the y-axis
        self.velocity.dy = -self.velocity.dy
        if (self.velocity.dy == 0):
            self.velocity.dy += 1
            
    def restart(self):
        # This is for when the ball goes off the screen. It will reset the balls characteristics. 
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.velocity.dx = random.randint(-3,5)
        self.velocity.dy = random.randint(-3,5)
        
    def rotate(self):
        """
        Sets the speed of rotaion
        """
        self.angle += 5
        
class Paddle():
    
    def __init__(self):
        # This will initialize the characteristics f the paddle.
        self.center = Point()
        self.center.x = (SCREEN_WIDTH - (PADDLE_WIDTH * 2 ))
        self.center.y = SCREEN_HEIGHT / 2
        self.center.z = SCREEN_HEIGHT / 2
        self.center.t = PADDLE_WIDTH * 2
        
    def draw(self):
        # This will draw the paddle on the screen
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.center.t, self.center.z, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        
    def move_up(self):
        # This is the function that will allow the paddle to move up the side of the screen, but not
        # go off the screen.
        if self.center.y < SCREEN_HEIGHT - (PADDLE_HEIGHT / 2):
            self.center.y += MOVE_AMOUNT
        if self.center.y == SCREEN_HEIGHT:
            self.center.y = PADDLE_HEIGHT / 2
        
    def move_up_two(self):
        
        if self.center.z < SCREEN_HEIGHT - (PADDLE_HEIGHT / 2):
            self.center.z += MOVE_AMOUNT
        if self.center.z == SCREEN_HEIGHT:
            self.center.z = PADDLE_HEIGHT / 2
            
    def move_down(self):
        # This is the function that will allow the paddle to move down the side of the screen, but not
        # go off the screen.
        if self.center.y > (PADDLE_HEIGHT / 2):
            self.center.y -= MOVE_AMOUNT
    
    def move_down_two(self):
            
        if self.center.z > (PADDLE_HEIGHT / 2):
            self.center.z -= MOVE_AMOUNT
            
            



class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        
        self.score_one = 0
        self.score_two = 0
        

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False
        self.holding_a = False
        self.holding_d = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """
        

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()
        

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Player 1: {}".format(self.score_one)
        start_x =  SCREEN_WIDTH / 6
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE)
        
        score_text2 = "Player 2: {}".format(self.score_two)
        start_2x = SCREEN_WIDTH * 2 / 3
        arcade.draw_text(score_text2, start_x=start_2x, start_y=start_y, font_size=12, color=arcade.color.WHITE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        # Move the ball forward one element in time
        self.ball.advance()
        self.ball.rotate()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()
        
        
        
    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS
        too_close_t = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_z = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
           
        
        if (abs(self.ball.center.x - self.paddle.center.t) < too_close_t and
                    abs(self.ball.center.y - self.paddle.center.z) < too_close_z and
                    self.ball.velocity.dx < 0):
            
            # we are too close and moving left, this is a hit!
            self.ball.bounce_horizontal()
            
        

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # Player two missed!
            self.score_one += 1
            self.ball.restart()
         
        if self.ball.center.x < 0:
            # Player one missed!
            self.score_two += 1
            self.ball.restart()
        
    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()
            

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()
        if self.holding_a:
            self.paddle.move_down_two()

        if self.holding_right:
            self.paddle.move_up()
        if self.holding_d:
            self.paddle.move_up_two()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True
        if key == arcade.key.A or key == arcade.key.S:
            self.holding_a = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True
        if key == arcade.key.D or key == arcade.key.W:
            self.holding_d = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False
        
        if key == arcade.key.A or key == arcade.key.S:
            self.holding_a = False
        

        if key == arcade.key.D or key == arcade.key.W:
            self.holding_d = False
            
        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
