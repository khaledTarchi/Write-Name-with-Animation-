import pygame
import random

# Initialize pygame and set the window size
pygame.init()
screen = pygame.display.set_mode((1100, 1900))

# Set the window title
pygame.display.set_caption("TR")

# Load a font to use for the text
font = pygame.font.Font("freesansbold.ttf", 80)

# Create a text surface with the name "KHALED TR"

text_surface = font.render("KHALED TR", True, (255, 255, 255))
text_rect = text_surface.get_rect()


# Set the starting position of the text
text_rect.center = (550, 950)

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a random color rectangle behind the text
    pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (0, 0, 1100, 1900))

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

    # Animate the text by changing its position
    text_rect.x += random.randint(-5, 5)
    text_rect.y += random.randint(-5, 5)

    # Limit the text's movement to the window
    if text_rect.left < 0 or text_rect.right > 1100:
        text_rect.x -= 2 * text_rect.x
    if text_rect.top < 0 or text_rect.bottom >1900:
        text_rect.y -= 2 * text_rect.y


    # Add some sparkles around the text
    for i in range(20):
        x = random.randint(text_rect.left - 50, text_rect.right + 50)
        y = random.randint(text_rect.top - 50, text_rect.bottom + 50)
        pygame.draw.circle(screen, (255, 255, 255), (x+10, y+10), 7)
        pygame.draw.circle(screen, (0, 0, 0), (x+10, y+10), 7)


    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
