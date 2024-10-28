import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame Window")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (80, 180, 80)
BUTTON_TEXT_COLOR = BLACK

# IMAGES
new_width = 50
new_height = 50
arrow_surf = pygame.image.load('images/arrow-down.png').convert_alpha()
arrow_scale = pygame.transform.scale(arrow_surf, (new_width, new_height))

# Position for arrow image
arrow_position = (400, 300)
arrow_rect = arrow_scale.get_rect(topleft=arrow_position)

button_rect = pygame.Rect(300, 500, 200, 50)  # (x, y, width, height)
font = pygame.font.Font(None, 36)
button_text = font.render("Click Me!", True, BUTTON_TEXT_COLOR)

clock = pygame.time.Clock()
FPS = 60  
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if arrow_rect.collidepoint(event.pos):  # Use arrow_rect for collision detection
                print("ARROW clicked!")

    screen.fill(WHITE)

    # Button hover effect
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    screen.blit(button_text, (button_rect.x + 50, button_rect.y + 10))

    # Draw the arrow image
    screen.blit(arrow_scale, arrow_position)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
