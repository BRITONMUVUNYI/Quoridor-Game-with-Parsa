"""caca"""
import turtle
from quoridor import Quoridor

class QuoridorX(Quoridor):
    """caca"""
    def __init__(self,*args):
        """caca"""
        super().__init__(*args)
        self.screen=turtle.Screen()
        self.type = ''
        self.pos = []
        self.ok=False
    def afficher(self):
        """caca"""
        p=''
        le = ""
        gk = len(self.état['joueurs'][0]["nom"])
        hk = len(self.état["joueurs"][1]["nom"])
        ss = [hk, gk]
        joueur1 = self.état['joueurs'][0]['nom']
        joueur2 = self.état['joueurs'][1]['nom']
        murs1 = self.état['joueurs'][0]['murs']
        murs2 = self.état['joueurs'][1]['murs']
        légende = "Légende:\n"
        légende_fin = ''
        ligne1 = '   ' + '1=' + joueur1 + ',' + ' ' + 'murs=' + ' |'*murs1 + '\n'
        figne1 = '   ' + '2=' + joueur2 + ',' + ' ' * (len(joueur1) - len(joueur2)) + ' ' + 'murs=' + ' |'*murs2 +'\n'
        ligne2 = '   ' + '1=' + joueur1 + ',' + ' ' * (len(joueur2) - len(joueur1)) + ' ' + 'murs=' + ' |'*murs1 + '\n'
        figne2 = '   ' + '2=' + joueur2 + ',' + ' ' + 'murs=' + ' |'*murs2 +'\n'
        if len(joueur1) >= len(joueur2):
            légende_fin = légende + ligne1 + figne1
        else:
            légende_fin = légende + ligne2 + figne2
        t = turtle.Turtle()
        self.screen.bgcolor('yellow')
        t.speed(20)
        t.hideturtle()
        t.penup()
        t.goto(-200,200)
        t.color('blue')
        t.clear()
        t.write(légende_fin.upper(),align="left",font=15)
        self.screen.update()
        t.goto(-200,-250)
        t.color("black")
        for n,i in enumerate(range(0,10)):
            t.pendown()
            t.forward(450)
            t.penup()
            t.goto(-200,-200+(50*n))
        t.setheading(90)
        t.goto(-200,-250)
        for n, i in enumerate(range(1,12)):
            t.pendown()
            t.forward(450)
            t.penup()
            t.goto(-200+(50*n),-250)
        t.goto(-220,-230)
        for i in range(1,10):
            t.write(i,font=20)
            t.goto(-220,-230+(50*i))
        t.setheading(90)
        t.hideturtle()
        t.goto(-175,-280)
        for i in range(1,10):
            t.write(i,font=20)
            t.goto(-175+(50*i),-280)
        self.tim=turtle.Turtle()
        self.tim.showturtle()
        self.tim.shapesize(2,2)
        self.tim.penup()
        self.tim.shape('circle')
        self.tim.fillcolor('green')
        self.tim.goto(-175+(self.état['joueurs'][0]['pos'][0]-1)*50,-225+(self.état['joueurs'][0]['pos'][1]-1)*50)
        self.ti=turtle.Turtle()
        self.ti.showturtle()
        self.ti.shapesize(2,2)
        self.ti.penup()
        self.ti.goto(-175+(self.état['joueurs'][1]['pos'][0]-1)*50,-225+(self.état['joueurs'][1]['pos'][1]-1)*50)
        self.ti.shape('circle')
        self.ti.fillcolor('red')
        self.ti.begin_fill()
        self.ti.end_fill()
        self.screen.update()   
        self.tom=turtle.Turtle()
        self.tom.hideturtle()
        self.tom.pensize(4)
        for bn in list(self.état["murs"]["horizontaux"]):
            self.tom.color("blue")
            self.tom.penup()
            self.tom.goto(-250+(bn[0])*50,-300+(bn[1])*50)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.penup()
        for mn in list(self.état["murs"]["verticaux"]):
            self.tom.color("green")
            self.tom.setheading(90)
            self.tom.penup()
            self.tom.goto(-250+(mn[0])*50,-300+(mn[1])*50)
            self.tom.pendown()
            self.tom.forward(100)
            self.tom.penup()
        def click(x,y):
            """caca"""
            if abs(x)<250 and  abs(y)<200:
                gg=[x for x in range(-200,300,50)]
                dis=0
                mb=0
                b=0
                vb=0
                vi=x
                bb=y
                dis = abs(vi - gg[0])
                vb = gg[0]
                for v in gg:
                    b = abs(vi - v)
                    if b < dis:
                        dis = b
                        vb = v
                dvs = abs(bb - gg[0])
                mb = gg[0]
                for v in gg:
                    b = abs(bb - v)
                    if b < dvs:
                        dvs = b
                        mb = v
                if dis<dvs:
                    self.tom.setheading(90)
                    self.tom.color('blue')
                    self.tom.penup()
                    self.tom.goto(vb,mb)
                    self.tom.pendown()
                    self.tom.forward(100)
                    self.tom.penup()
                    self.type="MV"
                    v = [int((vb + 175) // 50)+2, int((mb+ 225) // 50)+2]
                    self.pos=v
                    self.placer_un_mur(1, self.pos, 'vertical')
                else:
                    self.tom.setheading(0)
                    self.tom.color('black')
                    self.tom.penup()
                    self.tom.goto(vb,mb)
                    self.tom.pendown()
                    self.tom.forward(100)
                    self.tom.penup()
                    self.type="MH"
                    v = [int((vb + 175) // 50)+2 , int((mb+ 225) // 50)+2]
                    print(v)
                    self.pos=v
                    self.placer_un_mur(1, self.pos, 'horizontal')
                
        self.screen.onclick(click,btn=1)
        self.screen.listen()
        def dv():
            """caca"""
            
            o, x = list(self.tim.pos())
            v = [((o + 175) // 50) + 1, ((x + 225) // 50)]
            bum = list(self.état["murs"]["horizontaux"])
            if v not in bum:
                self.déplacer_jeton(1, v)
                self.tim.setheading(270)
                self.tim.forward(50)
                self.type = "D"
                self.pos = v
                self.ok = True
                self.screen.update() 
       
        self.screen.onkeypress(dv, 'Down')
       
    def effacer(self):
        """caca"""
    
        self.screen.clear()
    def demander_coup(self):
        tt=True
        
        def dv(ok):
            """caca"""
            if ok is True:
                o, x = list(self.tim.pos())
                v = [((o + 175) // 50) + 1, ((x + 225) // 50) + 2]
                bum = list(self.état["murs"]["horizontaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.tim.setheading(90)
                    self.tim.forward(50)
                    self.type = "D"
                    self.pos = v
                    self.ok = True
                    self.screen.update() 
            else:
                tt=False
                
        self.screen.onkeypress(lambda: dv(tt), 'Up')
        def dd(ok):
            if ok is True:
                o,x=self.tim.pos()
                v=[((o+175)//50)+2,((x+225)//50)+1]
                bum=list(self.état["murs"]["verticaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.tim.setheading(0)
                    self.tim.forward(50)
                    self.type = "D"
                    self.pos = v
                    self.ok=True
                    self.screen.update() 
            else:
                 tt=False
                 self
        self.screen.onkeypress(lambda:dd(tt), 'Right')
        def db(ok):
            """caca"""
            if ok is True:
                o,x=list(self.tim.pos())
                v=[((o+175)//50),((x+225)//50)+1]
                bum=list(self.état["murs"]["verticaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.tim.setheading(180)
                    self.tim.forward(50)
                    self.type="D"
                    self.pos  =v
                    self.ok=True
            else:
                tt=False
        self.screen.onkeypress(lambda:db(tt), 'Left')
        self.screen.listen()

        


        
        
