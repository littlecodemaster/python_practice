from random import choice, randrange
print("Welcome to the elections game! Do you have 1 or 2 players? (Please say '1' or '2'.)")
a=int(input())
state_map={'Alaska':3, 'Washington':12, 'Oregon':7, 'California':55, 'Hawaii':4, 'Idaho':4, 'Nevada':6, 'Utah':6, 'Arizona':11, 'Montana':3, 'Wyoming':3, 'Colorado':9, 'New Mexico':5, 'North Dakota':3, 'South Dakota':3, 'Nebraska':5, 'Kansas':6, 'Oklahoma':7, 'Texas':38, 'Minnesota':10, 'Iowa':6, 'Missouri':10, 'Arkansas':6, 'Louisiana':8, 'Wisconsin':10, 'Michigan':16, 'Illinois':20, 'Indiana':11, 'Kentucky':8, 'Tennessee':11, 'Mississippi':6, 'Alabama':9, 'Ohio':18, 'West Virginia':5, 'Virginia':13, 'North Carolina':15, 'South Carolina':9, 'Georgia':16, 'Florida':29, 'Maine':4, 'Vermont':3, 'New Hamshire':4, 'Massachusetts':11, 'Connecticut':7, 'Rhode Island':4, 'New York':29, 'Pennsylvania':20, 'New Jersey':14, 'Delaware':3, 'Maryland':10, 'Washington D.C.':3}
state_list=['Alaska', 'Washington', 'Oregon', 'California', 'Hawaii', 'Idaho', 'Nevada', 'Utah', 'Arizona', 'Montana', 'Wyoming', 'Colorado', 'New Mexico', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Oklahoma', 'Texas', 'Minnesota', 'Iowa', 'Missouri', 'Arkansas', 'Louisiana', 'Wisconsin', 'Michigan', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Mississippi', 'Alabama', 'Ohio', 'West Virginia', 'Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Maine', 'Vermont', 'New Hamshire', 'Massachusetts', 'Connecticut', 'Rhode Island', 'New York', 'Pennsylvania', 'New Jersey', 'Delaware', 'Maryland', 'Washington D.C.']
wrong=True
while wrong:
    if a==1 or a==2:
        wrong=False
    else:
        print("Could you please say how many players you have again? ('1' or '2')")
        a=int(input())
if a==1:
    a=(randrange(2))+1
    b=0
    c=0
    print("Then I will play against you. You will be team 1 and I will be team 2. Team", a, "will play first.")
    if a==1:
        while len(state_map)>1:
            wrong=True
            while wrong:
                print("Please enter one of the following for team 1:", state_list)
                input_state=input()
                if input_state in state_map.keys():
                    b=b+(state_map.get(input_state))
                    print("Team 1 now has", b, "electoral votes.")
                    state_list.remove(input_state)
                    state_map.pop(input_state, None)
                    wrong=False
                else:
                    print("This is not the name of one of the remaining states.")
            input_state=choice(state_list)
            c=c+(state_map.get(input_state))
            print("Team 2 now has", c, "electoral votes because team 2 picked", input_state, end="")
            print(".")
            state_list.remove(input_state)
            state_map.pop(input_state, None)
        wrong=True
        while wrong:
            print("Please enter one of the following for team 1:", state_list)
            input_state=input()
            if input_state in state_map.keys():
                b=b+(state_map.get(input_state))
                print("Team 1 now has", b, "electoral votes.")
                state_list.remove(input_state)
                state_map.pop(input_state, None)
                wrong=False
            else:
                print("This is not the name of one of the remaining states.")
    elif a==2:
        input_state=choice(state_list)
        c=c+(state_map.get(input_state))
        print("Team 2 now has", c, "electoral votes because team 2 picked", input_state, end="")
        print(".")
        state_list.remove(input_state)
        state_map.pop(input_state, None)
        while len(state_map)>1:
            wrong=True
            while wrong:
                print("Please enter one of the following for team 1:", state_list)
                input_state=input()
                if input_state in state_map.keys():
                    b=b+(state_map.get(input_state))
                    print("Team 1 now has", b, "electoral votes.")
                    state_list.remove(input_state)
                    state_map.pop(input_state, None)
                    wrong=False
                else:
                    print("This is not the name of one of the remaining states.")
            input_state=choice(state_list)
            c=c+(state_map.get(input_state))
            print("Team 2 now has", c, "electoral votes because team 2 picked", input_state, end="")
            print(".")
            state_list.remove(input_state)
            state_map.pop(input_state, None)
    print("Team 1 has", b, "electoral votes and team 2 has", c, "votes in the end.")
    if b==c:
        print("This means that both teams tie. The House of Representatives have to decide now!")
    elif b>c:
        print("This means that team 1 wins!")
    else:
        print("This means that team 2 wins!")
elif a==2:
    print("The first team will be team 1 and the second team will be team 2.")
    a=0
    b=0
    while len(state_map)>1:
        wrong=True
        while wrong:
            print("Please enter one of the following for team 1:", state_list)
            input_state=input()
            if input_state in state_map.keys():
                a=a+(state_map.get(input_state))
                print("Team 1 now has", a, "electoral votes.")
                state_list.remove(input_state)
                state_map.pop(input_state, None)
                wrong=False
            else:
                print("This is not the name of one of the remaining states.")
        wrong=True
        while wrong:
            print("Please enter one of the following for team 1:", state_list)
            input_state=input()
            if input_state in state_map.keys():
                b=b+(state_map.get(input_state))
                print("Team 2 now has", b, "electoral votes.")
                state_list.remove(input_state)
                state_map.pop(input_state, None)
                wrong=False
            else:
                print("This is not the name of one of the remaining states.")
    wrong=True
    while wrong:
        print("Please enter one of the following for team 1:", state_list)
        input_state=input()
        if input_state in state_map.keys():
            a=a+(state_map.get(input_state))
            print("Team 1 now has", a, "electoral votes.")
            state_list.remove(input_state)
            state_map.pop(input_state, None)
            wrong=False
        else:
            print("This is not the name of one of the remaining states.")
    print("Team 1 has", a, "electoral votes and team 2 has", b, "electoral votes in the end.")
    if a==b:
        print("This means that both teams tie. The House of Representatives have to decide now!")
    elif a>b:
        print("This means that team 1 wins!")
    else:
        print("This means that team 2 wins!")
