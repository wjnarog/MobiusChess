import pygame

def draw_chessboards():
    # initialize Pygame
    pygame.init()

    # set the screen size
    screen_size = (1320, 660)

    # create the Pygame window
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    #screen.fill(255,255,255)
    print("hello")

    # set the caption of the window
    pygame.display.set_caption('Enigma Chess')

    # define the colors
    white = (200, 195, 170)
    black = (110, 105, 100)

    pygame.draw.rect(screen, (75,100,75), [0, 0, 1320, 660])
    pygame.draw.rect(screen, (75,100,75), [0, 0, 1320, 2])
    # set the size of each square on the chessboard
    square_size = 60

    # create the first chessboard
    for row in range(11):
        for col in range(9):
            x = col * square_size
            y = row * square_size
            if (row + col) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, [x, y, square_size, square_size])

    # create the second chessboard with a bigger gap
    gap_size = 120 # set the gap size to 100 pixels
     # fill
    for row in range(11):
        for col in range(9):
            x = col * square_size + 11 * square_size + gap_size # add the gap size to the x-coordinate
            y = row * square_size
            if (row + col) % 2 == 0:
                color = black
            else:
                color = white
            pygame.draw.rect(screen, color, [x, y, square_size, square_size])

    new_ing = pygame.image.load('PlayNow.png').convert_alpha()
    pygame.draw.rect(screen, (50,50,50), [0, 0, 1320, 5])
    pygame.draw.rect(screen, (50,50,50), [0, 655, 1320, 5])
    pygame.draw.rect(screen, (50,50,50), [0, 0, 5, 660])
    pygame.draw.rect(screen, (50,50,50), [1315, 0, 5, 660])

    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
    
        def draw(self):
            pos = pygame.mouse.get_pos()
            screen.blit(self.image, (self.rect.x, self.rect.y))

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    print("click")

    startB = Button(550, 240, new_ing, .4)

    # wait for the user to close the window
    run = True
    while run:
        startB.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()

    # quit Pygame
    pygame.quit()

# Call the function to draw the two chessboards side by side with a bigger gap between them
draw_chessboards()
