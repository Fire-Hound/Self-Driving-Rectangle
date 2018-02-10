import pygame


pygame.init()
HEIGHT, WIDTH = 700, 1100

done = False
is_blue = True
x = 30
y = 30
color = (0,66,99)
clock = pygame.time.Clock()


#Setting up the the screen with walls
walls = []
def wall(rect):
        walls.append(rect)
class Player:
        def __init__(self, x, y, wallw, wallh, screen):
                self.x = x
                self.y = y
                self.wallh = wallh
                self.wallw = wallw
                self.screen = screen
                self.rect = pygame.Rect(x*wallw,y*wallh,wallw-1, wallh-1)
                self.spawn = self.rect.copy()
                self.lines = [pygame.draw.line for _ in range(5)]
        def move(self, dx, dy):   
                self.rect = self.rect.move(dx, dy)
                self.draw()
        def collide(self):
                return self.rect.collidelist(walls)

                


        def draw(self):
                rect = self.rect
                self.player = pygame.draw.rect(screen, (255,0,0), self.rect)
                self.points = [rect.midleft, rect.topleft, rect.midtop, rect.topright, rect.midright,
                               rect.bottomright, rect.midbottom, rect.bottomleft]#This took a lot of time to think

                for point in self.points:
                        #Calculating the distance between between the center and the points
                        dx = point[0] - self.rect.center[0] 
                        dy = point[1] - self.rect.center[1]

                        pygame.draw.line(self.screen, (0,200,255),point,
                        ( point[0] + dx*2 , point[1] + dy*2))
                         #Adding the distance calculated before to extend the line
                        #multiplying by 2 to extend the line even more
                pygame.display.update()
                


            

WallBP = [
         "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
         "WWW....................WWWW",
         "WWW....................WWWW",
         "WWW....................WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW......WWWWWWWWW.....WWWW",
         "WWW..P...WWWWWWWWW.....WWWW",
         "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
         "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
         "WWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

HorizontalWalls = len(WallBP[0])
VerticalWalls = len(WallBP)
WallHeight = int(HEIGHT/VerticalWalls)
WallWidth = int(WIDTH/HorizontalWalls)
screen = pygame.display.set_mode((WallWidth*HorizontalWalls, WallHeight*VerticalWalls))
screen.fill((0, 0, 0))

player = None
def draw_world(first=False):
        global player
        for y in range(VerticalWalls):
                for x in range(HorizontalWalls):

                        if WallBP[y][x] == "W":
                                if first:
                                        wall(pygame.Rect(x*WallWidth, y*WallHeight,WallWidth-1, WallHeight-1)) #Add wall to the wall list by calling this func
                                pygame.draw.rect(screen, color, pygame.Rect(x*WallWidth, y*WallHeight,WallWidth-1, WallHeight-1))
                        if first and WallBP[y][x] == "P" :
                                player = Player(x,y, WallWidth, WallHeight, screen)
                                player.draw()
                                #player = pygame.draw.rect(screen, (99,99,66), pygame.Rect(y*WallWidth,x*WallHeight,WallWidth-1 , WallHeight-1))
                                #outer = pygame.Rect(y*WallWidth,x*WallHeight,WallWidth-1 , WallHeight-1)
                                #pygame.draw.circle(screen, (255,0,0),(int(y*WallWidth+WallWidth/2),
                                #                                        int(x*WallHeight+WallHeight/2)), 10)

draw_world(first=True)

while not done:
        screen.fill((0,0,0))
        draw_world()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
                player.move(-2, 0)
        if key[pygame.K_d]:
                player.move(2, 0)
        if key[pygame.K_w]:
                player.move(0, -2)
        if key[pygame.K_s]:
                player.move(0, 2)
        # pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]: y -= 3
        # if pressed[pygame.K_DOWN]: y += 3
        # if pressed[pygame.K_LEFT]: x -= 3
        # if pressed[pygame.K_RIGHT]: x += 3

        
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)


        #COLLISION DETECTION -- if player collides with wall spawn them back to original place
        if player.collide() != -1:
                player.rect = player.spawn
        player.draw()
        pygame.display.update()
        clock.tick(60)