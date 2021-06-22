Moon light Redemption
====================================


## Introducción

El proyecto presente consta en el diseño e implementación de una interfaz gráfica para la realización del juego Moon Light Remdemption, el cual se trata de un juego, que tendrá como principal objetivo, el esquivar los asteroides propios de cada nivel durante el mayor tiempo posible, utilizando el lenguaje de programación Python 3.9.

Dicho juego tendrá su respectivo menú, en donde se encontrarán una variedad de botones, con los cuales el usuario podrá interactuar con el programa.

El juego constituirá de tres pantallas de juego, en donde el jugador tendrá que interactuar con la nave principal, la cual constará de parámetros de movimiento en el eje X y en el eje Y. Esto con la finalidad de esquivar todos los asteroides propios de cada nivel por un tiempo de 60 segundos, al finalizar el tiempo y si el jugador aun cuenta con vidas, este avanzará al siguiente nivel.

El jugador tendrá 3 vidas, las cuales se restarán con cada colisión que tenga con alguno de los asteroides.
Cada segundo que la nave se mantenga en juego, se sumará una cantidad de puntos dependiendo de cada nivel, al finalizar el juego, este puntaje se reflejará en la pantalla que refleja los mejores puntajes, si es que el jugador supera los 7 mejores lugares. 

## Secciones de código importantes

* **Movimiento de la nave:**
	```
	def player_move(keys_pressed):
        
        VEL = 5

        if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0: 
            player.x -= VEL

        if keys_pressed[pygame.K_RIGHT] and player.x +VEL + 50 < 900:
            player.x += VEL

        if keys_pressed[pygame.K_DOWN] and player.y + VEL + 50 < 640:
            player.y += VEL

        if keys_pressed[pygame.K_UP] and player.y - VEL > 50:
            player.y -= VEL
	```

	* La función de movimiento actúa de tal forma en la que la nave recibe las teclas presionadas y dependiendo de cuál sea la tecla presionada (derecha, izquierda, arriba o abajo) se mueve la cantidad de pixeles que se determina por la variable "VEL" 
    En caso de que la tecla presionada sea la flecha izquierda se mueve hacia la izquierda, siempre y cuando el valor de la coordenada X de la nave no sea menor a 0, porque en tal caso se saldría de la pantalla.

        Lo mismo sucede cuando se presiona la tecla derecha, pero en caso de el borde la derecha a parte de verificar la posición x, se tiene que sumar el ancho de la imagen para verificar que no se salga del límite derecho o el límite inferior.
        
        De la misma manera se han de verificar las coordenadas en Y para el movimiento de arriba y abajo, esto con el fin de que la nave no se salga de su respectiva pantalla de juego.


* **Movimiento de los asteroides:**
	```
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
	```
	
	* El movimiento de los asteroides funciona recibiendo una lista conteniendo la cantidad de enemigos y cada elemento de la lista contiene el objeto de *Rect* que es *hitbox* de los enemigos, además de esto contiene  una velocidad en el eje X y una velocidad en el eje Y, dicha  velocidad se mantiene hasta que choca con algún borde de la pantalla, cuando esto ocurre se invierte el valor del eje en el cual colisionó, aparte de generar un valor aleatorio en el otro eje para que el movimiento se pueda considerar como aleatorio.

        Por ejemplo, si un asteroide choca con el lado izquierdo de la pantalla se invierte la dirección en X para que el asteroide se mueva hacía la derecha, además de lo anterior mencionado se genera un valor que puede ser tanto positivo como negativo para que se modifique la velocidad en el eje en el que se está moviendo el asteroide, procedentemente el asteroide tendrá la capacidad de  moverse hacia arriba o hacia bajo sin importar cual haya sido su valor inicial antes del golpe.

