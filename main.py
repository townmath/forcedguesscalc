import pygame, sys
from pygame.locals import *

white = (0xFF, 0xFF, 0xFF)
black = (0,0,0)
kstfblue = (0, 0xA4, 0xDD)

def main():
    pygame.init()
    global CalculatorMain
    CalculatorMain = pygame.display.set_mode((200, 250))
    pygame.display.set_caption('Forced Guess Calculator V1.0')
    
    mousex, mousey = 0,0
    currentInput = 0
    isNumber = True
    fullNumberOld = ''
    fullNumberNew = ''
    operation = ''
    guess = False
    error = .1 #10%
    goodInput = True
    
    
    global calcNumberFont, calcWordFont
    calcNumberFont = pygame.font.SysFont('arial',36) #arial.ttf seems to work for idle, but just arial seems to work for pyinstaller, strange
    calcWordFont = pygame.font.SysFont('arial',24) 
    calcOutput = calcNumberFont.render('0.', True, black, white)
    calcRect = pygame.Rect(8,212,180,25)
    calcClear = calcNumberFont.render('                       ', True, black, white)
    zeroImg = calcNumberFont.render('0', True, white, kstfblue)
    oneImg = calcNumberFont.render('1', True, white, kstfblue)
    twoImg = calcNumberFont.render('2', True, white, kstfblue)
    threeImg = calcNumberFont.render('3', True, white, kstfblue)
    fourImg = calcNumberFont.render('4', True, white, kstfblue)
    fiveImg = calcNumberFont.render('5', True, white, kstfblue)
    sixImg = calcNumberFont.render('6', True, white, kstfblue)
    sevenImg = calcNumberFont.render('7', True, white, kstfblue)
    eightImg = calcNumberFont.render('8', True, white, kstfblue)
    nineImg = calcNumberFont.render('9', True, white, kstfblue)
    decimalImg = calcNumberFont.render('.', True, white, kstfblue)
    enterImg = calcWordFont.render('Enter', True, white, kstfblue)
    addImg = calcNumberFont.render('+', True, white, kstfblue)
    subtractImg = calcNumberFont.render('-', True, white, kstfblue)
    multiplyImg = calcNumberFont.render('x', True, white, kstfblue)
    divideImg = calcNumberFont.render('/', True, white, kstfblue)
    guessImg = calcWordFont.render('Guess', True, white, kstfblue)
    
    CalculatorMain.fill(kstfblue)
    # first row of calc
    CalculatorMain.blit(sevenImg,  (17,10))
    CalculatorMain.blit(eightImg, (67,10))
    CalculatorMain.blit(nineImg, (117,10))
    CalculatorMain.blit(addImg,  (167,10))
    # second row of calc
    CalculatorMain.blit(fourImg,       (17,60))
    CalculatorMain.blit(fiveImg,      (67,60))
    CalculatorMain.blit(sixImg,      (117,60))
    CalculatorMain.blit(subtractImg, (170,60))
    # third row of calc
    CalculatorMain.blit(oneImg,        (17,110))
    CalculatorMain.blit(twoImg,       (67,110))
    CalculatorMain.blit(threeImg,    (117,110))
    CalculatorMain.blit(multiplyImg, (167,110))
    # fourth row of calc
    CalculatorMain.blit(decimalImg,  (17,160))
    CalculatorMain.blit(zeroImg,    (67,160))
    CalculatorMain.blit(enterImg,  (100,165))
    CalculatorMain.blit(divideImg, (167,160))
    #fifth row of calc (output row)
    CalculatorMain.blit(calcOutput, calcRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                currentInput, isNumber = getButton(mousex,mousey)
                calcOutput, fullNumberOld, fullNumberNew, operation, guess = concatAndOperate(currentInput, isNumber, error, fullNumberOld, fullNumberNew, operation, guess)
            elif event.type == KEYDOWN:
#                if event.key 
                currentInput, isNumber, goodInput = getPress(event.key)
                if goodInput:
                    calcOutput, fullNumberOld, fullNumberNew, operation, guess = concatAndOperate(currentInput, isNumber, error, fullNumberOld, fullNumberNew, operation, guess)
#                print('old= ' + str(fullNumberOld))
#                print('op= ' + operation)
#                print('new= ' + fullNumberNew)
        CalculatorMain.blit(calcClear, calcRect)
        CalculatorMain.blit(calcOutput, calcRect)
        pygame.display.update()

def getButton(mousex, mousey):
    value = ''
    number = True
    if ((mousex>0)&(mousex<50)):
        if((mousey>=0)&(mousey<50)):
            value = '7'
            number = True
        elif ((mousey>=50)&(mousey<100)):
            value = '4'
            number = True
        elif ((mousey>=100)&(mousey<150)):
            value = '1'
            number = True
        elif ((mousey>=150)&(mousey<200)):
            value = '.'
            number = True
    elif ((mousex>=50)&(mousex<100)):
        if((mousey>=0)&(mousey<50)):
            value = '8'
            number = True
        elif ((mousey>=50)&(mousey<100)):
            value = '5'
            number = True
        elif ((mousey>=100)&(mousey<150)):
            value = '2'
            number = True
        elif ((mousey>=150)&(mousey<200)):
            value = '0'
            number = True
    elif ((mousex>=100)&(mousex<150)):
        if((mousey>=0)&(mousey<50)):
            value = '9'
            number = True
        elif ((mousey>=50)&(mousey<100)):
            value = '6'
            number = True
        elif ((mousey>=100)&(mousey<150)):
            value = '3'
            number = True
        elif ((mousey>=150)&(mousey<200)):
            value = 'Enter'
            number = False
    elif ((mousex>=150)&(mousex<200)):
        if((mousey>=0)&(mousey<50)):
            value = '+'
            number = False
        elif ((mousey>=50)&(mousey<100)):
            value = '-'
            number = False
        elif ((mousey>=100)&(mousey<150)):
            value = '*'
            number = False
        elif ((mousey>=150)&(mousey<200)):
            value = '/'
            number = False
    return (value, number)

def getPress (keypressed):
    value = ''
    number = True
    goodInput = True
    if keypressed == K_1:
        value = '1'
        number = True
    elif keypressed == K_2:
        value = '2'
        number = True
    elif keypressed == K_3:
        value = '3'
        number = True
    elif keypressed == K_4:
        value = '4'
        number = True
    elif keypressed == K_5:
        value = '5'
        number = True
    elif keypressed == K_6:
        value = '6'
        number = True
    elif keypressed == K_7:
        value = '7'
        number = True
    elif keypressed == K_8:
        value = '8'
        number = True
    elif keypressed == K_9:
        value = '9'
        number = True
    elif keypressed == K_0:
        value = '0'
        number = True
    elif keypressed == K_PLUS:
        value = '+'
        number = False
    elif keypressed == K_MINUS:
        value = '-'
        number = False
    elif keypressed == K_ASTERISK:
        value = '*'
        number = False
    elif keypressed == K_SLASH:
        value = '/'
        number = False
    elif keypressed == K_PERIOD:
        value = '.'
        number = False
    elif keypressed == K_RETURN:
        value = 'Enter'
        number = False
    elif keypressed == K_KP1:
        value = '1'
        number = True
    elif keypressed == K_KP2:
        value = '2'
        number = True
    elif keypressed == K_KP3:
        value = '3'
        number = True
    elif keypressed == K_KP4:
        value = '4'
        number = True
    elif keypressed == K_KP5:
        value = '5'
        number = True
    elif keypressed == K_KP6:
        value = '6'
        number = True
    elif keypressed == K_KP7:
        value = '7'
        number = True
    elif keypressed == K_KP8:
        value = '8'
        number = True
    elif keypressed == K_KP9:
        value = '9'
        number = True
    elif keypressed == K_KP0:
        value = '0'
        number = True
    elif keypressed == K_KP_PLUS:
        value = '+'
        number = False
    elif keypressed == K_KP_MINUS:
        value = '-'
        number = False
    elif keypressed == K_KP_MULTIPLY:
        value = '*'
        number = False
    elif keypressed == K_KP_DIVIDE:
        value = '/'
        number = False
    elif keypressed == K_KP_PERIOD:
        value = '.'
        number = False
    elif keypressed == K_KP_ENTER:
        value = 'Enter'
        number = False
    else:
        goodInput = False
    return (value, number, goodInput)

def concatAndOperate (value, number, error, OldNum, NewNum, operation, guess):
    if number:
        print NewNum, value
        NewNum = NewNum + value
        calcOutput = calcNumberFont.render(NewNum, True, black, white)
    elif (value == 'Enter'):
        if guess:
            if ((float(NewNum) <= OldNum*(1+error))&(float(NewNum) >= OldNum*(1-error))):
                calcOutput = calcNumberFont.render('Ans:' + str(OldNum), True, black, white)
                CalculatorMain.blit(calcWordFont.render('Enter  ', True, white, kstfblue),  (100,165))
                OldNum = ''
                NewNum = ''
                guess = False
            else:
                calcOutput = calcWordFont.render('Try Again', True, black, white)
                NewNum = ''
        else:
            guess = True
            text = 'Guess'
            if (operation == '+'):
                OldNum = float(OldNum) + float(NewNum)
            elif (operation == '-'):
                OldNum = float(OldNum) - float(NewNum)
            elif (operation == '*'):
                OldNum = float(OldNum) * float(NewNum)
            elif (operation == '/'):
                OldNum = float(OldNum) / float(NewNum)
            else:
                text = 'No Operation'
                guess = False
            if (text == 'Guess'):
                CalculatorMain.blit(calcWordFont.render(text, True, white, kstfblue),  (100,165))
            calcOutput = calcWordFont.render(text, True, black, white)
            NewNum = ''
            operation = ''
    else:
        operation = value
        OldNum = NewNum
        NewNum = ''
        calcOutput = calcNumberFont.render(operation, True, black, white)
    return (calcOutput,OldNum,NewNum,operation, guess)

main()
