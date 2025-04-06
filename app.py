import pyxel, random

STARTX = 55
STARTY = 105

class App:

    def __init__(self):
        pyxel.init(128,128,title="Don't Crash The SpaceX Rocket")
        self.rocket_x = STARTX
        self.rocket_y = STARTY
        self.obstacle_list = [] # need gas/coin list
        self.counter = 0 # turn into gas tank?
        self.distance = 0
        self.highscore = 0
        self.obstacle_freq = 35.0
        self.gas = 100

        pyxel.load("res.pyxres")
        pyxel.run(self.update,self.draw)


    def reset(self):
        self.rocket_x = STARTX
        self.rocket_y = STARTY
        self.distance = 0
        self.gas = 100


    def move_rocket(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (self.rocket_x+16 < 120):                                 
                self.rocket_x+=1
        if pyxel.btn(pyxel.KEY_LEFT):
            if (self.rocket_x > 8):          
                self.rocket_x-=1
        if pyxel.btn(pyxel.KEY_DOWN):
            if (self.rocket_y+20 < 128):
                self.rocket_y+=1
        if pyxel.btn(pyxel.KEY_UP):
            if (self.rocket_y > 0):
                self.rocket_y-=1

        if self.gas <= 0:
            self.reset()
            # explosion, out of gas
    

    def obstacles(self):

        # if self.distance % 5 == 0:
        #     self.obstacle_freq -= 5

        if (pyxel.frame_count % self.obstacle_freq == 0): # rate of new obstacles increases?
            self.obstacle_list.append([random.randint(8, 100),-10])

        
        for obstacle in self.obstacle_list:
            obstacle[1] += 1
            if  obstacle[1]>128:
                self.obstacle_list.remove(obstacle)
         
           
        for obstacle in self.obstacle_list:
            if obstacle[0] <= self.rocket_x+16 and obstacle[1] <= self.rocket_y+20 and obstacle[0]+20 >= self.rocket_x and obstacle[1] >= self.rocket_y:
                self.reset()
                self.obstacle_list.remove(obstacle)
                # show explosion, reset
    
        
    def update(self):
        if (pyxel.frame_count % 10 == 0):
            self.distance += 1
            self.gas -= 1
            if self.distance > self.highscore:
                self.highscore = self.distance
        self.move_rocket()
        self.obstacles()
        

    def draw(self):  
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,192- pyxel.frame_count % 192,128,128)
        pyxel.blt(self.rocket_x,self.rocket_y,0,0,8,16,20,2)
    
        for obstacle in self.obstacle_list:
            pyxel.blt(obstacle[0], obstacle[1],0,0,32,20,16,1) 
        
        pyxel.text(0,5, 'distance:'+ str(self.distance), 5)
        pyxel.text(47,5, 'gas:'+  str(self.gas),9)
        pyxel.text(78,5, 'high score:'+  str(self.highscore),8)
        
    
App()