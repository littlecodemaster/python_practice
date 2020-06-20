from graphics import *
print("Do you two want to play a tic tac toc game on this computer?")
if input()=="yes" or input()=="Yes":
    win3=GraphWin("tictactoc", 900, 900)
    myline=Line(Point(300.0, 300.0), Point(300.0, 600.0))
    myline.draw(win3)
    myline=Line(Point(400.0, 300.0), Point(400.0, 600.0))
    myline.draw(win3)
    myline=Line(Point(500.0, 300.0), Point(500.0, 600.0))
    myline.draw(win3)
    myline=Line(Point(600.0, 300.0), Point(600.0, 600.0))
    myline.draw(win3)
    myline=Line(Point(300.0, 300.0), Point(600.0, 300.0))
    myline.draw(win3)
    myline=Line(Point(300.0, 400.0), Point(600.0, 400.0))
    myline.draw(win3)
    myline=Line(Point(300.0, 500.0), Point(600.0, 500.0))
    myline.draw(win3)
    myline=Line(Point(300.0, 600.0), Point(600.0, 600.0))
    myline.draw(win3)
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    print("Then let's play!")
    j=int(input())
    if j==1:
        mycircle=Circle(Point(350.0, 350.0), 50)
        mycircle.draw(win3)
        a=1
    if j==2:
        mycircle=Circle(Point(450.0, 350.0), 50)
        mycircle.draw(win3)
        a=2
    if j==3:
        mycircle=Circle(Point(550.0, 350.0), 50)
        mycircle.draw(win3)
        a=3
    if j==4:
        mycircle=Circle(Point(350.0, 450.0), 50)
        mycircle.draw(win3)
        a=4
    if j==5:
        mycircle=Circle(Point(450.0, 450.0), 50)
        mycircle.draw(win3)
        a=5
    if j==6:
        mycircle=Circle(Point(550.0, 450.0), 50)
        mycircle.draw(win3)
        a=6
    if j==7:
        mycircle=Circle(Point(350.0, 550.0), 50)
        mycircle.draw(win3)
        a=7
    if j==8:
        mycircle=Circle(Point(450.0, 550.0), 50)
        mycircle.draw(win3)
        a=8
    if j==9:
        mycircle=Circle(Point(550.0, 550.0), 50)
        mycircle.draw(win3)
        a=9
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not j==a:
            if j==1:
                mynewcircle=Circle(Point(350.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=1
            if j==2:
                mynewcircle=Circle(Point(450.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=2
            if j==3:
                mynewcircle=Circle(Point(550.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=3
            if j==4:
                mynewcircle=Circle(Point(350.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=4
            if j==5:
                mynewcircle=Circle(Point(450.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=5
            if j==6:
                mynewcircle=Circle(Point(550.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=6
            if j==7:
                mynewcircle=Circle(Point(350.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=7
            if j==8:
                mynewcircle=Circle(Point(450.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=8
            if j==9:
                mynewcircle=Circle(Point(550.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                b=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b):
            if j==1:
                mycircle=Circle(Point(350.0, 350.0), 50)
                mycircle.draw(win3)
                c=1
            if j==2:
                mycircle=Circle(Point(450.0, 350.0), 50)
                mycircle.draw(win3)
                c=2
            if j==3:
                mycircle=Circle(Point(550.0, 350.0), 50)
                mycircle.draw(win3)
                c=3
            if j==4:
                mycircle=Circle(Point(350.0, 450.0), 50)
                mycircle.draw(win3)
                c=4
            if j==5:
                mycircle=Circle(Point(450.0, 450.0), 50)
                mycircle.draw(win3)
                c=5
            if j==6:
                mycircle=Circle(Point(550.0, 450.0), 50)
                mycircle.draw(win3)
                c=6
            if j==7:
                mycircle=Circle(Point(350.0, 550.0), 50)
                mycircle.draw(win3)
                c=7
            if j==8:
                mycircle=Circle(Point(450.0, 550.0), 50)
                mycircle.draw(win3)
                c=8
            if j==9:
                mycircle=Circle(Point(550.0, 550.0), 50)
                mycircle.draw(win3)
                c=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c):
            if j==1:
                mynewcircle=Circle(Point(350.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=1
            if j==2:
                mynewcircle=Circle(Point(450.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=2
            if j==3:
                mynewcircle=Circle(Point(550.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=3
            if j==4:
                mynewcircle=Circle(Point(350.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=4
            if j==5:
                mynewcircle=Circle(Point(450.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=5
            if j==6:
                mynewcircle=Circle(Point(550.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=6
            if j==7:
                mynewcircle=Circle(Point(350.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=7
            if j==8:
                mynewcircle=Circle(Point(450.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=8
            if j==9:
                mynewcircle=Circle(Point(550.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                d=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d):
            if j==1:
                mycircle=Circle(Point(350.0, 350.0), 50)
                mycircle.draw(win3)
                e=1
            if j==2:
                mycircle=Circle(Point(450.0, 350.0), 50)
                mycircle.draw(win3)
                e=2
            if j==3:
                mycircle=Circle(Point(550.0, 350.0), 50)
                mycircle.draw(win3)
                e=3
            if j==4:
                mycircle=Circle(Point(350.0, 450.0), 50)
                mycircle.draw(win3)
                e=4
            if j==5:
                mycircle=Circle(Point(450.0, 450.0), 50)
                mycircle.draw(win3)
                e=5
            if j==6:
                mycircle=Circle(Point(550.0, 450.0), 50)
                mycircle.draw(win3)
                e=6
            if j==7:
                mycircle=Circle(Point(350.0, 550.0), 50)
                mycircle.draw(win3)
                e=7
            if j==8:
                mycircle=Circle(Point(450.0, 550.0), 50)
                mycircle.draw(win3)
                e=8
            if j==9:
                mycircle=Circle(Point(550.0, 550.0), 50)
                mycircle.draw(win3)
                e=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e):
            if j==1:
                mynewcircle=Circle(Point(350.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=1
            if j==2:
                mynewcircle=Circle(Point(450.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=2
            if j==3:
                mynewcircle=Circle(Point(550.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=3
            if j==4:
                mynewcircle=Circle(Point(350.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=4
            if j==5:
                mynewcircle=Circle(Point(450.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=5
            if j==6:
                mynewcircle=Circle(Point(550.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=6
            if j==7:
                mynewcircle=Circle(Point(350.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=7
            if j==8:
                mynewcircle=Circle(Point(450.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=8
            if j==9:
                mynewcircle=Circle(Point(550.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                f=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e or j==f):
            if j==1:
                mycircle=Circle(Point(350.0, 350.0), 50)
                mycircle.draw(win3)
                g=1
            if j==2:
                mycircle=Circle(Point(450.0, 350.0), 50)
                mycircle.draw(win3)
                g=2
            if j==3:
                mycircle=Circle(Point(550.0, 350.0), 50)
                mycircle.draw(win3)
                g=3
            if j==4:
                mycircle=Circle(Point(350.0, 450.0), 50)
                mycircle.draw(win3)
                g=4
            if j==5:
                mycircle=Circle(Point(450.0, 450.0), 50)
                mycircle.draw(win3)
                g=5
            if j==6:
                mycircle=Circle(Point(550.0, 450.0), 50)
                mycircle.draw(win3)
                g=6
            if j==7:
                mycircle=Circle(Point(350.0, 550.0), 50)
                mycircle.draw(win3)
                g=7
            if j==8:
                mycircle=Circle(Point(450.0, 550.0), 50)
                mycircle.draw(win3)
                g=8
            if j==9:
                mycircle=Circle(Point(550.0, 550.0), 50)
                mycircle.draw(win3)
                g=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e or j==f or j==g):
            if j==1:
                mynewcircle=Circle(Point(350.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=1
            if j==2:
                mynewcircle=Circle(Point(450.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=2
            if j==3:
                mynewcircle=Circle(Point(550.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=3
            if j==4:
                mynewcircle=Circle(Point(350.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=4
            if j==5:
                mynewcircle=Circle(Point(450.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=5
            if j==6:
                mynewcircle=Circle(Point(550.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=6
            if j==7:
                mynewcircle=Circle(Point(350.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=7
            if j==8:
                mynewcircle=Circle(Point(450.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=8
            if j==9:
                mynewcircle=Circle(Point(550.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                h=9
            valid=True
        else:
            print("This is an invalid move.")
            j=int(input())
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e or j==f or j==g or j==h):
            if j==1:
                mycircle=Circle(Point(350.0, 350.0), 50)
                mycircle.draw(win3)
                i=1
            if j==2:
                mycircle=Circle(Point(450.0, 350.0), 50)
                mycircle.draw(win3)
                i=2
            if j==3:
                mycircle=Circle(Point(550.0, 350.0), 50)
                mycircle.draw(win3)
                i=3
            if j==4:
                mycircle=Circle(Point(350.0, 450.0), 50)
                mycircle.draw(win3)
                i=4
            if j==5:
                mycircle=Circle(Point(450.0, 450.0), 50)
                mycircle.draw(win3)
                i=5
            if j==6:
                mycircle=Circle(Point(550.0, 450.0), 50)
                mycircle.draw(win3)
                i=6
            if j==7:
                mycircle=Circle(Point(350.0, 550.0), 50)
                mycircle.draw(win3)
                i=7
            if j==8:
                mycircle=Circle(Point(450.0, 550.0), 50)
                mycircle.draw(win3)
                i=8
            if j==9:
                mycircle=Circle(Point(550.0, 550.0), 50)
                mycircle.draw(win3)
                i=9
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
    print("Press any key to finish.")
    a=input()
else:
    print("Ok. See you later. Bye.")
