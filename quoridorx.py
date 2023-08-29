"""caca"""
import turtle
from quoridor import Quoridor

class QuoridorX(Quoridor):
    """caca"""
    def __init__(self,*args):
        """on passe toujours les memes arguments etat[joeur] and etat[murs]"""
        """on cree un ecran avec sturtle"""
        """self.type et self.pos sont des variable qui sont utilise en bas pour tenir des elements tempoiraiment"""
        super().__init__(*args) 
        self.screen=turtle.Screen()
        self.type = ''
        self.pos = []
        self.ok=False
    def afficher(self):
        """caca"""
        """On commence par montre au joeur l'etat quand il joue"""
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
        """l'instance t du turtle.turtle est utilise pour ecrire sur l'ecran"""
        """et puis screen.update() pour reflechir l'ecran"""
        """self.joueur1 est cree et lier a un joueur le meme cas pour self.joueur2 pour le deuxieme joueur """
        """et self.murs pour touts les murs  """

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
        self.joueur1=turtle.Turtle()
        self.joueur1.showturtle()
        self.joueur1.shapesize(2,2)
        self.joueur1.penup()
        self.joueur1.shape('circle')
        self.joueur1.fillcolor('green')
        self.joueur1.goto(-175+(self.état['joueurs'][0]['pos'][0]-1)*50,-225+(self.état['joueurs'][0]['pos'][1]-1)*50)
        self.joueur2=turtle.Turtle()
        self.joueur2.showturtle()
        self.joueur2.shapesize(2,2)
        self.joueur2.penup()
        self.joueur2.goto(-175+(self.état['joueurs'][1]['pos'][0]-1)*50,-225+(self.état['joueurs'][1]['pos'][1]-1)*50)
        self.joueur2.shape('circle')
        self.joueur2.fillcolor('red')
        self.joueur2.begin_fill()
        self.joueur2.end_fill()
        self.screen.update()   
        self.murs=turtle.Turtle()
        self.murs.hideturtle()
        self.murs.pensize(4)
        for bn in list(self.état["murs"]["horizontaux"]):
            self.murs.color("blue")
            self.murs.penup()
            self.murs.goto(-250+(bn[0])*50,-300+(bn[1])*50)
            self.murs.pendown()
            self.murs.forward(100)
            self.murs.penup()
        for mn in list(self.état["murs"]["verticaux"]):
            self.murs.color("green")
            self.murs.setheading(90)
            self.murs.penup()
            self.murs.goto(-250+(mn[0])*50,-300+(mn[1])*50)
            self.murs.pendown()
            self.murs.forward(100)
            self.murs.penup()
        def click(x,y):
            """onclick for walls"""
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
                    self.murs.setheading(90)
                    self.murs.color('blue')
                    self.murs.penup()
                    self.murs.goto(vb,mb)
                    self.murs.pendown()
                    self.murs.forward(100)
                    self.murs.penup()
                    self.type="MV"
                    v = [int((vb + 175) // 50)+2, int((mb+ 225) // 50)+2]
                    self.pos=v
                    self.placer_un_mur(1, self.pos, 'vertical')
                else:
                    self.murs.setheading(0)
                    self.murs.color('black')
                    self.murs.penup()
                    self.murs.goto(vb,mb)
                    self.murs.pendown()
                    self.murs.forward(100)
                    self.murs.penup()
                    self.type="MH"
                    v = [int((vb + 175) // 50)+2 , int((mb+ 225) // 50)+2]
                    self.pos=v
                    self.placer_un_mur(1, self.pos, 'horizontal')
                
        self.screen.onclick(click,btn=1)
        self.screen.listen()
        def dv():
            """On keypress for players so that you can play on the screen"""
            
            o, x = list(self.joueur1.pos())
            v = [((o + 175) // 50) + 1, ((x + 225) // 50)]
            bum = list(self.état["murs"]["horizontaux"])
            if v not in bum:
                self.déplacer_jeton(1, v)
                self.joueur1.setheading(270)
                self.joueur1.forward(50)
                self.type = "D"
                self.pos = v
                self.ok = True
                self.screen.update() 
       
        self.screen.onkeypress(dv, 'Down')
       
    def effacer(self):
        """Each time a move is made we need to refresh"""
        self.screen.clear()
    def demander_coup(self):
        """on keypress for player to play on screen"""
        tt=True
        
        def dv(ok):
            """on keypress for player to play on screen"""
            if ok is True:
                o, x = list(self.joueur1.pos())
                v = [((o + 175) // 50) + 1, ((x + 225) // 50) + 2]
                bum = list(self.état["murs"]["horizontaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.joueur1.setheading(90)
                    self.joueur1.forward(50)
                    self.type = "D"
                    self.pos = v
                    self.ok = True
                    self.screen.update() 
            else:
                tt=False
                
        self.screen.onkeypress(lambda: dv(tt), 'Up')
        def dd(ok):
            if ok is True:
                o,x=self.joueur1.pos()
                v=[((o+175)//50)+2,((x+225)//50)+1]
                bum=list(self.état["murs"]["verticaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.joueur1.setheading(0)
                    self.joueur1.forward(50)
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
                o,x=list(self.joueur1.pos())
                v=[((o+175)//50),((x+225)//50)+1]
                bum=list(self.état["murs"]["verticaux"])
                if v not in bum:
                    self.déplacer_jeton(1, v)
                    self.joueur1.setheading(180)
                    self.joueur1.forward(50)
                    self.type="D"
                    self.pos  =v
                    self.ok=True
            else:
                tt=False
        self.screen.onkeypress(lambda:db(tt), 'Left')
        self.screen.listen()

        


        
        
