import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.runnig, self. playing = True, False
        self.Up_k, self.Down_k, self.Start_k,self.Back_k = False, False, False, False
        self.width, self.heigth = 500, 600
        self.display = pygame.Surface((self.width, self.heigth))
        self.window = pygame.display.set_mode((self.width, self.heigth))
        self.font = "Vermin Vibes V"
        self.black, self.white = (0,0,0),(255,255,255)

    def loop_game(self):
        while self.playing:
            self.events()
            if self.Start_k:
                self.playing =False
            self.display.fill(self.black)
            self.draw_text("Prueba", 20, self.width/2, self.heigth/2)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runnig, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.Start_k = True
                if event.key == pygame.K_BACKSPACE:
                    self.Back_k = True
                if event.key == pygame.K_DOWN:
                    self.Down_k = True
                if event.key == pygame.K_UP:
                    self.Up_k = True

    def reset(self):
        self.Up_k, self.Down_k, self.Start_k, self.Back_k = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font, size)
        txt_surface = font.render(text,True, self.white)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (x,y)
        self.display.blit(txt_surface, txt_rect)