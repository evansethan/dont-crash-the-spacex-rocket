import pyxel

# Constants
TILE = 8
SCREEN_WIDTH = TILE * 8
SCREEN_HEIGHT = TILE * 8
PLAYER_SIZE = 8


class App():
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Cute Lil Game", fps=30)
        pyxel.load("res.pyxres") # Load our resource file
        self.playerX = TILE # Initial pixel position of player, feel free to change
        self.playerY = TILE
        self.camX = 0 # Leftmost topmost pixel shown on screen
        self.camY = 0
        # Add more variables here
        pyxel.playm(0, loop=True) # Music
        pyxel.run(self.update, self.draw) # Run the game!



    def update(self):

        prev_location = self.playerX, self.playerY

        if pyxel.btn(pyxel.KEY_LEFT):
            self.playerX -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.playerX += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.playerY -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.playerY += 1


    def draw(self):
        # See pyxel documentation for exactly what these are doing and their syntax, but basically we are
        # taking a subset of pixels from res and putting them on the screen at certain coordinates.
        pyxel.bltm(self.camX, self.camY, 0, self.camX, self.camY, SCREEN_WIDTH, SCREEN_HEIGHT) # Render Tilemap
        pyxel.blt(self.playerX, self.playerY, 0, PLAYER_SIZE, 0, PLAYER_SIZE, PLAYER_SIZE, 0) # Render Player Sprite

App()
