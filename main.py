import pygame, sys
from pygame.locals import *

white = (0xFF, 0xFF, 0xFF)
black = (0,0,0)

zeroImg = pygame.image.load('zero.png')
oneImg = pygame.image.load('one.png')
twoImg = pygame.image.load('two.png')
threeImg = pygame.image.load('three.png')
fourImg = pygame.image.load('four.png')
fiveImg = pygame.image.load('five.png')
sixImg = pygame.image.load('six.png')
sevenImg = pygame.image.load('seven.png')
eightImg = pygame.image.load('eight.png')
nineImg = pygame.image.load('nine.png')
decimalImg = pygame.image.load('decimal.png')
enterImg = pygame.image.load('enter.png')
addImg = pygame.image.load('add.png')
subtractImg = pygame.image.load('subtract.png')
multiplyImg = pygame.image.load('multiply.png')
divideImg = pygame.image.load('divide.png')

def main():
    pygame.init()
    CalculatorMain = pygame.display.set_mode((200, 250))
    pygame.display.set_caption('Forced Guess Calculator V1.0')
    
    mousex, mousey = 0,0
    currentInput = 0
    isNumber = True
    fullNumberOld = ''
    fullNumberNew = ''
    operation = ''
    
    
    global calcFont
    calcFont = pygame.font.Font('freesansbold.ttf',24)
    calcOutput = calcFont.render('0.', True, black, white)
    calcRect = pygame.Rect(10,212,180,25)
    calcClear = calcFont.render('                  ', True, black, white)

    CalculatorMain.fill(white)
    # first row of calc
    CalculatorMain.blit(sevenImg,  (0,0))
    CalculatorMain.blit(eightImg, (50,0))
    CalculatorMain.blit(nineImg, (100,0))
    CalculatorMain.blit(addImg,  (150,0))
    # second row of calc
    CalculatorMain.blit(fourImg,       (0,50))
    CalculatorMain.blit(fiveImg,      (50,50))
    CalculatorMain.blit(sixImg,      (100,50))
    CalculatorMain.blit(subtractImg, (150,50))
    # third row of calc
    CalculatorMain.blit(oneImg,        (0,100))
    CalculatorMain.blit(twoImg,       (50,100))
    CalculatorMain.blit(threeImg,    (100,100))
    CalculatorMain.blit(multiplyImg, (150,100))
    # fourth row of calc
    CalculatorMain.blit(decimalImg,  (0,150))
    CalculatorMain.blit(zeroImg,    (50,150))
    CalculatorMain.blit(enterImg,  (100,150))
    CalculatorMain.blit(divideImg, (150,150))
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
                calcOutput, fullNumberOld, fullNumberNew, operation = concatAndOperate(currentInput, isNumber, fullNumberOld, fullNumberNew, operation)
                print('old= ' + str(fullNumberOld))
                print('op= ' + operation)
                print('new= ' + fullNumberNew)
#            elif event.type == KEYDOWN:
#    	currentInput = getPress()
        CalculatorMain.blit(calcClear, calcRect)
        CalculatorMain.blit(calcOutput, calcRect)
        pygame.display.update()

def getButton(mousex, mousey):
    value = 0
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

def concatAndOperate (value, number, OldNum, NewNum, operation):
    if number:
        NewNum = NewNum + value
        calcOutput = calcFont.render(NewNum, True, black, white)
    elif (value == 'Enter'):
        if (operation == '+'):
            OldNum = float(OldNum) + float(NewNum)
        elif (operation == '-'):
            OldNum = float(OldNum) - float(NewNum)
        elif (operation == '*'):
            OldNum = float(OldNum) * float(NewNum)
        elif (operation == '/'):
            OldNum = float(OldNum) / float(NewNum)
        calcOutput = calcFont.render(str(OldNum), True, black, white)
        OldNum = ''
        NewNum = ''
        operation = ''    
    else:
        operation = value
        OldNum = NewNum
        NewNum = ''
        calcOutput = calcFont.render(operation, True, black, white)
    return (calcOutput,OldNum,NewNum,operation)

main()
