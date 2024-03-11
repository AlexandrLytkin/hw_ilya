import pygame as pg
import logging
import datetime

# TODO ДЗ: Как через функцию basicConfig назначить для каждого лога (уровня) отдельный хэндлер.

logger = logging.getLogger(__name__)

logger_handler_1 = logging.FileHandler(
    filename=f'Move {datetime.datetime.now().strftime("%Y-%m")}.log',
    mode='w',
    encoding='utf-8'
)
logger_handler_2 = logging.FileHandler(
    filename=f'Move {datetime.datetime.now().strftime("%m-%d %H")}.log',
    mode='w',
    encoding='utf-8'
)
logger.addHandler(logger_handler_1)
logger.addHandler(logger_handler_2)
logger_handler_1.setLevel(logging.INFO)
logger_handler_2.setLevel(logging.DEBUG)

logging.basicConfig(
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt="%d/%m/%Y %I/%M/%S",
                    level=logging.DEBUG,
                    handlers=[logger_handler_1, logger_handler_2],
                    encoding='utf-8'
                    )


class Player:
    def __init__(self):
        self.image = pg.Surface((100, 100))
        self.image.fill('red')
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def keyboard_move(self):
        key = pg.key.get_pressed()
        if key[pg.K_UP]:
            self.rect.y -= 1
            logging.info(f'Передвижение вверх, текущие координаты {self.rect.center}')
        if key[pg.K_DOWN]:
            self.rect.y += 1
            logging.debug(f'Передвижение вниз, текущие координаты {self.rect.center}')

    def update(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)


if __name__ == '__main__':
    screen = pg.display.set_mode((500, 500))
    pl1 = Player()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        pl1.update(screen)
        pg.display.update()
