#Se importa la biblioteca que se utilizará para
import pygame, sys, random, os
pygame.init()
pygame.mixer.init()
#se inicia la ventana

screen = pygame. display.set_mode([900,700])
pygame.display.set_caption("Moon light Redemption")
clock = pygame.time.Clock()

# se configura el bg dentro de la pantalla de juego
lista_musica = ["01.mp3","02.mp3","03.mp3"]

#bg = pygame.image.load("Imagenes/Background.jpg").convert()
lives = 3
score = 0
pause = False
Niveles = 0

#-------------------------------------------imgaes----------------------------------#
Asteroid = pygame.transform.scale(
    pygame.image.load(
        os.path.join("Imagenes/Asteroide.png")
),(40,40)
)

SpaceShip = pygame.transform.scale(
    pygame.image.load(
        os.path.join("Imagenes/SpaceShip.png")
    ),(50,50)
)
hearth_position = [715, 775,835]
BgMenu = pygame.image.load("Imagenes/BgMenu.png").convert()
BgL1 = pygame.image.load("Imagenes/Bglevel1.png").convert()
Bgl2 = pygame.image.load("Imagenes/BgLevel2.jpg").convert()
BgL3 = pygame.image.load("Imagenes/Bglevel3.jpg").convert()
Button_grande = pygame.image.load("Imagenes/button(2).png")
Button_pequeno = pygame.image.load("Imagenes/button.png")
Icono_vida  = pygame.image.load("Imagenes/Icono_vida.png")
Icono_sonido = pygame.image.load("Imagenes/Icono_Sonido.png")
Backgrounds = [BgMenu, BgL1, Bgl2, BgL3]

#---------------------------music-----------------------------#
pygame.mixer.music.load("Sneaky Driver.mp3")
pygame.mixer.music.play(-1,0,0)

HIT_SOUND = pygame.mixer.Sound("Grenade+1.mp3")

#--------------------------------------------------------------#
Font_tutulo = pygame.font.Font("8-BIT WONDER.TTF", 40)
Fuente_complementaria = pygame.font.Font("LVDCGO__.TTF", 15)
Titulo = Font_tutulo.render("Moon light Redemption",0, (255, 255, 255))
label_font = pygame.font.Font("8-BIT WONDER.TTF", 20)
label_user = label_font.render("Write your name", 0, (255, 255, 255))
Font_botones = pygame.font.Font("8-BIT WONDER.TTF", 15)
Font_final_screens = pygame.font.Font("8-BIT WONDER.TTF", 55)

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

def draw_Final_screens (txt, color, x, y, font = Font_final_screens):
    text_obj = font.render(txt, 1, color)
    text_obj = font.render(txt, 1, color)
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))

#-------------------------------------text reading----------------------------------#
def creating_leaderboard_2(lista):
    resultado = []
    for i in lista:
        name= ""
        score = ""
        separation = False
        for j in i:
            if j == ",":
                separation = True
            elif separation:
                score += j
            elif not separation:
                name += j
        resultado += [[int(score[:-1]),name]]
    print (resultado)


f = open("leaderboard.txt","rt")
temporal_list = f.readlines() #creates a list of the different places
creating_leaderboard_2(temporal_list)
f.close()
#------------


