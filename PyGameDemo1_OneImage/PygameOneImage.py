# pygame demo 1 - draw one image

# 1 - Import packages
import pygame
from pygame.locals import *
import sys 

def validate_window_dimensions(width, height, contstrainedWidth, constrainedHeight):
    if width < contstrainedWidth or height < constrainedHeight:
        raise ValueError("The window dimensions do not accommodate the ball image dimensions")

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png') 

# 5 - Initialize variables
# 100x100 pixels
pxBallImageWidth = 100
pxBallImageHeight = 100

# Simple validation for window dimensions
validate_window_dimensions(WINDOW_WIDTH, WINDOW_HEIGHT, pxBallImageWidth, pxBallImageHeight)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" action

    # 9 - Clear the window
    window.fill(BLACK)

    # 10 - Draw all window elements
    # Draw ball at center of screen 
    window.blit(ballImage, ((WINDOW_WIDTH / 2) - (pxBallImageWidth / 2) , (WINDOW_HEIGHT / 2) - (pxBallImageHeight / 2)))

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND) 