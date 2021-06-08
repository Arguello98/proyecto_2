#Se importa la biblioteca que se utilizará para
import pygame, sys, random
pygame.init()
#se inicia la ventana

screen = pygame. display.set_mode([900,700])
pygame.display.set_caption("Moon light Redemption")
clock = pygame.time.Clock()

# se configura el bg dentro de la pantalla de juego

#bg = pygame.image.load("Imagenes/Background.jpg").convert()
lives = 3

Niveles = 0

BgMenu = pygame.image.load("Imagenes/BgMenu.png").convert()
BgL1 = pygame.image.load("Imagenes/BgLevel1.png").convert()
Bgl2 = pygame.image.load("Imagenes/BgLevel2.jpg").convert()
BgL3 = pygame.image.load("Imagenes/Bglevel3.jpg").convert()
Button_grande = pygame.image.load("Imagenes/button(2).png")
Button_pequeno = pygame.image.load("Imagenes/button.png")

Backgrounds = [BgMenu, BgL1, Bgl2, BgL3]

Font_tutulo = pygame.font.Font("8-BIT WONDER.TTF", 40)
Fuente_complementaria = pygame.font.Font("LVDCGO__.TTF", 15)
Titulo = Font_tutulo.render("Moon light Redemption",0, (255, 255, 255))
label_font = pygame.font.Font("8-BIT WONDER.TTF", 20)
label_user = label_font.render("Write your name", 0, (255, 255, 255))
Font_botones = pygame.font.Font("8-BIT WONDER.TTF", 15)

def draw_text(txt, color, x, y, font = Font_tutulo):

    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

def draw_complementos(txt, color, x, y, font = label_font):
    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

def draw_botones(txt, color, x, y, font = Font_botones):
    text_obj = font.render(txt, 1, color)
    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

