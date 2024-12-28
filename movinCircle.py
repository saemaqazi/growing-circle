import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN=(0,255,0)
BLUE=(0,0,255) 
BLACK=(0,0,0)

# Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Create a Circle object
circle = Circle(300, 200, 50, RED)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the circle
    circle.draw(screen)

    # Event handling
     
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                circle.move(0, -10)
            elif event.key == K_DOWN:
                circle.move(0, 10)
            elif event.key == K_LEFT:
                circle.move(-10, 0)
            elif event.key == K_RIGHT:
                circle.move(10, 0)

    # Update display
    pygame.display.flip()

pygame.quit()