* **Quicksort:**
	```
	def dividir_lista(lista):
        pivote = lista[0]
        lista_menor = []
        lista_mayor = []

        for i in range(1, len(lista)):
            if lista[i][1] < pivote[1]:
                lista_menor.append(lista[i])
            else:
                lista_mayor.append(lista[i])
        return lista_menor, pivote, lista_mayor
    
    def quicksort(lista):
        if lista == []:
            return lista
        lista_menor, pivote, lista_mayor = dividir_lista(lista)
        return quicksort(lista_menor) + [pivote] + quicksort    (lista_mayor)
	```
	
    * El *quicksort* se define como un algoritmo de ordenamiento en el cual elige un elemento del conjunto (la lista) a ordenar, el cual es llamado como “pivote”.
    Este ayuda para poder resituar los demás elementos de la lista a cada lado del pivote, de esta manera se puede obtener que todos los elementos menores queden situados a un lado y al otro lado todos los elementos mayores al pivote. Los elementos que son iguales al pivote ocupan el mismo lugar que le corresponderá en la lista ordenada.

    
        Una vez que la lista queda dividida en sublistas, una correspondiente a los elementos menores al pivote y otra a los mayores al pivote, se repite este método recursivo para las sublistas, esto hasta que la lista quede completamente ordenada.

        Para la implementación de este algoritmo dentro del proyecto, este recibe una lista compuesta por el nombre del jugador y el puntaje obtenido en partida ([[[[“Nombre”, Score1], [“Nombre”, Score2], [“Nombre”, Score3]]]]), en donde se toma en cuenta el valor numérico dentro de la sublista, y mantiene el  nombre del usuario dentro en la lista en cada una de las divisiones, esto para que en el *leaderboard* .se pueda ver el nombre del usuario junto a su respectiva puntuación.

## Resultados
Se pudieron concluir a cabalidad todos los objetivos esperados dentro de del diseño del programa, entre los cuales están:

* **Pantalla de inicio y complementarias:**

