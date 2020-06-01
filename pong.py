import pygame
from paddle import PaddleSprite
from ball import Ball
import os
import time

def main():
    os.chdir(os.path.dirname(__file__))
    """ Set up the game and run the main game loop """
    pygame.init() # Prepare the pygame module for use

    # setting up the screen
    size = (800 , 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong')

    # setting colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # setting sound
    pygame.mixer.music.load('zapsplat_pong_bounce.mp3') # sound from https://www.zapsplat.com/
    

    # setting spirtes
    
    paddleA = PaddleSprite(WHITE, 10, 100)
    paddleA.rect.x = 0
    paddleA.rect.y = 250
 
    paddleB = PaddleSprite(WHITE, 10, 100)
    paddleB.rect.x = 790
    paddleB.rect.y = 250

    ball = Ball(WHITE,10,10)
    ball.rect.x = 400
    ball.rect.y = 300

    # list of all sprites
    all_sprites_list = pygame.sprite.Group()

    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

    # setting the clock
    clock = pygame.time.Clock()

    #Initialise player scores
    scoreA = 0
    scoreB = 0

    # main program loop
    RUNNING = True
    while RUNNING:

        # polls for events 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                RUNNING = False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: 
                    RUNNING = False
                
        # Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)    

        # Game logic
        all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=790:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>590:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1] 

        # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            pygame.mixer.music.play()
            ball.bounce()
            
        # Drawing
        # screen to black
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (398, 0), (398,600), 4)
        # sprites
        all_sprites_list.draw(screen)
        
        # Display scores:
        font = pygame.font.Font("AtariSmall.ttf", 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (200,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (600,10))

        # update the screen 
        pygame.display.flip()
     
        # Limit to 60 frames per second
        clock.tick(60)
 
    # end of main loop
    pygame.quit()

main()

