#Se importa la biblioteca que se utilizará para
import pygame, sys
pygame.init()
#se inicia la ventana

screen = pygame. display.set_mode([900,700])
pygame.display.set_caption("Moon light Redemption")
clock = pygame.time.Clock()

# se configura el bg dentro de la pantalla de juego

#bg = pygame.image.load("Imagenes/Background.jpg").convert()

Font_tutulo = pygame.font.Font("8-BIT WONDER.TTF", 40)
Titulo = Font_tutulo.render("Moon light Redemption", 0, (255, 255, 255))
label_font = pygame.font.Font("8-BIT WONDER.TTF", 20)
label_user = label_font.render("Write your name", 0, (255, 255, 255))

def draw_text(txt, color, x, y, font = Font_tutulo):
    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

def menu():


    Textbox = pygame.Rect(450+10,150, 300, 50)
    button_play = pygame.Rect(450-300//2,450,300,50)
    button_Easy = pygame.Rect(450-150//2-150-75,300,150,50)
    button_Medium = pygame.Rect(450-150//2,300,150,50)
    button_Hard = pygame.Rect(600,300,150,50)
    button_Instructions = pygame.Rect(450-300-10,600,300,50)
    button_Credits = pygame.Rect(450+10,600,300,50)
    clock = pygame.time.Clock()

    mouse_click = False
    User = " "
    active = False

    #--------ciclo logico--------

    while True:

        clock.tick(60)
        cursor_x , cursor_y =  pygame.mouse.get_pos()

        #-----------clicks---------

        if mouse_click:
            active = False
        if mouse_click:
            active = False
        if button_Easy.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Easy")
                level()
        if button_Medium.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Madium")
                level()
        if button_Hard.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Hard")
                level()
        if button_Credits.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Credits")
        if button_Instructions.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Instructions")
        if Textbox.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                active = True
        mouse_click = False

        #----------eventos------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        User = User[:-1]
                    elif len(User) < 10:
                        User += event.unicode

        #-----------------drwaw--------------------------#

       # screen.blit(bg, [-20, -200])
        screen.fill((0,0,0))
        screen.blit(Titulo, (50, 50))
        screen.blit(label_user, (450-150//2-150-75,160))

        pygame.draw.rect(screen,(255,0,0), button_play)
        pygame.draw.rect(screen, (255, 0, 0), button_Easy)
        pygame.draw.rect(screen, (255, 0, 0), button_Medium)
        pygame.draw.rect(screen, (255, 0, 0), button_Hard)
        pygame.draw.rect(screen, (255, 0, 0), button_Instructions)
        pygame.draw.rect(screen, (255, 0, 0), button_Credits)
        if active:
            pygame.draw.rect(screen, (255, 255, 255), Textbox)
        else:
            pygame.draw.rect(screen, (255, 0, 0), Textbox)

            #Texto escrito por el usuario
        draw_text(User, (0,0,0), 600,160 , label_font)
        pygame.display.update()



def level():


    #------------Barra superior----------------#
    BarraSuperior = pygame.Rect(0,0, 900, 50)
    ButtonExit = pygame.Rect(450-130//2,5,130,40)

    #-------------Barra de progreso-----------#
    BarraProgreso = pygame.Rect(0,700-60, 900, 60)
    #----------------texto-------------#
    Fuente_complementaria = pygame.font.Font("LVDCGO__.TTF", 15)
    LabelScore = Fuente_complementaria.render("SCORE:", 0, (0, 0, 0))
    LabelTime = Fuente_complementaria.render("TIME:", 0, (0, 0, 0))
    LabelLives = Fuente_complementaria.render("LIVES:", 0, (0, 0, 0))

    level_1 = False
    mouse_click = False

    while not level_1:
        cursor_x, cursor_y = pygame.mouse.get_pos()

        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Exit")
                menu()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True


       # screen.blit(bg, [-20, -200])

        screen.fill((0,0,0))

        #----------draw------------#

        pygame.draw.rect(screen, (255, 255, 255), BarraSuperior)
        pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        pygame.draw.rect(screen, (255, 255, 255), BarraProgreso)
        screen.blit(LabelScore, (450 - 150 // 2 - 150 - 75, 665))
        screen.blit(LabelTime, (450 - 150 // 2, 665))
        screen.blit(LabelLives, (600, 665))

        pygame.display.update()


menu()
level()
