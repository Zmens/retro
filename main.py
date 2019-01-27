import pyxel
from retro import start


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        start.print_end()
        pyxel.quit()


def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)


start.print_start()
pyxel.init(160, 120)
pyxel.run(update, draw)

