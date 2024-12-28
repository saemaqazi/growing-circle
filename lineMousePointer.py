import pygame
#from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Following Mouse")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Line class
class Line:
    def __init__(self, start_pos, end_pos, color, width):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color
        self.width = width

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.width)

# Create a Line object
line = Line((300, 200), (300, 200), GREEN, 5)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Update line's end position to the mouse position
    line.end_pos = pygame.mouse.get_pos()

    # Draw the line
    line.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

pygame.quit()
