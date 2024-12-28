import pygame
from pygame.locals import QUIT
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Rectangles")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle class
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dy):
        self.y += dy

# Create multiple rectangles
rectangles = [Rectangle(random.randint(0, WIDTH - 50), 0, 50, 30, BLUE) for _ in range(5)]

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw and move rectangles
    for rect in rectangles:
        rect.draw(screen)
        rect.move(1)
        if rect.y > HEIGHT:  # Reset rectangle to top
            rect.y = 0
            rect.x = random.randint(0, WIDTH - 50)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update display
    pygame.display.flip()

pygame.quit()
