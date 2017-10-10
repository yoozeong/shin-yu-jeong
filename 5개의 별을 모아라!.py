print("5개의 별을 모으는 재미있는 덧셈게임")
print("5개의 문제를 맞춰서 별 5개를 모아보세요")

import turtle as t
import random as r

t.bgcolor("black")                  #배경색을 black 으로 지정
t.color("yellow")                   #선의 색을  yellow 로 지정

ct=0
    
for x in range(10):                 #10번 반복
    t.begin_fill()                  #색칠할 영역 시작
    a=r.randint(1,30)               #a에 1~30 사이의 임의의 수를 저장
    b=r.randint(1,30)               #b에 1~30 사이에 임의의 수를 저장
    c=a+b
    print(a,"+",b,"=")              #문제를 출력
    x=input()                       #답을 입력받아 x에 저장(문자열로 저장됨)
    d=int(x)                        #비교를 위해 문자열을 정수로 바꿈

    if c==d:                        #비교 결과가 같다면 반복을 통한 별 그림을 그리기 시작
        for x in range(6):          #별 모양을 만들기 위해6번 반복(다음 별의 시작점을 위해서6번으로 설정했어요)
            t.fd(100)               #100만큼 앞으로 이동
            t.rt(144)               #144도 오른쪽으로 회전(별의 내각이 36도라서)
        t.lt(144+360/5)             #다음별이 그려질 때의 각도를 위해서 각도를 옮겨줬어요
        t.end_fill()                #색칠할 영역을 마무리
        ct=ct+1                     #정답을 맞출 시 별의 갯수를 하나씩 증가시킴

        print("총 별",ct,"개 획득")

    if c!=d:                        #비교결과가 같지 않다면 "오답"이라고 표시.
        print("오답")

    if ct==5:                       #5개의 별이 생성되면 반복을 멈춤.
        break
        print("Congratulation!!!!!!!!!!")   #축하메시지 전달 후 게임 종료

else:
    print("다음기회에...")               #10번안에 5개의 별을 모으지못할시.

