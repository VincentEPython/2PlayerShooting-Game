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
        super().__init__() # super is a function that's calling the constructor function of the parent class (Sprite)
        self.image = pygame.image.load(img_path)
        #scaling the image
        self.image = pygame.transform.scale(self.image,(70,80))
        self.rect = self.image.get_rect(topleft=(x,y))# the top left corner of the hitbox rectangle that is around the image is being placed at the xy coordinates
        self.controls = controls
        self.side = side
        self.hp = 10
        self.bullets = pygame.sprite.Group()
    
    def move(self,keys):    
        if keys[self.controls["left"]]:
            self.rect.x -= PLAYER_SPEED
        if keys[self.controls["right"]]:
            self.rect.x += PLAYER_SPEED
        if keys[self.controls["up"]]:
            self.rect.y -= PLAYER_SPEED
        if keys[self.controls["down"]]: 
            self.rect.y += PLAYER_SPEED
        
        #top and bottom boundaries
        self.rect.top = max(0,self.rect.top)
        self.rect.bottom = min(HEIGHT,self.rect.bottom)
        #left and right boundaries
        if self.side == "left":
            self.rect.left = max(0,self.rect.left)
            self.rect.right = min(DIVIDER.left,self.rect.right)
        if self.side == "right":
            self.rect.left = max(DIVIDER.right,self.rect.left)
            self.rect.right = min(WIDTH,self.rect.right)
    
#creating Playerobject
playerL = Player(
    100,250,
    "images\homelander_idle.png",
    {
        "left" : pygame.K_a,
        "right" : pygame.K_d,
        "up" : pygame.K_w,
        "down" : pygame.K_s
    },
    "left" 
)
playerR = Player(
    900,250,
    "images\souljaboy.jpg",
    {
        "left" : pygame.K_LEFT,
        "right" : pygame.K_RIGHT,
        "up" : pygame.K_UP,
        "down" : pygame.K_DOWN
    },
    "right"
)
#creating player group
players = pygame.sprite.Group()
#adding players to the group
players.add(playerL)
players.add(playerR)

def draw():
    screen.fill("navy blue")
    #displaying the Divider
    pygame.draw.rect(screen,"white",DIVIDER)

    # displaying players sprite
    players.draw(screen)

    #combining player hp with the hp_font
    left_hp_text = hp_font.render(f"Health: {playerL.hp}",True,(200,150,115))
    right_hp_text = hp_font.render(f"Health: {playerR.hp}",True,(200,150,115))

    #displaying the hp text
    screen.blit(left_hp_text,(20,40))
    screen.blit(right_hp_text,(850,40))
    # constantly updating the screen
    pygame.display.update()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit(0)

        #getting the keyboardkeys pressed
        keys = pygame.key.get_pressed()
        playerL.move(keys)
        playerR.move(keys)
        draw()


main()
