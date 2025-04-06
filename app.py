import pyxel, random

STARTX = 55
STARTY = 105

class App:

    def __init__(self):
        pyxel.init(128,128,title="Don't Crash The SpaceX Rocket")
        self.rocket_x = STARTX
        self.rocket_y = STARTY
        self.obstacle_list = [] # need gas/coin list
        #self.counter = 0 # turn into gas tank?
        self.score = 0
        self.record = 0
        self.obstacle_freq = 45.0
        self.gas = 100
        self.tank_list = []

        pyxel.load("res.pyxres")
        pyxel.run(self.update,self.draw)


    def reset(self):
        self.rocket_x = STARTX
        self.rocket_y = STARTY
        self.score = 0
        self.gas = 100


    def move_rocket(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (self.rocket_x+16 < 120):                                 
                self.rocket_x+=2
        if pyxel.btn(pyxel.KEY_LEFT):
            if (self.rocket_x > 8):          
                self.rocket_x-=2
        if pyxel.btn(pyxel.KEY_DOWN):
            if (self.rocket_y+20 < 128):
                self.rocket_y+=2
        if pyxel.btn(pyxel.KEY_UP):
            if (self.rocket_y > 0):
                self.rocket_y-=2

        if self.gas <= 0:
            self.reset()
            # explosion, out of gas
    

    def obstacles(self):

        if (pyxel.frame_count % self.obstacle_freq == 0):
            self.obstacle_list.append([random.randint(8, 100),-10])

        for obstacle in self.obstacle_list:
            obstacle[1] += -(self.score // -100) # speed up obstacles as score increases
            if  obstacle[1]>128:
                self.obstacle_list.remove(obstacle)
         
        for obstacle in self.obstacle_list:
            if obstacle[0] <= self.rocket_x+16 and obstacle[1] <= self.rocket_y+20 and obstacle[0]+20 >= self.rocket_x and obstacle[1] >= self.rocket_y:
                self.reset()
                self.obstacle_list.remove(obstacle)
                # show explosion, reset


    def gas_tanks(self):

        if (pyxel.frame_count % 400 == 0): 
            self.tank_list.append([random.randint(8, 100),-10])
        
        for tank in self.tank_list:
            tank[1] += 1
            if  tank[1]>128:
                self.tank_list.remove(tank)
             
        for tank in self.tank_list:
            if tank[0] <= self.rocket_x+16 and tank[1] <= self.rocket_y+20 and tank[0]+20 >= self.rocket_x and tank[1] >= self.rocket_y:
                self.gas = 100
                self.tank_list.remove(tank)
    
        
    def update(self):
        if (pyxel.frame_count % 10 == 0):
            self.score += 1
            self.gas -= 1
            if self.score > self.record:
                self.record = self.score
        self.move_rocket()
        self.obstacles()
        self.gas_tanks()
        

    def draw(self):  
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,192- pyxel.frame_count % 192,128,128)
        pyxel.blt(self.rocket_x,self.rocket_y,0,0,8,16,20,2)
    
        for obstacle in self.obstacle_list:
            pyxel.blt(obstacle[0], obstacle[1],0,0,32,20,16,1) 
        
        for tank in self.tank_list:
            pyxel.blt(tank[0], tank[1],0,16,8,16,20,2) 
        
        pyxel.text(2,5, 'score:'+ str(self.score), 5)
        pyxel.text(45,5, 'gas:'+  str(self.gas),9)
        pyxel.text(80,5, 'record:'+  str(self.record),8)
        
    
App()