import sys

import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Updated from Feature Branch")

# Set up font
font = pygame.font.SysFont(None, 48)
text = font.render("Hello", True, (255, 255, 255))

# Set up a red rectangle
rect_color = (255, 0, 0)
rect = pygame.Rect(100, 100, 200, 100)  # A rectangle at position (100, 100)

# Run the game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(text, (250, 200))  # Draw the "Hello" text at the center
    pygame.draw.rect(screen, rect_color, rect)  # Draw the red rectangle
    pygame.display.flip()  # Update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
