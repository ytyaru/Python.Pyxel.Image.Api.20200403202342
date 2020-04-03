#!/usr/bin/env python3
# coding: utf8
import pyxel
class App:
    def __init__(self):
        self.window = Window()
        pyxel.init(self.window.Width, self.window.Height, caption=self.window.Caption)
        self.niko = Niko()
        self.niko.set_center(self.window.Width, self.window.Height)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.niko.update()
    def draw(self):
        pyxel.cls(0)
        self.niko.draw()
        pyxel.text(0, 0, 'Please SPACE key: ' + str(self.niko.color), 7)
class Window:
    @property
    def Width(self): return 96
    @property
    def Height(self): return 54
    @property
    def Caption(self): return "Image API"
class Niko:
    def __init__(self):
        self.__set_image0()
    def __set_image0(self):
        self.x = 0
        self.y = 0
        self.img = 0
        self.u = 0
        self.v = 0
        self.w = 16
        self.h = 16
        self.colkey = 0
        self.color = 7
        pyxel.image(0).set(0, 0, [
            "0000077777700000",
            "0007700000077000",
            "0070000000000700",
            "0700000000000070",
            "0700000000000070",
            "7000070000700007",
            "7000070000700007",
            "7000000000000007",
            "7000000000000007",
            "7000000000000007",
            "7000700000070007",
            "0700070000700070",
            "0700007777000070",
            "0070000000000700",
            "0007700000077000",
            "0000077777700000",
        ])
    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.__change_color()
    def draw(self):
        pyxel.pal(7, self.color)
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)
        pyxel.pal()
    def __change_color(self):
        self.color += 1
        if 15 <= self.color: self.color = 1
    def set_center(self, win_w, win_h):
        self.x = (win_w / 2) - (self.w / 2)
        self.y = (win_h / 2) - (self.h / 2)

App()
