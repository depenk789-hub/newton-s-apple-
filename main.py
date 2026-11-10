#importing necessary libraries to the program
import pygame
pygame.init()
import random
#creating a 800 * 800 game window
screen = pygame.display.set_mode((800, 800))

#setting title of the game
pygame.display.set_caption("Newton's Apple")
clock = pygame.time.Clock()

#creating snake's initial appearance
SNAKE_HEAD = pygame.Rect(100, 100, 30, 30) # x_position, y_position, height and width resp as parameters

#creating apple's initial appearence
APPLE = pygame.Rect(300, 400, 10, 10) # x_position, y_position, height and width resp as parameters

#creating body segment to be added 
body_segment = pygame.Rect(70, 100, 30, 30) 

#initilisations
speed = 30
direction = (1, 0)
running = True
score = 0

move_interval = 160
last_move = pygame.time.get_ticks()

#initialising pygame font
score_font = pygame.font.Font(None, 32) 


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
    
    #updating sanke's position
    now = pygame.time.get_ticks()
    if now -last_move >= move_interval:
        body_segment.topleft = SNAKE_HEAD.topleft # moves the body segment along side the head
        SNAKE_HEAD.x += direction[0] * speed
        SNAKE_HEAD.y += direction[1] * speed
        last_move = now
        
    #detecting whether the snake has hit the walls
    if SNAKE_HEAD.left <= 0 or SNAKE_HEAD.right >= 800 or SNAKE_HEAD.top <= 0 or SNAKE_HEAD.bottom >= 800:
        print("The snake hits the wall. Game over!")
        running = False
    
    #rendering the score of the player
    score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
    
    #positioning the score_text in the screen
    screen.blit(score_text, (15, 15))
    
       
    #detecting collision between snake and apple, and changing apple's position once it is eaten by sanke
    if SNAKE_HEAD.colliderect(APPLE):
        score += 1
        print("Apple is eaten!")
        
        #apple does not appear beneath snake right after it is eaten
        while SNAKE_HEAD.colliderect(APPLE):
            APPLE.x = random.randint(10, 780) # random x position with minimum of 10 and maximum of 780 inclusive
            APPLE.y = random.randint(10, 780) # random y position with minimum of 10 and maximum of 780 inclusive   
    
    
    #background of the screen                
    screen.fill((230, 240, 220))
    
    #drawing snake using SNAKE_HEAD with color code 0, 0, 0
    pygame.draw.rect(screen, (0, 0, 0), SNAKE_HEAD)
    
    #drawing apple using APPLE with color code 255, 0 , 0
    pygame.draw.rect(screen, (255, 0 , 0), APPLE)
    
    #drawing body segment using body_segment with color code 255, 0 , 0
    pygame.draw.rect(screen, (30, 100 , 40), body_segment)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()