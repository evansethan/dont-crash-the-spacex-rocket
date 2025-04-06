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

    loc1 = pyxel.tilemaps[0].pget(self.playerX // 8, self.playerY // 8)
    loc2 = pyxel.tilemaps[0].pget(-(self.playerX // -8), self.playerY // 8)
    loc3 = pyxel.tilemaps[0].pget(self.playerX // 8, -(self.playerX // -8))
    loc4 = pyxel.tilemaps[0].pget(-(self.playerX // -8), -(self.playerX // -8))

    if loc1[1] == 1 and loc1[0] == 0:
        self.playerX = prev_location[0]
        self.playerY = prev_location[1]
    
    if loc1[1] == 1 and loc1[0] == 1:
        self.playerX = TILE
        self.playerY = TILE

    # if loc2[1] == 1 and loc2[0] == 0:
    #     self.playerX = prev_location[0]
    #     self.playerY = prev_location[1]
    
    # if loc2[1] == 1 and loc2[0] == 1:
    #     self.playerX = TILE
    #     self.playerY = TILE

    # if loc3[1] == 1 and loc3[0] == 0:
    #     self.playerX = prev_location[0]
    #     self.playerY = prev_location[1]
    
    # if loc3[1] == 1 and loc3[0] == 1:
    #     self.playerX = TILE
    #     self.playerY = TILE

    # if loc4[1] == 1 and loc4[0] == 0:
    #     self.playerX = prev_location[0]
    #     self.playerY = prev_location[1]
    
    # if loc4[1] == 1 and loc4[0] == 1:
    #     self.playerX = TILE
    #     self.playerY = TILE

    self.camX = max(self.playerX - SCREEN_WIDTH*1/2, 0)
    self.camY = max(self.playerY - SCREEN_HEIGHT*1/2, 0)
    pyxel.camera(self.camX, self.camY)

  def draw(self):
    # See pyxel documentation for exactly what these are doing and their syntax, but basically we are
    # taking a subset of pixels from res and putting them on the screen at certain coordinates.
    pyxel.bltm(self.camX, self.camY, 0, self.camX, self.camY, SCREEN_WIDTH, SCREEN_HEIGHT) # Render Tilemap
    pyxel.blt(self.playerX, self.playerY, 0, PLAYER_SIZE, 0, PLAYER_SIZE, PLAYER_SIZE, 0) # Render Player Sprite

App()
