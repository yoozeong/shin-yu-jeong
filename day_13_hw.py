import turtle as t
import random as r

def horizontal():           #원이 사각형에 수평으로 부딪힐때의 함수.
       t.seth(-ang)

def vertical():             #원이 사각형에 수직으로 부딪힐 때의 함수.         
       t.seth(180-ang)

t.pensize(5)                #펜 굵기 5로 설정

t.up()                      #원이 움직일 사각형 그리기.
t.goto(-250,-250)
t.down()
for x in range(4):
       t.fd(500)
       t.lt(90)

t.up()                      # 거북이를 원점으로 보내고 써클 모양으로 만듬.
t.home()
t.shape("circle")

t.seth(r.randint(0,360))    #처음 시작점에서 랜덤으로 원의 방향을 설정

t.fd(1)                     #원을 소량 이동시켜서 이동한 각도를 fowards함수를 이용하여 구합니다.           
ang=t.towards(0,0)          

#t.down()
while True:                 #계속해서 원을 5씩 움직임

       t.fd(5)

       if t.xcor()<=-250 or t.xcor()>=250:  #원이 좌벽과, 우벽을 만났을때(수직벽)
              a=t.xcor()                  # 이때의 x좌표와 y좌표를 a,b로 기억합니다.
              b=t.ycor()
              horizontal()                #horizontal함수를 이용해서 원의 방향을 바꿈
              t.fd(1)                     #원을 소량 앞으로 이동시켜 회전한 각도를 ang에 저장
              ang=t.towards(a,b)
       
       
       if t.ycor()>=250 or t.ycor()<=-250: #원이 천장,바닥과 만났을때(수평벽)
              a=t.xcor()                  #이 때의 x,y좌표 a,b로 기억합니다.
              b=t.ycor()
              
              vertical()                  #vertical함수로 원의 방향을 바꿈
              t.fd(1)                     #원을 소량앞으로  이동시켜 회전한 각도를  ang에 저장
              ang=t.towards(a,b)
