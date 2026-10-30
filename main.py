import pygame
pygame.init()
#screen = pygame.display.setmode((800, 800))
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Newton's Apple")
clock = pygame.time.Clock()

# creating snake's initial appearance

SNAKE_HEAD = pygame.Rect(100, 100, 30, 30) # x_position, y_position, height and width resp as parameters

# creating apple's initial appearence

APPLE = pygame.Rect(300, 400, 10, 10) # x_position, y_position, height and width resp as parameters

speed = 2.5
direction = (1, 0)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            else:
                direction = (0, 1)    
    screen.fill((230, 240, 220))
    SNAKE_HEAD.x += direction[0] * speed
    SNAKE_HEAD.y += direction[1] * speed
    
     # detecting whether the snake has hit the walls
    
    if SNAKE_HEAD.left <= 0 or SNAKE_HEAD.right >= 800 or SNAKE_HEAD.top <= 0 or SNAKE_HEAD.bottom >= 800:
        print("The snake hits the wall. Game over!")
        running = False
        
    # drawing snake using SNAKE_HEAD with color code 0, 0, 0
    pygame.draw.rect(screen, (0, 0, 0), SNAKE_HEAD)
    
    #drawing apple using APPLE with color code 255, 0 , 0
    pygame.draw.rect(screen, (255, 0 , 0), APPLE)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()