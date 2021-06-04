#Se importa la biblioteca que se utilizará para
import pygame, sys
pygame.init()
#se inicia la ventana

screen = pygame. display.set_mode([500,600])
pygame.display.set_caption("Moon light Redemption")
clock = pygame.time.Clock()


Font_tutulo = pygame.font.Font("8-BIT WONDER.TTF", 20)
Titulo = Font_tutulo.render("Moon light Redemption", 0, (255, 255, 255))
label_font = pygame.font.Font("8-BIT WONDER.TTF", 10)
label_user = label_font.render("Write your name", 0, (255, 255, 255))
def draw_text(txt, color, x, y, font = Font_tutulo):
    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

def menu():
    # se configura el bg dentro de la pantalla de juego

    bg = pygame.image.load("Imagenes/Background.jpg").convert()

    Textbox = pygame.Rect(270, 100, 125, 25)
    button_Easy = pygame.Rect(190,190,120,45)
    button_Medium = pygame.Rect(190,270,120,45)
    button_Hard = pygame.Rect(190,350,120,45)
    button_Instructions = pygame.Rect(260,500,120,45)
    button_Credits = pygame.Rect(120,500,120,45)
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
        if button_Easy.collidepoint((cursor_x , cursor_y)):
            if mouse_click:
                print("Level Easy")
        if button_Medium.collidepoint((cursor_x , cursor_y)):
            if mouse_click:
                print("Level Madium")
        if button_Hard.collidepoint((cursor_x , cursor_y)):
            if mouse_click:
                print("Level Hard")
        if button_Credits.collidepoint((cursor_x , cursor_y)):
            if mouse_click:
                print("Credits")
        if button_Instructions.collidepoint((cursor_x , cursor_y)):
            if mouse_click:
                print("Instructions")
        if Textbox.collidepoint((cursor_x , cursor_y)):
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
                    elif len(User) < 15:
                        User += event.unicode
        pygame.draw.rect(screen, (255, 0, 0), button_Easy)
        pygame.draw.rect(screen, (255, 0, 0), button_Medium)
        pygame.draw.rect(screen, (255, 0, 0), button_Hard)
        pygame.draw.rect(screen, (255, 0, 0), button_Instructions)
        pygame.draw.rect(screen, (255, 0, 0), button_Credits)
        if active:
            pygame.draw.rect(screen, (255, 255, 255), Textbox)
        else:
            pygame.draw.rect(screen, (255, 0, 0), Textbox)
        draw_text(User, (0, 0, 0), 450, 450)
        pygame.display.update()
        screen.blit(bg, [-20, -200])
        screen.blit(Titulo, (50, 50))
        screen.blit(label_user, (90,105))
        pygame.display.update()


menu()
