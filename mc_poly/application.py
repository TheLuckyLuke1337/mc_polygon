import pygame as p

from .mapgen import map_gen

from .config import RESOLUTION, CONCRETE, BEDROCK, SQUARES, SAMPLING


class Application:
    def __init__(self, n, L):
        p.init()
        L = L - 1
        self.__load_images()
        self.__map = map_gen(n, L)
        self.__clock = p.time.Clock()

    def __load_images(self):
        size = (RESOLUTION, RESOLUTION)
        self.concrete = p.image.load(CONCRETE)
        self.concrete = p.transform.scale(self.concrete, size)
        self.bedrock = p.image.load(BEDROCK)
        self.bedrock = p.transform.scale(self.bedrock, size)

    def run(self):
        self.__clock.tick(60)
        self.__running = True
        self.screen = p.display.set_mode(
            (len(self.__map[0])*RESOLUTION,
             len(self.__map)*RESOLUTION)
        )
        while self.__running:
            self.screen.fill((0, 0, 0))
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.__running = False
            self.draw_map()
            p.display.flip()

    def draw_map(self):
        for i, row in enumerate(self.__map):
            for j, block in enumerate(row):
                destination = (j*RESOLUTION, i*RESOLUTION)
                if block:
                    self.screen.blit(self.concrete, destination)
                else:
                    self.screen.blit(self.bedrock, destination)
