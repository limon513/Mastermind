import random

basecolor = ['r','g','b','y','w','b']
targetcolor = []
codelength=4
tries = 10

def target_generator(): #generating random target
    for _ in range(4):
        targetcolor.append(random.choice(basecolor))
        
def checkinput(lst):
    n = len(lst) 
    resultstr=""
    inbase=True
    if n != codelength:
        resultstr=f"Input Should be of length {codelength}"
        inbase=False
        return resultstr,inbase
        
    for clr in lst:
        if clr  not in basecolor:
            inbase=False
            resultstr = f"Colors are no in base colors {basecolor}"
            return resultstr, inbase
        
    return resultstr, inbase
        
  
def user_guess():
    inputlist=[]
    while True:
        print('Make Your Guess Maintaining Above Rules :',end=' ')
        inp = input().split()
        msg, conf = checkinput(inp)
        if conf:
            inputlist=inp
            break
        else:
            print(msg)
    return inputlist

def game_check(usrlst):
    correctpos=0 
    incorrectpos=0
    tcpy = targetcolor.copy()
    for i in range(0,4):    #foor correct positions
        if usrlst[i]==tcpy[i]:
            correctpos+=1
            tcpy[i]='#'
            usrlst[i]='#'
    for i,col in enumerate(usrlst): # for incorrect positons
        for j,tclr  in enumerate(tcpy):
            if col==tclr and col!='#':
                incorrectpos+=1
                tcpy[j]='#'
                break
                
    return correctpos, incorrectpos




def game():
    target_generator() 
    correctpos,incorrectpos = 0,0
    print(f'{"#"*35} WELCOME TO MASTERMIND {"#"*35}')
    print('Game Rules : ')
    print(f'1 : Your Guess Should be of These {basecolor} Colors,')
    print(f'2 : Your Guess Should be of Length {codelength},')
    print(f'3 : You Will Get Total of {tries} Tries,')
    print('GOOD LUCK!')
    print(targetcolor)
    print('_'*100)
    end = False
    for i in range(0,10):
        print(f'You Have {tries-i} Tries Left')
        print(f'Correct Position = {correctpos} && Incorrect Position = {incorrectpos}')
        userchoice = user_guess()
        correctpos,incorrectpos = game_check(userchoice)
        if correctpos==codelength :
            end = True
            break
        
    if end:
        print(f'CONGRATULATIONS You Finished in {tries-i-1} Tries')
    else:
        print(f'YOU LOSE ! Better Do Next Time IT WAS {targetcolor}')
        
            

if __name__ == "__main__":
    game()