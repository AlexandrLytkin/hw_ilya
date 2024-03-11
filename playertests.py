import unittest
from player import Player
import pygame as pg


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.screen = pg.display.set_mode((500, 500))
        self.pl1 = Player()
        self.FPS = pg.time.Clock()

    # def test_move(self):
    #     self.pl1.move(10, 10)
    #     self.assertEqual(self.pl1.rect.center, (60, 60))
    def test_keyboard_move(self):
        finish = False
        is_gone = False
        while not finish:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finish = True

            if self.pl1.rect.top < 0 or self.pl1.rect.bottom > 500:
                is_gone = True

            self.screen.fill('black')
            self.pl1.keyboard_move()
            self.pl1.update(self.screen)

            self.FPS.tick(60)
            pg.display.update()

        self.assertFalse(is_gone, 'ВЫХОД ЗА ГРАНИЦУ')