def menu():

    global Niveles, lives, score, pause

    Textbox = pygame.Rect(450+10,150, 300, 50)
    button_play = pygame.Rect(450-300//2,375,300,50)
    Button_Score = pygame.Rect(450-300//2,450,300,50)
    button_Easy = pygame.Rect(450-150//2-150-75,300,150,50)
    button_Medium = pygame.Rect(450-150//2,300,150,50)
    button_Hard = pygame.Rect(600,300,150,50)
    button_Instructions = pygame.Rect(450-300-10,600,300,50)
    button_Credits = pygame.Rect(450+10,600,300,50)
    clock = pygame.time.Clock()
    Sound = pygame.Rect(15, 10, 30, 23)

    mouse_click = False
    User = " "
    active = False
    Niveles = 1

    #--------ciclo logico----------------------------------#

    while True:
        lives = 3
        score = 0
        clock.tick(60)
        cursor_x , cursor_y =  pygame.mouse.get_pos()

        #-----------clicks----------------------------#

        if mouse_click:
            active = False
        if mouse_click:
            active = False
        if button_play.collidepoint((cursor_x, cursor_y)):
            if mouse_click and User != " ":
                print("Historia :v")
                level(Niveles)
        if button_Easy.collidepoint((cursor_x, cursor_y)):
            if mouse_click and User != " ":
                print("Level Easy")
                Niveles = 1
                #level(Niveles)
        if button_Medium.collidepoint((cursor_x, cursor_y)):
            if mouse_click and User != " ":
                print("Level Madium")
                Niveles = 2
                #level(Niveles)
        if button_Hard.collidepoint((cursor_x, cursor_y)):
            if mouse_click and User != " ":
                print("Level Hard")
                Niveles = 3
                #level(Niveles)
        if button_Credits.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Credits")
                Creditos()
        if button_Instructions.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Instructions")
                Instructions()
        if Button_Score.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Best Scores")
                Best_Score_Screen()
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

            if Sound.collidepoint((cursor_x, cursor_y)):
                if mouse_click:
                    print(pause)
                    if not pause:
                        pygame.mixer.music.pause()
                        pause = True
                    else:
                        pygame.mixer.music.unpause()
                        pause = False

        #-----------------drwaw--------------------------#


        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Moon light Redemption",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        draw_complementos("Write Your name ", (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 300,160)


        #pygame.draw.rect(screen,(255,0,0), button_play)
        screen.blit(Button_grande,[450-300//2,375])
        #pygame.draw.rect(screen, (255, 0, 0), Button_Score)
        screen.blit(Button_grande, [450 - 300 // 2, 450])
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
        Linea_txt = pygame.draw.line(screen, (255,255,255), (460,190), (760,190), 4)


            #Texto escrito por el usuario
        draw_text(User, (255,255,255), 600,160 , label_font)

        # pygame.draw.rect(screen,(255,255,255), Sound)
        screen.blit(Icono_sonido, (15, 10))

        # -------------------Texto de los botones------------------------#
        draw_complementos("Play", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 900 // 2,387)
        draw_complementos("Best Score", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 900 // 2,463)
        draw_complementos("Instructions", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 290, 615)
        draw_complementos("Credits", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),610, 615)
        if Niveles == 1:
            draw_botones("Easy",  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 225, 315)
            draw_botones("Medium", (0,0,0), 450, 315)
            draw_botones("Hard", (0,0,0), 675, 315)
        if Niveles == 2:
            draw_botones("Easy",   (0,0,0), 225, 315)
            draw_botones("Medium", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 450, 315)
            draw_botones("Hard", (0,0,0), 675, 315)
        if Niveles == 3:
            draw_botones("Easy",  (0,0,0), 225, 315)
            draw_botones("Medium", (0,0,0), 450, 315)
            draw_botones("Hard", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 675, 315)

        pygame.display.update()


def Creditos():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40)
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
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (375, 640))
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)
        #---------------------------Creditos---------------------------------#
        draw_complementos("Costa Rica",(255,255,255),450,150)
        draw_complementos("Instituto tecnologico de Costa Rica",(255,255,255), 450,200)
        draw_complementos("Ingenieria en Computadores",(255,255,255),450, 250)
        draw_complementos("Profesor Luis Barboza Artavia",(255,255,255), 450,300)
        draw_complementos("Taller de programacion" ,(255,255,255),450,350)
        draw_complementos("Daniel Arguello Poma e Isac Marin Sirias",(255,255,255),450,400)
        draw_complementos("Version X", (255,255,255),450,450)
        draw_complementos("2021", (0,0,0),450 + 200,550)
        draw_complementos("Grupo 4", (0,0,0),450//2,550)
        pygame.display.update()

def Instructions():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40)
    mouse_click = False

    while True:
        clock.tick(60)
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

        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Instructions",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (375, 640))
        draw_complementos("Welcome to Moon Light Redemption", (255, 255, 255), 450, 200)
        draw_complementos("It passes through the two most important cities", (255, 255, 255), 450, 250)
        draw_complementos("cities protected by a meteor shower", (255, 255, 255), 450, 300)
        draw_complementos("Be careful", (255, 255, 255), 450, 350)
        draw_complementos("To use your ship use the movement keys", (255, 255, 255), 450, 400)
        draw_complementos("Get to the moon and become the winner", (255, 255, 255), 450, 450)
        draw_complementos("", (255, 255, 255), 450, 450)
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)

        pygame.display.update()

def Victory_screen():
    Button_play_again = pygame.Rect(450 - 300 // 2, 550, 300, 50)
    mouse_click = False
    run = True
    while run:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()

        # ---------Jugar de nuevo--------#
        if Button_play_again.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                run = False
            mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True


        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_Final_screens("Victory for you",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,300)
        #pygame.draw.rect(screen, (255, 0, 0), Button_play_again)
        screen.blit(Button_grande, (300, 550))
        draw_complementos("Play Again", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 455, 565)

        pygame.display.update()

def End_Screen():
    Button_play_again = pygame.Rect(450 - 300 // 2, 550, 300, 50)
    mouse_click = False

    run = True

    while run:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()

        # ---------Jugar de nuevo--------#
        if Button_play_again.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                run = False
            mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        screen.blit(Backgrounds[0], [0, 0])
        # -------------------------texto principal------------------------#
        draw_Final_screens("Game Over", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           450, 300)
        # pygame.draw.rect(screen, (255, 0, 0), Button_play_again)
        screen.blit(Button_grande, (300, 550))
        draw_complementos("Play Again", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 455,
                          565)

        pygame.display.update()

def Best_Score_Screen():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40)
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
        draw_text("Best Scores",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (375, 640))
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)

        pygame.display.update()


def level(nivel):
    global lives,score, pause

    pygame.mixer.music.load(lista_musica[nivel-1])
    pygame.mixer.music.play(-1,0,0)

    def create_cubes(cubos,nivel):
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
            vel_temporal_1 = random.randint(1,5)*  direccion_x
            vel_temporal_2 = random.randint(1,5)*  direccion_y
            cubos +=[[temporal,vel_temporal_1,vel_temporal_2]]
    
    def movimiento_cubos(lista):
        for i in lista:
            if i[0].x <= 0:
                i[1] = random.randint(1,5)
                i[2] = random.randint(-5,5)
                HIT_SOUND.play()
            if i[0].x +i[1] +50 >=900:
                i[1] = random.randint(1,5) * -1
                i[2] = random.randint(-5,5)
                HIT_SOUND.play()
            if i[0].y <= 50:
                i[2]= random.randint(1,5)
                i[1] = random.randint(-5,5)
                HIT_SOUND.play()
            if i[0].y+ i[2]+ 50>=640:
                i[2]= random.randint(1,5)*-1
                i[1] = random.randint(-5,5)
                HIT_SOUND.play()
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
                HIT_SOUND.play()
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
    Sound = pygame.Rect(15,10, 30,23)

    levels = False
    mouse_click = False
    invincibility = True
    timer = 0
    timer_2 = 0
    time = 60
    victory = False
    cubos = []
    exit = False
    create_cubes(cubos, nivel)

    while not levels:
        clock.tick(60)
        cursor_x, cursor_y = pygame.mouse.get_pos()

        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)):
            if mouse_click:
                print("Exit")
                levels = True
                exit = True
        if Sound.collidepoint((cursor_x,cursor_y)):
            if mouse_click:
                print(pause)
                if not pause:
                    pygame.mixer.music.pause()
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    pause = False
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
            if nivel ==1:
                score += 1
            if nivel == 2:
                score += 3
            if nivel == 3:
                score += 5
        timer_2 += 1

        if lives == 0:
            levels = True
        #------------------------move-----------------------#
        keys_pressed = pygame.key.get_pressed()
        player_move(keys_pressed)
        movimiento_cubos(cubos)
        collision_check(cubos, invincibility)

        screen.blit(Backgrounds[Niveles], [0, 0])
        #----------draw------------#
        for i in cubos:
            screen.blit(Asteroid ,(i[0].x,i[0].y))
            #pygame.draw.rect(screen,(255,255,255),i[0])
        #pygame.draw.rect(screen,(0,255,0),player)
        screen.blit(SpaceShip,(player.x,player.y))

        #----------draw------------#   
        #pygame.draw.rect(screen, (255, 255, 255), Sound)
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (450-130//2,2))
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 460, 15)

        #pygame.draw.rect(screen,(255,255,255), Sound)
        screen.blit(Icono_sonido, (15,10))
        draw_text(str(time),(0,0,0),450 + 40,665,Fuente_complementaria)      
        draw_text(str(score),(0,0,0),450 - 150 // 2 -75,665,Fuente_complementaria)
        screen.blit(LabelScore, (450 - 150 // 2 - 150 - 75, 665))
        screen.blit(LabelTime, (450 - 150 // 2, 665))
        screen.blit(LabelLives, (600, 665))
        for i in range(lives):
            screen.blit(Icono_vida,(hearth_position[i],650))

        pygame.display.update()

        #----------------level condition---------------------------#
        if time == 0:
            if nivel < 3:
                nivel += 1
                time = 60
                lives = 3
                timer = 0
                invincibility = True
                timer_2 = 0
                pygame.mixer.music.load(lista_musica[nivel-1])
                pygame.mixer.music.play(-1,0,0)
                cubos = []
                create_cubes(cubos, nivel)
            else:
                victory = True
                levels = True
    print(score)
    if not exit:
        if victory:
            print ("victory_screen()")
        #  Victory_screen()
        else:
            print("end_screen()")
            End_Screen()
    
    pygame.mixer.music.load("Sneaky Driver.mp3")
    pygame.mixer.music.play(-1,0,0)

menu()

