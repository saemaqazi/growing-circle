import pygame
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Basic Shapes")

# Set up colors (R, G, B format)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Main loop
running = True
while running:
    # Fill the background with white
    screen.fill(WHITE)

    # Draw a red circle (center at 300, 200 with radius 50)
    pygame.draw.circle(screen, RED, (300, 200), 50)

    # Draw a blue rectangle (top-left at 100, 100, width 120, height 80)
    pygame.draw.rect(screen, BLUE, pygame.Rect(100, 100, 120, 80))

    # Draw a green line (start at 50, 50, end at 550, 350, width 5)
    pygame.draw.line(screen, GREEN, (50, 50), (550, 350), 5)

    # Update the display
    pygame.display.flip()

    # Event loop to exit the program
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

# Quit Pygame
pygame.quit()
