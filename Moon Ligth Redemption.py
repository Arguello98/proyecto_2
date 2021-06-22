#Se importan la bibliotecas que se utilizará para
import pygame, sys, random, os
pygame.init()
pygame.mixer.init()
#se inicia la ventana

screen = pygame. display.set_mode([900,700]) #Se configuran las dimensiones de la pantalla, va a ser igual en todas
pygame.display.set_caption("Moon light Redemption") # Titulo de la ventana
clock = pygame.time.Clock() # Clock es para que el juego corra a un numero determinado de fps

# Lista con los soundtracks ppropios de cada una de las pantallas del juego
lista_musica = ["01.mp3","02.mp3","03.mp3"]

#bg = pygame.image.load("Imagenes/Background.jpg").convert()
# Variables globales que se utilizaran en otras pantallas
lives = 3 # Vidas del jugador
score = 0 # Puntuacion del jugador inicializada en cero
pause = False # Falg para poder detener la musica cada vez que se preciona su respectivo boton
Niveles = 0 # Variable necesaria para la transicion de un nivel a otro
# Encuentra la frase en el codigo

# En esta variable se guarda el nombre del jugador
User = ""
#-------------------------------------------Sprites-----------------------------------------------------#

# La decalracion de este objeto o de este sprite abre la imagen respectiva y la redimenciona
Asteroid = pygame.transform.scale(
    pygame.image.load(
        os.path.join("Imagenes/Asteroide.png")
),(40,40)
)
# La decalracion de este objeto o de este sprite abre la imagen respectiva y la redimenciona
SpaceShip = pygame.transform.scale(
    pygame.image.load(
        os.path.join("Imagenes/SpaceShip.png")
    ),(50,50)
)
hearth_position = [715, 775,835] #Posiciones de los corazones referentes a la vida del jugador
BgMenu = pygame.image.load("Imagenes/BgMenu.png").convert() # Carga de la imagen del background del menu
BgL1 = pygame.image.load("Imagenes/Bglevel1.png").convert()# Carga de la imagen del background del nivel 1
Bgl2 = pygame.image.load("Imagenes/BgLevel2.jpg").convert()# Carga de la imagen del background del nivel 2
BgL3 = pygame.image.load("Imagenes/Bglevel3.jpg").convert()# Carga de la imagen del background del nivel 3
Button_grande = pygame.image.load("Imagenes/button(2).png") # Carga de un boton alargado
Button_pequeno = pygame.image.load("Imagenes/button.png") #Carga de un boton corto
Icono_vida  = pygame.image.load("Imagenes/Icono_vida.png") # Carga de los iconos de la vida
Icono_sonido = pygame.image.load("Imagenes/Icono_Sonido.png") #Carca para el icono de los sonidos y canciones
Backgrounds = [BgMenu, BgL1, Bgl2, BgL3] #Una lista para poder cambiar los backgrounds de cada una de las pantallas

#---------------------------music------------------------------#

pygame.mixer.music.load("Sneaky Driver.mp3")
pygame.mixer.music.play(-1,0,0)

HIT_SOUND = pygame.mixer.Sound("Grenade+1.mp3")#Efecto de sonido de los asteroides cuando chocan con algun borde o con la nave
#
#------------------------Fuentes de escritura-------------------------#
# Se declaran variables las cuales son las fuentes para poder escribir en el juego, este toma como parametro
# Una fuente descargada, su color y si tamaño.
Font_tutulo = pygame.font.Font("8-BIT WONDER.TTF", 40)
Fuente_complementaria = pygame.font.Font("LVDCGO__.TTF", 15)
Titulo = Font_tutulo.render("Moon light Redemption",0, (255, 255, 255))
label_font = pygame.font.Font("8-BIT WONDER.TTF", 20)
label_user = label_font.render("Write your name", 0, (255, 255, 255))
Font_botones = pygame.font.Font("8-BIT WONDER.TTF", 15)
Font_final_screens = pygame.font.Font("8-BIT WONDER.TTF", 55)


