import turtle as t
import random as r

def obs(q,w,e):             #사각형(장애물obstacle)을 만드는 함수를 정의
       t.up()
       t.goto(q,w)          #시작 좌표로 거북이 이동
       t.down()
       for x in range(4):   #for  문을 이용하여 사각형 만듬
              t.fd(e)
              t.lt(90)

def horizontal():           #거북이가 사각형에 수평으로 부딪힐때의 함수.
       t.seth(-ang)
def vertical():             #거북이가 사각형에 수직으로 부딪힐 때의 함수.         
       t.seth(180-ang)

t.pensize(5)

obs(-250,-250,500)


t.up()
t.home()
t.shape("circle")

t.seth(r.randint(0,360))    #처음 시작점에서 랜덤으로 원의 방향을 설정
t.fd(1)                     
ang=t.towards(0,0)          #원을 소량 이동시켜서 이동한 각도를 fowards함수를 이용하여 구합니다.

#t.down()
while True:

       t.fd(5)

       if t.xcor()<=-249 or t.xcor()>=249:  #원이 좌벽과, 우벽을 만났을때(수직벽)
              a=t.xcor()                  # 이때의 x좌표와 y좌표를 a,b로 기억합니다.
              b=t.ycor()
              horizontal()                #horizontal함수를 이용해서 원의 방향을 바꿈
              t.fd(1)                     #원을 소량 이동시켜 회전한 각도를 ang에 저장
              ang=t.towards(a,b)
       
       
       if t.ycor()>=249 or t.ycor()<=-249: #원이 천장,바닥과 만났을때(수평벽)
              a=t.xcor()                  #이 때의 x,y좌표 a,b로 기억합니다.
              b=t.ycor()
              
              vertical()                  #vertical함수로 원의 방향을 바꿈
              t.fd(1)                     #원을 소량 이동시켜 회전한 각도를  ang에 저장
              ang=t.towards(a,b)
