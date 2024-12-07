import pygame as pg
import os
from settings import *

class SoundManager:
    def __init__(self):
        
        pg.mixer.init()
        self.A = pg.mixer.Sound(sound_dict["Explode"][0])
        self.B = pg.mixer.Sound(sound_dict["Fill"][0])
        self.C = pg.mixer.Sound(sound_dict["End"][0])


    def play_explode_bucket(self):
        sound_chan = pg.mixer.Channel(sound_dict["Explode"][1])
        sound_chan.play(self.A, loops = 0)

    def play_add_sugar(self):
        sound_chan = pg.mixer.Channel(sound_dict["Fill"][1])
        sound_chan.play(self.B, loops = 0)

    def play_level_complete(self):
        sound_chan = pg.mixer.Channel(sound_dict["End"][1])
        sound_chan.play(self.C, loops = 0)

  
