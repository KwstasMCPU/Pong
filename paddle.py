import pygame
BLACK = (0,0,0)
WHITE = (255, 255, 255)

class PaddleSprite(pygame.sprite.Sprite):
    """Initialising the paddles for the players"""
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # Fetch the rectangle object
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
		# Check if the paddles are off the edge of the screen (y-axis)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Check if the paddles are off the edge of the screen (y-axis)
        if self.rect.y > 500:
            self.rect.y = 500


