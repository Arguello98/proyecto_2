import pygame

class Menu():
    def __init__(self, Game):
        self.game = Game
        self.center_w, self.center_h = self.game.width/2, self.game.heigth/2
        self.run = True
        self.cursor  = pygame.Rect(0,0,20,20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor, self.cursor.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset()

class MainMenu(Menu):
    def __init__(self, Game):
        Menu.__init__(self, Game)
        self.state = "Start"
        self.startx, self.starty = self.center_w, self.center_h + 30
        self.instructionsx, self.instructionsy = self.center_w, self.center_h + 50
        self.creditsx, self.creditsy= self.center_w, self.center_h + 704
        self.cursor.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.events()
            self.game.display.fill(self.game.black)
            self.game.draw_text("Menu", 20, self.game.width/2, self.game.heigth/2 -20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Instructions", 20, self.instructionsx, self.instructionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()

    def move_cursor(self):
        if self.game.Down_k:
            if self.state == "Start Game":
                self.cursor.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = "Instructions"
            elif self.state == "Instructions":
                self.cursor.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Instructions"
            elif self.state == "Credits":
                self.cursor.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start Game"
        elif self.game.Up_k:
            if self.state == "Start Game":
                self.cursor.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Instructions":
                self.cursor.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start Game"
            elif self.state == "Credits":
                self.cursor.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = "Instructions"

