import sys

import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello from Main Branch")

# Set up font
font = pygame.font.SysFont(None, 48)
text = font.render("Hello", True, (255, 255, 255))

# Set up circle properties
circle_color = (0, 255, 0)  # Green circle
circle_radius = 50
circle_position = (460, 240)  # Center of the screen

# Run the game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(text, (250, 200))  # Draw the "Hello" text at the center
    pygame.draw.circle(
        screen, circle_color, circle_position, circle_radius
    )  # Draw the green circle
    pygame.display.flip()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
