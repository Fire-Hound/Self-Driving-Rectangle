import pygame

pygame.init()
display = pygame.display.set_mode((500,500))
display.fill((0,0,0))
finished = False
rect = pygame.Rect(200,100,50,50)
pygame.draw.rect(display, (255,0,0), rect)

print(rect.topleft)

points = [rect.midleft, rect.topleft, rect.midtop, rect.topright, rect.midright]

for point in points:
    #Calculating the distance between between the center and the points
    dx = point[0] - rect.center[0] 
    dy = point[1] - rect.center[1]

    pygame.draw.line(display, (0,200,255),point,
    ( point[0] + dx*2 , point[1] + dy*2)) #Adding the distance calculated before to extend the line
# x = pygame.draw.line(display, (0,200,255),rect.center,rect.topleft)
# pygame.draw.line(display, (0,200,255),rect.center,rect.topright)
# pygame.draw.line(display, (0,200,255),rect.center,rect.midtop)
# pygame.draw.line(display, (0,200,255),rect.center,rect.midleft)
# pygame.draw.line(display, (0,200,255),rect.center,rect.midright)
#133fym15 
#15 
#print(x)
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pygame.display.update()

    
