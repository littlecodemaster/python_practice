from graphics import *
def check_if_win(number_list, whiteorblack):
    possibilities_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    number_list.sort()
    for possible in possibilities_list:
        if number_list==possible:
            print(whiteorblack, "wins. Thanks for playing! Press any key to finish.")
            y=input()
            sys.exit(0)
def first_turn(a, b, c, d, e, f, g, h):
    if a==0:
        print("Then let's play!")
    else:
        print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e or j==f or j==g or j==h):
            if j==1:
                mycircle=Circle(Point(350.0, 350.0), 50)
                mycircle.draw(win3)
                white_list.append(1)
            if j==2:
                mycircle=Circle(Point(450.0, 350.0), 50)
                mycircle.draw(win3)
                white_list.append(2)
            if j==3:
                mycircle=Circle(Point(550.0, 350.0), 50)
                mycircle.draw(win3)
                white_list.append(3)
            if j==4:
                mycircle=Circle(Point(350.0, 450.0), 50)
                mycircle.draw(win3)
                white_list.append(4)
            if j==5:
                mycircle=Circle(Point(450.0, 450.0), 50)
                mycircle.draw(win3)
                white_list.append(5)
            if j==6:
                mycircle=Circle(Point(550.0, 450.0), 50)
                mycircle.draw(win3)
                white_list.append(6)
            if j==7:
                mycircle=Circle(Point(350.0, 550.0), 50)
                mycircle.draw(win3)
                white_list.append(7)
            if j==8:
                mycircle=Circle(Point(450.0, 550.0), 50)
                mycircle.draw(win3)
                white_list.append(8)
            if j==9:
                mycircle=Circle(Point(550.0, 550.0), 50)
                mycircle.draw(win3)
                white_list.append(9)
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())

def second_turn(a, b, c, d, e, f, g):
    print("Next turn.")
    j=int(input())
    valid=False
    while not valid:
        if not (j==a or j==b or j==c or j==d or j==e or j==f or j==g):
            if j==1:
                mynewcircle=Circle(Point(350.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(1)
            if j==2:
                mynewcircle=Circle(Point(450.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(2)
            if j==3:
                mynewcircle=Circle(Point(550.0, 350.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(3)
            if j==4:
                mynewcircle=Circle(Point(350.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(4)
            if j==5:
                mynewcircle=Circle(Point(450.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(5)
            if j==6:
                mynewcircle=Circle(Point(550.0, 450.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(6)
            if j==7:
                mynewcircle=Circle(Point(350.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(7)
            if j==8:
                mynewcircle=Circle(Point(450.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(8)
            if j==9:
                mynewcircle=Circle(Point(550.0, 550.0), 50)
                mynewcircle.setFill('black')
                mynewcircle.draw(win3)
                black_list.append(9)
            valid=True
        else:
            print("This is an invalid move. Try again.")
            j=int(input())
print("Do you two want to play a tic tac toc game on this computer?")
if input()=="yes" or input()=="Yes":
    white_list=[]
    black_list=[]
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
    a=b=c=d=e=f=g=h=0
    first_turn(a, b, c, d, e, f, g, h)
    a=white_list[0]
    second_turn(a, b, c, d, e, f, g)
    b=black_list[0]
    first_turn(a, b, c, d, e, f, g, h)
    c=white_list[1]
    second_turn(a, b, c, d, e, f, g)
    d=black_list[1]
    first_turn(a, b, c, d, e, f, g, h)
    e=white_list[2]
    check_if_win([a, c, e], 'White')
    second_turn(a, b, c, d, e, f, g)
    f=black_list[2]
    check_if_win([b, d, f], 'Black')
    first_turn(a, b, c, d, e, f, g, h)
    g=white_list[3]
    check_if_win([a, c, g], 'White')
    check_if_win([a, e, g], 'White')
    check_if_win([c, e, g], 'White')
    second_turn(a, b, c, d, e, f, g)
    h=black_list[3]
    check_if_win([b, d, h], 'Black')
    check_if_win([b, f, h], 'Black')
    check_if_win([d, f, h], 'Black')
    first_turn(a, b, c, d, e, f, g, h)
    i=white_list[4]
    check_if_win([a, c, i], 'White')
    check_if_win([a, e, i], 'White')
    check_if_win([a, g, i], 'White')
    check_if_win([c, e, i], 'White')
    check_if_win([c, g, i], 'White')
    check_if_win([e, g, i], 'White')
    print("It looks like it was a tie. Thanks for playing! Press any key to finish.")
    x=input()
else:
    print("Ok. See you later. Bye.")
