import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

		# general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Arena')
        self.clock = pygame.time.Clock()
        
        self.windowSurface = pygame.display.set_mode((WIDTH, HEIGTH))
        self.windowSurface.fill((255, 153, 0))
        
        self.imag_bg = pygame.image.load('../graphics/menumain.png')
        self.windowSurface.blit(self.imag_bg, (50, 0))
        pygame.display.update()
        
        self.imag_game_over = pygame.image.load('../graphics/gameover.png')
        self.imag_player_win = pygame.image.load('../graphics/playerwin.png')
    
        self.level = Level()
        self.font = pygame.font.SysFont(None, 48)
        
        self.resultado = -1
        
		# sound 
        main_sound = pygame.mixer.Sound('../audio/music.mp3')
        main_sound.set_volume(0.3)
        main_sound.play(loops = -1)
        
    def show_text(self, text, x, y):
        text_surf = self.font.render(text,False,TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright = (x,y))
        
        pygame.draw.rect(self.windowSurface,UI_BG_COLOR,text_rect.inflate(20,20))
        self.windowSurface.blit(text_surf,text_rect)
        pygame.draw.rect(self.windowSurface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
        pygame.display.update()
    
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def waitForPlayerToPressKey(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Pressing ESC quits.
                        self.terminate()
                    return
         
    def run(self):
        self.show_text('Pressione uma tecla para começar', 900, 600)
        self.waitForPlayerToPressKey()
        
        
        while True:
            self.level.open_game_over = False
            self.level = Level()
            
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            self.level.toggle_menu()
                        
                self.screen.fill(WATER_COLOR)
                
                self.resultado = self.level.run()
                if self.resultado == 2 or self.resultado == 1:
                    break
                
                pygame.display.update()
                self.clock.tick(FPS)
                
            if self.resultado == 2: #player morreu    
                self.windowSurface.blit(self.imag_game_over, (-200, 0))
                self.show_text('Pressione uma tecla para reiniciar', 900, 550)
            elif self.resultado == 1: #win
                self.windowSurface.blit(self.imag_player_win, (30, 0))
                self.show_text('Pressione uma tecla para jogar novamente', 980, 600)
                
            self.waitForPlayerToPressKey()
            pygame.display.update()
    
if __name__ == '__main__':
	game = Game()
	game.run()