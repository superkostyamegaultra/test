import sys, pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AllienInvasion:

    def __init__(self): #функция инициализации окна игры и подключения ресурсов
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Aliens Invasion")

        self.ship = Ship(self)


    def run_game(self): #запуск основного цикла игры
        while True:
            #Отслеживание действий клавиатуры и мыши ..?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AllienInvasion()
    ai.run_game()















