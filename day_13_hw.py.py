import turtle as t
import random as r

def rec(q,w,e):
       t.up()
       t.goto(q,w)
       t.down()
       for x in range(4):
              t.fd(e)
              t.lt(90)

def lrwall():
       t.seth(-ang)
def tbwall():
       t.seth(180-ang)
t.pensize(5)
rec(-250,-250,500)


t.up()
t.home()
t.shape("circle")

t.seth(r.randint(0,360))
t.fd(5)
x=t.xcor()
y=t.ycor()
ang=t.towards(0,0)
#t.down()
while True:

       t.fd(5)

       if t.xcor()<=-249 or t.xcor()>=249: 
              a=t.xcor()
              b=t.ycor()
              lrwall()
              t.fd(1)
              x=t.xcor()
              y=t.ycor()
              ang=t.towards(a,b)
       
       
       if t.ycor()>=249 or t.ycor()<=-249:
              a=t.xcor()
              b=t.ycor()
              
              tbwall()
              t.fd(1)
              x=t.xcor()
              y=t.ycor()
              ang=t.towards(a,b)
