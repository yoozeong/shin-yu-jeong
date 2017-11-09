import turtle as t
import random as r
t.speed(0)

t.up()
t.goto(-250,-250)
t.down()
for x in range(4):
       t.fd(500)
       t.lt(90)



t.up()

t.goto(0,0)
t.down()
t.shape("turtle")
t.color("white")


te=t.Turtle()
te.up()
te.goto(0,200)
te.down()

te.shape("turtle")
te.color("red")



ts=t.Turtle()
ts.up()
ts.goto(0,-200)
ts.down()
ts.shape("circle")
ts.color("green")

t.bgcolor("orange")


def right():
       t.setheading(0)

def left():
       t.setheading(180)

def up():
       t.setheading(90)
def down():
       t.setheading(270)

def play():

       t.fd(7)
  
              
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.listen()
t.up()

play()

x=True
score=0
while x:
       play()
       te.up()
       ang=te.towards(t.pos())
       te.setheading(ang)
       te.forward(4)
       

       if t.distance(ts)<=10:
              print("먹었다")
              t.write("먹었다")
              score=score+1
              print(score)
              ts_x=r.randint(-240,240)
              ts_y=r.randint(-240,240)
              ts.up()
              ts.goto(ts_x,ts_y)

       if t.distance(te)<=10:
              x=False
              print("잡혔다")
              t.write("game over"+str(score),False,"center",("",20))