| Figura 1         | Figura 2  | Figura 3 |
| ----------------- | --------- | ----------- |
|   ![Menú](https://user-images.githubusercontent.com/83249731/122828553-12180b80-d2a3-11eb-9199-db294ddee470.png) |  ![Instrucciones](https://user-images.githubusercontent.com/83249731/122828667-31169d80-d2a3-11eb-87ca-d11e20aacedf.png)|  ![Creditos](https://user-images.githubusercontent.com/83249731/122828802-5dcab500-d2a3-11eb-8fad-60545fa98cc2.png)|
|   <p align="center">**Figura 4**</p>     | <p align="center">**Figura 5**</p>  | <p align="center">**Figura 6**</p>    |
|![Best scores](https://user-images.githubusercontent.com/83249731/122829316-142e9a00-d2a4-11eb-9a3e-eccd769e0c63.png)| ![WinnerScreen](https://user-images.githubusercontent.com/83249731/122829458-450ecf00-d2a4-11eb-85b3-72b9adcf70dd.png)   | ![ScreenGO](https://user-images.githubusercontent.com/83249731/122829507-56f07200-d2a4-11eb-92c7-14a2d7ce0861.png)|
|<p align="center">**Figura 7**</p>  |<p align="center">**Figura 8**</p>   |<p align="center">**Figura 9**</p>   |
|   ![Nivel1](https://user-images.githubusercontent.com/83249731/122829964-e9911100-d2a4-11eb-8d0f-55c5683bce90.png)| ![Nivel2](https://user-images.githubusercontent.com/83249731/122830267-57d5d380-d2a5-11eb-8c8e-a02ab268e62b.png)|![Nivel3](https://user-images.githubusercontent.com/83249731/122830312-67edb300-d2a5-11eb-99e4-8f5553b3c5a2.png)





Como se denota en la Figura 1, la pantalla de inicio tiene acceso a ventanas
diferentes, las figuras 2 y 3 se tratan pantallas complementarias de información sobre programa para conocimiento del usuario, las cuales indican por quienes y en donde fue realizado el videojuego, las instrucciones que debe de seguir para poder jugar de una manera correcta, y su puntaje
una vez que ya haya acabado su partida.

* **Niveles y objetos del de juego:**



    * ***Niveles:*** Como se puede apreciar en la figura 7, 8 y 9 en cada un de los niveles se lograron los resultados esperados que se plantearon en el diseño del mismo, dado a que en cada uno de los niveles, los asteroides se mueven en direcciones y a velocidades aleatorias en el eje X y en el eje Y, haciendo que su movimiento sea impredecible, a medida que se avanza de nivel, los asteroides aumentan en número, haciendo que cada nivel tenga una dificultad progresiva con respecto al nivel anterior.

    * ***Nave del jugador y generalidades del movimiento:*** La nave que se encuentra en cada uno de los tres niveles tiene la capacidad de moverse con las teclas de movimiento. Pudiendo moverse en el eje X, en el eje Y, y en diagonal, hacía cualquiera de los puntos cardinales. Todo este movimiento limitado por las dimensiones de la pantalla de juego, esto para que la nave no se salga de la pantalla de juego.

    * ***Barra de progreso:*** Cada nivel posee un *game progress bar* el cual posee el puntaje del jugador, el cual se va actualizando a medida que corre el tiempo de juego, de la misma manera cuenta con la vida del jugador, la cual se verá reducida cada vez que el un asteroide colisiona con la nave. Además de esto cuanta con el nombre del jugador en pantalla y un temporizador por nivel, el cual indica el tiempo faltante para que ocurra una transición de nivel.

    * ***Botón Exit:***  En todas las figuras, menos en la figura 1 se aprecia que en cada una de las pantallas del programa la presencia de un botón "Exit", el cual
    retorna a la pantalla inicial cada vez que el jugador decida acabar con el juego.

     * ***Efectos musicales y bagckgrounds:*** Tanto el menú como las pantallas complementarias cuentan con un *background* y un *soundtrack* diferente acorde con la temática del juego, además de esto, cada pantalla cuenta con un botón *sound on - sound off*, el cual detendrá o reanudará la música del juego, esto sin intervenir con los efectos sonoros propios de los asteroides.

## Conclusiones

**1.** Al realizar la documentación interna, se reconoce la importancia de hacerla lo mas clara y lo más detallada posible, ya que es necesario para el entendimiento de las demás personas a la hora de leer el código realizado.

**2.** Se concluye el proyecto con la idea de que al crear algo grande a como lo es un videojuego, con cosas relativamente básicas y sin tener muchos recursos o mucho conocimiento de programación, se pueden lograr cosas muy provechosas e impresionantes como lo es un juego.

**3.** En la elaboración de un proyecto se da la oportunidad de adquirir nuevos conocimientos, nuevas formas de pensar y desarrollar la lógica computacional y de programación, con el fin de poder realizar a futuro, proyectos aún más avanzados y con más eficiencia mayor.

**4.** El algoritmo de ordenamiento utilizado en el presente proyecto (*quicksort*), fue de gran utilidad para la confección del *leaderboard* ya que este algoritmo tiene una complejidad de (n log n), lo cual significa que es muy eficiente para el ordenamiento, en el caso del proyecto, fue eficiente para el ordenamiento de las puntuaciones, esto verificado por la experimentación y prueba de este algoritmo en una asignación del curso Taller de programación.

**5.** La mente de los estudiantes durante la confección de un código debe de permanecer siempre abierta, ser dinámica y adoptando una manera de mantener funcionales sus capacidades de pensamiento lógico y matemático, dentro del cual se reta a la inteligencia a al desarrollo en programación de los estudiantes.



## Recomendaciones

**1.** Para la confección de un proyecto se debe de ser sumamente cuidadoso y organizado con el tiempo y las tareas asignadas a cada uno de los integrantes del grupo, debido a que esto podría traer graves consecuencias a la hora de encontrarse con problemas a días previos a la entrega del programa.

**2.** Cuando se realiza un proyecto es importante tener los objetivos bien definidos ya que, a base de los objetivos, es como se obtiene el producto final, por ende, la definición del cumplimiento de un objetivo del proyecto, el tener metas diarias, las estrategias de confección y la buena planeación, son indispensables para la buena realización de un proyecto. 

**3.** A la hora de realizar un código para un proyecto se debe de tomar en cuenta el utilizar las buenas prácticas de programación, como el uso de nombres claros y precisos para el nombre de variables y funciones.

**4.** Hay que crear un ambiente agradable para los miembros del grupo, ya que los programadores, son la base para realizar el código de manera correcta, por lo tanto, al trabajar en parejas, es necesario que los estudiantes tengan un ambiente amento, en donde puedan desarrollar sus capacidades intelectuales de la mejor manera posible, ya que el ser amable, el celebrar éxitos después de resolver un problema, genera motivación para que se pueda realizar el proyecto de la mejor manera posible.

**5.** El cuidar los detalles tanto en un proyecto de programación, a como en un proyecto de investigación, es indispensable, dado que en los pequeños detalles se encuentra la perfección.

**6.** Al finalizar un proyecto, es de gran ayuda el poder analizarlo, ya que permite ver errores que no se tomatón en cuenta, o bien al revisarlo surgen nuevas ideas para poder implementar algo más en el respectivo proyecto. 
