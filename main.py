import pygame, sys

pygame.init()

CalculatorMain = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Forced Guess Calculator V1.0')

white = (0xFF, 0xFF, 0xFF)
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
