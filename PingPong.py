from logging import disable
import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PingPong"

class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball=Ball("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/pingpong/ball.png",0.7)
        self.racket=Racket("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/pingpong/bar.png",0.7)
        self.score=0
        self.tries=1000


    def setup(self):
        self.ball.center_x=300
        self.ball.center_y=300
        self.ball.change_x=5
        self.ball.change_y=5

        self.racket.center_x=300
        self.racket.center_y=150
        self.racket.change_x=0
        self.racket.change_y=0

    def on_key_press(self,key,modifiers):
        if key == arcade.key.RIGHT:
            self.racket.change_x=5
    #NEW:
        if key == arcade.key.LEFT:
            self.racket.change_x = -5

    # rendering
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        self.ball.draw()
        self.racket.draw()
        text_score=f"Score: {self.score}"
        arcade.draw_text(text_score,10,570,arcade.color.BLACK,20,font_name='comic')
        text_tries=f"Tries: {self.tries}"
        arcade.draw_text(text_tries,10,550,arcade.color.BLACK,20)

    # logic
    def update(self, delta_time):
        self.ball.update()
        self.racket.update()
        if self.ball.bottom < 0:
            self.tries -=1
        if self.tries <= 0:
            self.ball.stop()
            self.racket.stop()
            self.tries=0
    # NEW:
        if arcade.check_for_collision(self.ball,self.racket):
            self.ball.bottom=self.racket.top
            self.ball.change_y=-self.ball.change_y
            self.score+=1
            print(self.score)

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x=-self.change_x
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y=-self.change_y

class Racket(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 0 :
            self.left=0
        if self.right > SCREEN_WIDTH:
            self.right=SCREEN_WIDTH
         



game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
