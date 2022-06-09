from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.cast import Cast
from game.director import Director
from game.moving_object import MovingObject
from game.rock import Rock
from game.gem import Gem
from game.common.coordinate import Coordinate
from game.common.color import Color
import random

"""
This file will excute and start the game
"""
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 50


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = MovingObject()#Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Coordinate(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y-20)
    position = Coordinate(x, y)

    robot = MovingObject(can_move_y = False) #Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.randint(33, 126))
        #message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Coordinate(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # artifact = Rock()#Artifact()
        if (random.randint(1, 2) % 2) == 0:
            artifact = Rock()
        else:
            artifact = Gem()

        # artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        #artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()