#-----------Funciones para escribir texto dentro de las pantallas---------------#
def draw_text(txt, color, x, y, font = Font_tutulo): #Toma como parametro el texto, color, coordenadas, y fuente

    text_obj = font.render(txt, 1, color) #Toma el objetvo para escribirlo
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y)) # Muestra dentro de la pantalla el texto centrado

def draw_complementos(txt, color, x, y, font = label_font):#Toma como parametro el texto, color, coordenadas, y fuente
    text_obj = font.render(txt, 1, color)#Toma el objetvo para escribirlo
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))# Muestra dentro de la pantalla el texto centrado


def draw_botones(txt, color, x, y, font = Font_botones):#Toma como parametro el texto, color, coordenadas, y fuente
    text_obj = font.render(txt, 1, color)#Toma el objetvo para escribirlo.
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y)) # Muestra dentro de la pantalla el texto centrado

def draw_Final_screens (txt, color, x, y, font = Font_final_screens):#Toma como parametro el texto, color, coordenadas, y fuente
    text_obj = font.render(txt, 1, color)#Toma el objetvo para escribirlo.
    screen.blit(text_obj, (x - text_obj.get_width() // 2, y))# Muestra dentro de la pantalla el texto centrado

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
        resultado += [[name,int(score[:-1])]]
    return resultado

#-----------hijo de isac-------------------#
def dividir_lista(lista):
    pivote = lista[0] #el pivote será el punto de referencia de donde se empezará a dividir la lista
    lista_menor = [] # Lista en donde se almacenan los numeros menores al pivote
    lista_mayor = [] #Lista en donde se almacenan los numeros mayores al pivote

    for i in range(1, len(lista)):
        if lista[i][1] < pivote[1]: # Si el numero es menor al pivote
            lista_menor.append(lista[i]) #Este se numero menor se almacenará en la lista de los numeros menores
        else: #El caso contrario es que si no son menores es que sean  mayores al pivote
            lista_mayor.append(lista[i]) #Este numero mayor se almacenará en la lista de los numeros mayores
    return lista_menor, pivote, lista_mayor # Se cocatena una lista con los numeros menores, el pivote y la lista mayor

# Esta funcion realiza los mismo pero de manera que divida no solo una lista, sino los dos extremos, los cuales son la lista menor y mayor
def quicksort(lista):
    if lista == []: # Se detiene una vez que no hayan elementos en la lista
        return lista # Cuando se cumple el caso base, retorna la lista a como queda
    lista_menor, pivote, lista_mayor = dividir_lista(lista) # La lista de los menores y mayores será igual a la funcion anterior para poder ser dividida
    return quicksort(lista_menor) + [pivote] + quicksort(lista_mayor) # Retorna una lista con los numeros ordenados con menores + pivote + mayores

f = open("leaderboard.txt","rt")
leaderboard = f.readlines() #creates a list of the different places
leaderboard = creating_leaderboard_2(leaderboard)
leaderboard = quicksort(leaderboard)
print (leaderboard)
f.close()



#--------------------Pantalla del menu------------------------------#
def menu():
    #Se llaman a las variables globales que se utilizaran en esta pantalla
    global Niveles, lives, score, pause, User

    # Rectangulos que serán los hitbox de cada uno de los botones que se utilizarán en la pantalla
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

    # Flags necesarios para la pantalla del menu
    mouse_click = False # Clikeo del mouse
    active = False
    Niveles = 1 #Para que el nivel predeterminado sea el primero, la variable se inicia en 1

    #--------ciclo logico------------#

    while True:
        lives = 3 # Vidas del jugador
        score = 0 # Puntuacion
        clock.tick(60) # FPS a los que se correrá el juego
        cursor_x , cursor_y =  pygame.mouse.get_pos() #Coordenadas del cursor

        #-----------clicks----------------------------#

        if mouse_click: # Se hace un click
            active = False
        if mouse_click: #Se hace un click
            active = False
        if button_play.collidepoint((cursor_x, cursor_y)): # Si el cursor toca el hitbox del button_play
            if mouse_click and User != "": # Si se hace un click y si se escribe un user name
                #print("Historia :v")
                level(Niveles) # Se abre la pantalla del nivel 1
                User = ""
        if button_Easy.collidepoint((cursor_x, cursor_y)):# Si el cursor toca el hitbox del primer nivel
            if mouse_click: # Si se hace  un clicj sobre el hitbox
                print("Level Easy")
                Niveles = 1 #Se abre la pantalla del primer nivel
                #level(Niveles)
        if button_Medium.collidepoint((cursor_x, cursor_y)):# Si el cursor toca el hitbox del segundo nivel
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                #print("Level Madium")
                Niveles = 2 #Se abre la pantalla del primer nivel
                #level(Niveles)
        if button_Hard.collidepoint((cursor_x, cursor_y)):# Si el cursor toca el hitbox del tercer nivel
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                #print("Level Hard")
                Niveles = 3 #Se abre la pantalla del tercer nivel
                #level(Niveles)
        if button_Credits.collidepoint((cursor_x, cursor_y)):# Si el cursor toca el hitbox del boton de creditos
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                #print("Credits")
                Creditos()#Se abre la pantalla de los creditos
        if button_Instructions.collidepoint((cursor_x, cursor_y)):#Si el cursor toca el hitbox del boton de las intrucciones
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                #print("Instructions")
                Instructions()# Se abre la pantalla de las instruciones
        if Button_Score.collidepoint((cursor_x, cursor_y)): #Si el cursor toca el hitbox del boton del leaderboard
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                #print("Best Scores")
                Best_Score_Screen() # Se abre la pantalla de los mejores puntajes
        if Textbox.collidepoint((cursor_x, cursor_y)): #Si el cursor toca el hitbox del entry
            if mouse_click:# Si se hace  un clicj sobre el hitbox
                active = True # Se activa la bandera que permite escribir
                print() #Escribe sobre la pantalla lo que escribe el usuario
        mouse_click = False # El mouse se bloquea por así decirlo para que cuando termine el click ya no haga nada

        #----------eventos-----------------#

        # Ciclo para que cuando se toque la X de la pantalla, se salga del juego
        for event in pygame.event.get(): #Si el evento es un evento fuera de la propia la pantalla de juego
            if event.type == pygame.QUIT: # Si se preciona la X de la parte superior de la pantalla
                pygame.quit() #Se detiene el juego
                sys.exit() #x2

           # Funcion que ve el movimiento y los clicks del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True
            # Funcion que hace que se pueda escribir y usar todos los caracteres del teclado
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        User = User[:-1]
                    elif len(User) < 10:
                        User += event.unicode

            if Sound.collidepoint((cursor_x, cursor_y)): #Si el cursor toca el hitbox del sonido
                if mouse_click: #Y se realiza un click por parte del usuario
                    #print(pause)
                    if not pause: # Si el flag no está activado
                        pygame.mixer.music.pause() # La musica se pausa
                        pause = True # el flag pasa a ser verdadero
                    else: # Si el flag esta en verdadero
                        pygame.mixer.music.unpause() # La musica se reanuda
                        pause = False # Y la bandera vuelve a ser falsa

        #-----------------drwaw--------------------------#
        screen.blit(Backgrounds[0], [0, 0]) # Se configura el background en pantalla
        #-------------------------texto principal------------------------#
        draw_text("Moon light Redemption",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50) # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        draw_complementos("Write Your name ", (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 300,160)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
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
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        draw_complementos("Best Score", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 900 // 2,463)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        draw_complementos("Instructions", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 290, 615)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        draw_complementos("Credits", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),610, 615)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        if Niveles == 1: # Si el nivel es el uno
            draw_botones("Easy",  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 225, 315)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            #Eso si, en las letras del boton del nivel 1
            draw_botones("Medium", (0,0,0), 450, 315) #Este boton se pone en negro
            draw_botones("Hard", (0,0,0), 675, 315) # Y este tambien :v
        if Niveles == 2: # Si el nivel es el 2
            draw_botones("Easy",   (0,0,0), 225, 315)#Este boton se pone en negro
            draw_botones("Medium", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 450, 315)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            # Eso si, en las letras del boton del nivel 2
            draw_botones("Hard", (0,0,0), 675, 315)# Y este tambien :v
        if Niveles == 3: # Si el nivel es el 3
            draw_botones("Easy",  (0,0,0), 225, 315)#Este boton se pone en negro
            draw_botones("Medium", (0,0,0), 450, 315)# Y este tambien :v
            draw_botones("Hard", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 675, 315)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            # Eso si, en las letras del boton del nivel 3

            # A ALLAN TURING LE ENCANTA EL PINTO CON PAPA A LA HUANCAINA y tambien es joto, por eso lo mataron :,c

        pygame.display.update()

#-------------Pantalla de los creditos-------------#
def Creditos():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40) #Boton exit
    mouse_click = False #Flag para los clicks
    run = True # Bandera para correr el nivel
    while run:
        clock.tick(60) #FPS a los que el juego corre
        cursor_x, cursor_y = pygame.mouse.get_pos()


        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)): #Si el hitbox está sobre el boton de exit
            if mouse_click: # Si se presiona el click
                #print("Exit")
                run  = False # El juego se detine

        #--------eventos-------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si el evento es que se presione la X superior de la pantalla
                pygame.quit() #El juego se detiene
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #Si el evento es que se presione algo con el mause
                if event.button == 1: #El eveneto es igual a algun boton
                    mouse_click = True #Se concede el permiso para presionar
        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Credits",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (375, 640)) #Se muestra el boton pequeño en pantalla
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        #---------------------------Creditos---------------------------------#
        #En lo siguiente se escribe las frases sin la linea maldita#
        draw_complementos("Costa Rica",(255,255,255),450,150)
        draw_complementos("Instituto tecnologico de Costa Rica",(255,255,255), 450,200)
        draw_complementos("Ingenieria en Computadores",(255,255,255),450, 250)
        draw_complementos("Profesor Luis Barboza Artavia",(255,255,255), 450,300)
        draw_complementos("Taller de programacion" ,(255,255,255),450,350)
        draw_complementos("Daniel Arguello Poma e Isac Marin Sirias",(255,255,255),450,400)
        draw_complementos("Version X", (255,255,255),450,450)
        draw_complementos("2021", (0,0,0),450 + 200,550)
        draw_complementos("Grupo 4", (0,0,0),450//2,550)
        #Y cuando hablo de lo siguiente, me refiero a que termina aquí bby#
        pygame.display.update()

#-----------------Funcion en donde se encuentra la pantalla de instrucciones-----------#
def Instructions():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40) #Se declara el rectangulo que será el hitbox del boton exit
    mouse_click = False #El flag de los clicks se inicializa en falso

    run = True #Flag en donde se corre la pantalla
    while run: #Si el flag de run esta activo
        clock.tick(60) #FPS a los que corre la pantalla
        cursor_x, cursor_y = pygame.mouse.get_pos() #Coordenadas del cursor

        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)): #Si el hitbox está sobre el boton de exit
            if mouse_click: # Si se presiona el click
                #print("Exit")
                run = False # El juego se detine
            mouse_click = False
        #--------eventos-------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si el evento es que se presione la X superior de la pantalla
                pygame.quit() #El juego se detiene
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #Si el evento es que se presione algo con el mause
                if event.button == 1: #El eveneto es igual a algun boton
                    mouse_click = True #Se concede el permiso para presionar

        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_text("Instructions",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        #pygame.draw.rect(screen, (255, 0, 0), ButtonExit)
        screen.blit(Button_pequeno, (375, 640)) #Se pinta el boton pequelo en pantalla
        draw_complementos("Welcome to Moon Light Redemption", (255, 255, 255), 450, 200)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("It passes through the two most important cities", (255, 255, 255), 450, 250)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("cities protected by a meteor shower", (255, 255, 255), 450, 300)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("Be careful", (255, 255, 255), 450, 350)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("To use your ship use the movement keys", (255, 255, 255), 450, 400)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("Get to the moon and become the winner", (255, 255, 255), 450, 450)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("", (255, 255, 255), 450, 450)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # -= linea maldita
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        # Esta si tiene la linea maldita jejejejeje

        pygame.display.update()

#------------------- Pantalla de victoria------------------#

def Victory_screen():
    global User, score,leaderboard #Se llaman a las variables globales que se utilizaran en la pantalla
    
    leaderboard.append([User,score]) #Se escribe el nombre de usuario y la puntuacion en el leaderboard
    leaderboard = quicksort(leaderboard)# Mi hijo ya no recibe una lista, sino que recibe el leaderboard
    Button_play_again = pygame.Rect(450 - 300 // 2, 550, 300, 50) #Se llama al hitbox para poder volver a jugar
    mouse_click = False # El flag del mouse se inicializa en falso

    f = open("leaderboard.txt","w") #Se abre  eel txt
    for i in range(7): # Si la puntuacion está entre 1 y 7
        f.write(leaderboard[-i-1][0] + "," + str(leaderboard[-1-i][1]) + "\n") #Se escribe en el txt, el nombre y la puntuacion del usuario
    f.close() # Se cierra el txt
    
    posicion = 0
    print(leaderboard)
    while posicion < len(leaderboard):
        if [User,score] == leaderboard[-posicion-1]:
            #print("hola")
            posicion +=1
            break
        else:
            posicion += 1

    #print(posicion)
    high_score = False
    if posicion < 8:
        high_score = True

    Button_play_again = pygame.Rect(450 - 300 // 2, 550, 300, 50) #Rectangulo con el hitbox del boton "play again"
    mouse_click = False #El flag del mouse inicializa en flaso
    run = True
    while run:
        clock.tick(60) # FPS a los que corre el juego
        cursor_x, cursor_y = pygame.mouse.get_pos() #coordenadas dle cursor

        # ---------Jugar de nuevo--------#
        if Button_play_again.collidepoint((cursor_x, cursor_y)): # Cuando el cursor está en el hitbox del boton play
            if mouse_click: #Cunado el se presiona un el click
                run = False # El juego deja de correr
            mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si hay un contacto con la X superior en la pantalla
                pygame.quit() #Se sale del juego
                sys.exit() #x2
            if event.type == pygame.MOUSEBUTTONDOWN: #Si el evento es que se presione algo con el mause
                if event.button == 1: #El eveneto es igual a algun boton
                    mouse_click = True #Se concede el permiso para presionar



        screen.blit(Backgrounds[0], [0, 0])
        #-------------------------texto principal------------------------#
        draw_Final_screens("Victory for you",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,100)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras

        if high_score: # Se ven en pantalla el nuevo mejor puntajes
            draw_complementos("new high score", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,300)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            draw_complementos("Position  " + str(posicion), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,350)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            draw_complementos("Score  " + str(score), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,400)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        screen.blit(Button_grande, (300, 550)) #Se dibuja el boton para jugar de nuevo
        draw_complementos("Play Again", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 455, 565)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        pygame.display.update()

def End_Screen():
    global User, score, leaderboard  # Se llaman a las variables globales que se utilizaran en la pantalla

    leaderboard.append([User, score])  # Se escribe el nombre de usuario y la puntuacion en el leaderboard
    leaderboard = quicksort(leaderboard)  # Mi hijo ya no recibe una lista, sino que recibe el leaderboard
    Button_play_again = pygame.Rect(450 - 300 // 2, 550, 300, 50)  # Se llama al hitbox para poder volver a jugar
    mouse_click = False  # El flag del mouse se inicializa en falso

    f = open("leaderboard.txt", "w")  # Se abre  eel txt
    for i in range(7):  # Si la puntuacion está entre 1 y 7
        f.write(leaderboard[-i - 1][0] + "," + str(
            leaderboard[-1 - i][1]) + "\n")  # Se escribe en el txt, el nombre y la puntuacion del usuario
    f.close()  # Se cierra el txt

    posicion = 0
    print(leaderboard)
    while posicion < len(leaderboard):
        if [User,score] == leaderboard[-posicion-1]:
            print("hola")
            posicion +=1
            break
        else:
            posicion += 1

    print(posicion)
    high_score = False
    if posicion < 8:
        high_score = True
    run = True

    while run:
        clock.tick(60) #FPS a los que corre el juego
        cursor_x, cursor_y = pygame.mouse.get_pos() #Coordenadas del cursor

        # ---------Jugar de nuevo--------#
        if Button_play_again.collidepoint((cursor_x, cursor_y)): # Cuando el cursor está en el hitbox del boton play
            if mouse_click: #Cunado el se presiona un el click
                run = False # El juego deja de correr
            mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Si hay un contacto con la X superior en la pantalla
                pygame.quit() #Se sale del juego
                sys.exit() #x2
            if event.type == pygame.MOUSEBUTTONDOWN: #Si el evento es que se presione algo con el mause
                if event.button == 1: #El eveneto es igual a algun boton
                    mouse_click = True #Se concede el permiso para presionar

        screen.blit(Backgrounds[0], [0, 0])
        # -------------------------texto principal------------------------#
        draw_Final_screens("Game Over", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                           450, 100)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        if high_score: # Se ven en pantalla el nuevo mejor puntajes
            draw_complementos("new high score", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,300)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            draw_complementos("Position  " + str(posicion), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,350)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            draw_complementos("Score  " + str(score), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            450,400)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        
        screen.blit(Button_grande, (300, 550)) # Se dibuja el boton gande dentro de las pantallas
        draw_complementos("Play Again", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 455,
                          565)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras

        pygame.display.update()

#-----------Pantalla de los mejores puntajes-----------#

def Best_Score_Screen():

    ButtonExit = pygame.Rect(450 - 130 // 2, 650, 130, 40) #Se pone el hitbox del boton exit en pantalla
    mouse_click = False #El flag mouse se inicializa en falso

    run = True
    while run:
        clock.tick(60) #FPS a los que corre la pantalla
        cursor_x, cursor_y = pygame.mouse.get_pos() #Coordenadas del mouse

        if ButtonExit.collidepoint((cursor_x, cursor_y)):  # Si el hitbox está sobre el boton de exit
            if mouse_click:  # Si se presiona el click
                # print("Exit")
                run = False  # El juego se detine
            mouse_click = False
            # --------eventos-------#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si el evento es que se presione la X superior de la pantalla
                pygame.quit()  # El juego se detiene
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Si el evento es que se presione algo con el mause
                if event.button == 1:  # El eveneto es igual a algun boton
                    mouse_click = True  # Se concede el permiso para presionar

        screen.blit(Backgrounds[0], [0, 0]) #Se pone el background respectivo de la pantalla
        #-------------------------texto principal------------------------#
        draw_text("Best Scores",(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        450,50)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        i = 140
        position = -1
        while i <= 500:
            draw_text(leaderboard[position][0] ,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 300, i)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            draw_text(str(leaderboard[position][1]),(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 600, i)
            # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
            i += 60
            position -= 1

        screen.blit(Button_pequeno, (375, 640)) #Se dibuja en pantalla el boton pequeño
        draw_complementos("Exit", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 453, 653)
        # Se hace uso de la linea maldita de codigo para poder escribir una vomitada de colores magicos en las letras
        pygame.display.update()

#-------------------Pantalla de los niveles------------------------#

def level(nivel):
    global lives,score, pause, User #Se llaman a las variables que se van a utilizar en esta pantalla

    #musica dependiendo del nivel
    pygame.mixer.music.load(lista_musica[nivel-1]) #carga la cancion
    pygame.mixer.music.play(-1,0,0) #reproduce la cancion en forma de loop

    #creacion de los enemigos dependiendo del nivel
    def create_cubes(cubos,nivel):
        for i in range(5*nivel): #por nmivel de dificultad crea un enemigo
            temporal = pygame.Rect(random.randint(10, 800),random.randint(100,500),40,40) #crea un rectangulo que sera el hitbox del enemigo
            if random.randint(-5,5) > 0: #dependiendo de si el numero es mayor o menor se define la direccion en la cual se va a mover
                direccion_x = -1 #se mueve hacia la izquierda
            else:
                direccion_x = 1 #se mueve hacia la derecha
            if random.randint(-5,5)>0: # dependiendo del si el numero es positivo o negativo define la direccion en la cual se va a mvoer
                direccion_y = -1 # se mueve hacia arriba
            else:
                direccion_y = 1 #se mueve hacia abajo
            vel_temporal_1 = random.randint(1,5)*  direccion_x #se define una velicdad para el enemigo en el eje x
            vel_temporal_2 = random.randint(1,5)*  direccion_y #se define una velocidad para el enemigo en el eje  y
            cubos +=[[temporal,vel_temporal_1,vel_temporal_2]] # se añade el hitbox asi com su velocidad en x y y  a la lista de enemigos
    
    #movimiento de los enemigos, recibe la lista de enemigos
    def movimiento_cubos(lista): 
        for i in lista: #por cada elemento de la lista
            if i[0].x <= 0: #si colisiona con el lado izquierdo pantalla
                i[1] = random.randint(1,5) #se genera un numero para la velocidad en x que es positivo para que se mueve hacia la derecha
                i[2] = random.randint(-5,5) #se genera un numero para la velocidad en el y que puede ser tanto positivo como negativo
                HIT_SOUND.play() #se ejecuta el sonido de golpe
            if i[0].x +i[1] +50 >=900: #si colisiona con el lado derecho de la pantalla
                i[1] = random.randint(1,5) * -1 #se genera un numero aleatorio en el cual se movera hacia la izquierda 
                i[2] = random.randint(-5,5) #se genera un numero aleatorio para la velocidad en y que puede ser tanto positivo como negativo
                HIT_SOUND.play() #se ejecuta el sonido de golpe
            if i[0].y <= 50: #en caso de que se colisiona con el lado superior de la pantalla
                i[2]= random.randint(1,5) #se genera un numero para la velocidad en el eje y de la pantalla, para que se mueva hacia abajo
                i[1] = random.randint(-5,5) #se genera un numero para la velocidad en x que puede ser tanto positivo como negativo
                HIT_SOUND.play() #se ejetcuta el sonido del golpe
            if i[0].y+ i[2]+ 50>=640: #en caso de que colisiona con el lado inferior de la pantalla
                i[2]= random.randint(1,5)*-1 #se genera un numero negativo para la velocidad en y, para que se mueva hacia arriba
                i[1] = random.randint(-5,5) #se genera un numero que puede ser tanto positivo como negativo para la velocidad en x
                HIT_SOUND.play() #ejecuta el sonido del golpe
            else:#en caso de que no colisione con ningun bor de la pantalla
                i[0].x += i[1]  #al valor de x del hitbox se le suma la velocidad en x
                i[0].y += i[2] #al valor de y del hitbox se le suma la volocidad en y
    
    #el movimiento de la nave del jugador
    def player_move(keys_pressed): #recibe la tecla presionada por el jugador
        VEL = 5 #se define una velocidad a la cual se va a mover la nave
        if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0: #si se presiona el boton izuqierdo y no se sale del limite 
            player.x -= VEL #se mueve hacia la izquierda
        if keys_pressed[pygame.K_RIGHT] and player.x +VEL + 50 < 900:#si se presiona el boton de la derecha y no se sale del limite 
            player.x += VEL #se mueve hacia la derecha
        if keys_pressed[pygame.K_DOWN] and player.y + VEL + 50 < 640:#si se presiona el boton de abajo y no se sale del limite 
            player.y += VEL #se mueve hacia abajo
        if keys_pressed[pygame.K_UP] and player.y - VEL > 50:#rsi se presiona el boton de arriba y no se sale del limite 
            player.y -= VEL #se mueve hacia arriba

    #verifica la colision de los enemigos con el jugador
    def collision_check(lista,invincibility): #recibe la lista de enemigos y una variable para saber si el jugador puede recibir daño
        global lives #llama la varriable de vidas
        for i in lista: #por cada elemento de la lista
            if player.colliderect(i[0]) and not invincibility: #si el jugador colisiona con el enemigo y puede recibir daño
                cubos.remove(i) #remueve el enemigo de la lista de enemigos
                HIT_SOUND.play() #reproduce el sonido de golpe
                lives -= 1 #disminye el valor de vidas en 1 
    
    player = pygame.Rect(450,450,50,50) #Hitbox del label del jugador
    clock = pygame.time.Clock()

    #------------Barra superior----------------#
    BarraSuperior = pygame.Rect(0,0, 900, 50) #Barra o hitbox en donde estará el boton para volver al menu y el boton del sonido
    ButtonExit = pygame.Rect(450-130//2,5,130,40) # Hitbox del boton exit

    #-------------Barra de progreso-----------#
    BarraProgreso = pygame.Rect(0,700-60, 900, 60) # Barra de progreso, en la cual estaran varios labels
    #----------------texto-------------#
    
    LabelScore = Fuente_complementaria.render("SCORE:", 0, (0, 0, 0)) #Se escribe el label del score en pantalla
    LabelTime = Fuente_complementaria.render("TIME:", 0, (0, 0, 0)) #Se escribe el label del tiempo en pantalla
    LabelLives = Fuente_complementaria.render("LIVES:", 0, (0, 0, 0)) #Se escribe el label de las vidas en pantalla
    LabelPlayer = Fuente_complementaria.render("Player: " + User, 0, (0,0,0)) #Se escribe el label del jugador en pantalla
    Sound = pygame.Rect(15,10, 30,23) # Hitbox del boton de sonido

    levels = False #Bandera de los niveles en inicializada en falso
    mouse_click = False #Bandera de los clicks inicializada en falso
    invincibility = True #bandera de invisibilidad inicializada en falso
    timer = 0 # variable timer se inicializa en 0
    timer_2 = 0 # de la misma manera que el segundo timer
    time = 60 # El timepo de juego se inicializa en 60 para hacer una cuenta regresiva
    victory = False # Bandera de victoria se inicializa en falso
    cubos = [] #Esta variable almacena las los cubos o asteroides
    exit = False
    create_cubes(cubos, nivel) #Funcion que crea los cubos, toma el cubo y tambien el nive para saber cuantos deben de haber dentro de la lista

    #EXTRAÑO A MI EX

    while not levels:
        clock.tick(60) #FPS a los que corre la pantalla
        cursor_x, cursor_y = pygame.mouse.get_pos() #

        #-------Volver a menu------#
        if ButtonExit.collidepoint((cursor_x, cursor_y)): # Si el cursor esta sobre el boton de exit
            if mouse_click: #Y se hace algun click
               # print("Exit")
                levels = True #La variable de los niveles se convierte en verdadero
                exit = True # De la misma manera a la de exit
        if Sound.collidepoint((cursor_x,cursor_y)): #Cuando el cursor está sobre el sound
            if mouse_click: #y se realiza un click
                #print(pause)
                if not pause: #Cuando no está en falso el sound
                    pygame.mixer.music.pause() #La musica se detiene
                    pause = True #Y la bandera se convierte falsa
                else: #El caso conntrario es que la musica este pausada
                    pygame.mixer.music.unpause() #Entonces la musica se reanuda
                    pause = False #Y la vandera vuelve a ser  falsa
        mouse_click = False #Esto hace algo como para que por cada click se realice una accion y no

        # Ciclo para que cuando se toque la X de la pantalla, se salga del juego
        for event in pygame.event.get(): #Si el evento es un evento fuera de la propia la pantalla de juego
            if event.type == pygame.QUIT: # Si se preciona la X de la parte superior de la pantalla
                pygame.quit() #Se detiene el juego
                sys.exit() #x2
           # Funcion que ve el movimiento y los clicks del mouse
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

        screen.blit(Backgrounds[Niveles], [0, 0]) # Backgrounds de la pantalla
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
        screen.blit(Icono_sonido, (15,10)) # Se dibuja el icono del sonido en la pantalla
        draw_text(str(time),(0,0,0),550,665,Fuente_complementaria) # Se escribe el timepo en pantalla a la par de su respectivo label
        draw_text(str(score),(0,0,0),400,665,Fuente_complementaria) # Se escribe el score en pantalla a la par de su respectivo label
        screen.blit(LabelScore, (275- 10, 665)) # Se escribe el label del score en la pantalla
        screen.blit(LabelTime, (440, 665))# Se escribe el label del tiempo en la pantalla
        screen.blit(LabelLives, (600, 665))# Se escribe el label de las vidas en la pantalla
        screen.blit(LabelPlayer, (25, 665))# Se escribe el label de "player" en la pantalla
        for i in range(lives):
            screen.blit(Icono_vida,(hearth_position[i],650))
            #En serio extraño mucho a mi ex :.ccccc#

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

