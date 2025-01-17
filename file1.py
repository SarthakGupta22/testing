import sys

import pygame

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Triangle from New Feature Branch")

# Set up font
font = pygame.font.SysFont(None, 48)
text = font.render("Hello", True, (255, 255, 255))

# Triangle properties
triangle_color = (255, 0, 0)  # Red triangle
triangle_width = 60
triangle_height = 50
triangle_x = 0  # Starting position of the triangle
triangle_y = 200

# Set the movement speed of the triangle
triangle_speed = 5

# Run the game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(text, (250, 100))  # Draw the "Hello" text at the top
    # Draw the triangle (we use a polygon to make the triangle)
    points = [
        (triangle_x, triangle_y),
        (triangle_x + triangle_width, triangle_y),
        (triangle_x + triangle_width / 2, triangle_y - triangle_height),
    ]
    pygame.draw.polygon(screen, triangle_color, points)  # Draw the red triangle
    pygame.display.flip()  # Update the display

    # Move the triangle horizontally
    triangle_x += triangle_speed
    if triangle_x > 640:  # If the triangle goes off-screen, reset its position
        triangle_x = -triangle_width

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