def menu():

    global Niveles, lives
    lives = 3
    

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

    #--------ciclo logico----------------------------------#

    while True:
        Niveles = 0
        clock.tick(60)
        cursor_x , cursor_y =  pygame.mouse.get_pos()

        #-----------clicks----------------------------#

        if mouse_click:
            active = False
        if mouse_click:
            active = False
        if button_Easy.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Easy")
                Niveles =  1
                level(Niveles)
        if button_Medium.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Madium")
                Niveles = 2
                level(Niveles)
        if button_Hard.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Level Hard")
                Niveles = 3
                level(Niveles)
        if button_Credits.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Credits")
                Creditos()
        if button_Instructions.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Instructions")
                Instructions()
        if Textbox.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                active = True
        mouse_click = False

        #----------eventos--------------------------------#

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


        screen.blit(Backgrounds[Niveles], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Moon light Redemption",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        draw_complementos("Write Your name ", (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 300,160)

        #pygame.draw.rect(screen,(255,0,0), button_play)
        screen.blit(Button_grande,[450-300//2,450])
        #pygame.draw.rect(screen, (255, 0, 0), button_Easy)
        screen.blit(Button_pequeno, (450-150//2-150-75,300))
        #pygame.draw.rect(screen, (255, 0, 0), button_Medium)
        screen.blit(Button_pequeno, (450-150//2,300))
        #pygame.draw.rect(screen, (255, 0, 0), button_Hard)
        screen.blit(Button_pequeno, (600,300))
        #pygame.draw.rect(screen, (255, 0, 0), button_Instructions)
        screen.blit(Button_grande, [450-300-10, 600])
        #pygame.draw.rect(screen, (255, 0, 0), button_Credits)
        screen.blit(Button_grande, (450 + 10, 600))
        if active:
            pygame.draw.rect(screen, (255, 255, 255), Textbox)
        else:
            pygame.draw.rect(screen, (255, 0, 0), Textbox)

            #Texto escrito por el usuario
        draw_text(User, (0,0,0), 600,160 , label_font)

        # -------------------Texto de los botones------------------------#
        draw_complementos("Play", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 900 // 2,462)
        draw_complementos("Instructions", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 290, 615)
        draw_complementos("Cedrits", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),610, 615)
        draw_botones("Easy",  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 225, 315)
        draw_botones("Medium", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 450, 315)
        draw_botones("Hard", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 675, 315)

        pygame.display.update()


def Creditos():

    ButtonExit = pygame.Rect(450 - 130 // 2, 5, 130, 40)
    mouse_click = False
    while True:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()


        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Exit")
                menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Credits",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        screen.blit(Button_pequeno, (450 - 130 // 2, 2))
        pygame.display.update()


def Instructions():

    ButtonExit = pygame.Rect(450 - 130 // 2, 5, 130, 40)
    mouse_click = False

    while True:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()


        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Exit")
                menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Instructions",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        screen.blit(Button_pequeno, (450 - 130 // 2, 2))
        pygame.display.update()




def level(nivel):
    global lives

    cubos = []
    for i in range(5*nivel):
        temporal = pygame.Rect(random.randint(10, 800),random.randint(100,500),40,40)
        if random.randint(-5,5) > 0:
            direccion_x = -1
        else:
            direccion_x = 1
        if random.randint(-5,5)>0:
            direccion_y = -1
        else:
            direccion_y = 1
        vel_temporal_1 = random.randint(1,3*4) * direccion_x
        vel_temporal_2 = random.randint(1,3*4) * direccion_y
        cubos +=[[temporal,vel_temporal_1,vel_temporal_2]]
    
    def movimiento_cubos(lista):
        for i in lista:
            if i[0].x <= 0:
                i[1] = random.randint(1,5)
            if i[0].x +i[1] +50 >=900:
                i[1] = random.randint(1,5) * -1
            if i[0].y <= 50:
                i[2]= random.randint(1,5)
            if i[0].y+ i[2]+ 50>=640:
                i[2]= random.randint(1,5)*-1
            else:
                i[0].x += i[1]
                i[0].y += i[2]
    
    def player_move(keys_pressed):
        VEL = 5
        if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0: #left
            player.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and player.x +VEL + 50 < 900:#right
            player.x += VEL
        if keys_pressed[pygame.K_DOWN] and player.y + VEL + 50 < 640:#right
            player.y += VEL
        if keys_pressed[pygame.K_UP] and player.y - VEL > 50:#right
            player.y -= VEL

    def collision_check(lista,invincibility):
        global lives
        for i in lista:
            if player.colliderect(i[0]) and not invincibility:
                cubos.remove(i)
                lives -= 1
                print(lives)

    player = pygame.Rect(450,450,50,50)
    clock = pygame.time.Clock()

    #------------Barra superior----------------#
    BarraSuperior = pygame.Rect(0,0, 900, 50)
    ButtonExit = pygame.Rect(450-130//2,5,130,40)

    #-------------Barra de progreso-----------#
    BarraProgreso = pygame.Rect(0,700-60, 900, 60)
    #----------------texto-------------#
    
    LabelScore = Fuente_complementaria.render("SCORE:", 0, (0, 0, 0))
    LabelTime = Fuente_complementaria.render("TIME:", 0, (0, 0, 0))
    LabelLives = Fuente_complementaria.render("LIVES:", 0, (0, 0, 0))

    levels = False
    mouse_click = False
    invincibility = True
    timer = 0
    timer_2 = 0
    time = 60


    while not levels:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()

        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Exit")
                levels = True
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        if timer >= 90:
            timer = 90
            invincibility = False
        timer +=1

        if timer_2 > 60:
            timer_2 = 0
            time -= 1
        timer_2 += 1

        if lives == 0:
            level_1 = True
        #------------------------move-----------------------#
        keys_pressed = pygame.key.get_pressed()
        player_move(keys_pressed)
        movimiento_cubos(cubos)
        collision_check(cubos, invincibility)

        screen.blit(Backgrounds[Niveles], [0, 0])
        #----------draw------------#
        for i in cubos:
            pygame.draw.rect(screen,(255,255,255),i[0])
        pygame.draw.rect(screen,(255,0,0),player)

        #----------draw------------#   
       # pygame.draw.rect(screen, (255, 255, 255), BarraSuperior)
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (450-130//2,2))
        #pygame.draw.rect(screen, (255, 255, 255), BarraProgreso)


        draw_text(str(time),(0,0,0),450 + 40,665,Fuente_complementaria)
        
        screen.blit(LabelScore, (450 - 150 // 2 - 150 - 75, 665))
        screen.blit(LabelTime, (450 - 150 // 2, 665))
        screen.blit(LabelLives, (600, 665))

        pygame.display.update()


menu()

