import pygame

# Initializes game
pygame.init()

# Creates 800 x 800 display
display = pygame.display.set_mode((800,800))

# Title and icon setup
# Icon credit: <div>Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('battleship.png')
pygame.display.set_icon(icon)

# Fighter
fighter_image = pygame.image.load('gaming.png')
fighter_imageX = 400
fighter_imagey = 650

def player():
    display.blit(fighter_image, (fighter_imageX, fighter_imagey))
# Game Runner
game_running = True

while game_running:
    # Must be filled before the updates
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    player()
    pygame.display.update()