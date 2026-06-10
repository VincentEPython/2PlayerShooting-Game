import pygame

pygame.init()
#constants
FPS = 60
WIDTH = 1000
HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 3
MAX_BULLET = 3
DIVIDER = pygame.Rect(WIDTH // 2 -5, 0,10,HEIGHT)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#adding title to window
pygame.display.set_caption("Laser Royale")

#setting the font
hp_font = pygame.font.SysFont("courier",20)
win_lose_font = pygame.font.SysFont("Times New Roman",30)

#creating Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,img_path,controls,side):
        super().__init__()
        self.img = pygame.image.load(img_path)





def draw():
    screen.fill("navy blue")
    #displaying the Divider
    pygame.draw.rect(screen,"white",DIVIDER)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()

main()
