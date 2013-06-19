import pygame, sys
from pygame.locals import *

pygame.init()

CalculatorMain = pygame.display.set_mode((200, 250))
pygame.display.set_caption('Forced Guess Calculator V1.0')

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

    calcFont = pygame.font.Font('freesansbold.ttf',24)
    calcOutput = calcFont.render('0.', True, black, white)
    calcRect = pygame.Rect(10,212,180,25)

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
        pygame.display.update()
