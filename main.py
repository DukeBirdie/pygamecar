import os, sys
import pygame
from pygame import surface
from pygame.locals import *
import time

(width, height) = (1920, 1080)
#(900, 700)
surface = pygame.display.set_mode((width, height))

#set title
pygame.display.set_caption("THIS TOOK 2 HOURS")

#fill background
background_color = (200, 200, 200)
surface.fill(background_color)

#color
color = (255, 0, 0)

#car drawing

#base lines
pygame.draw.line(surface, color, (width-600, height-350), (width-300, height-350), width=2)

#bumpers
pygame.draw.line(surface, color, (width-250, height-350), (width-175, height-350), width=2)
pygame.draw.line(surface, color, (width-725, height-350), (width-650, height-350), width=2)

#hubs
radius = 25
#from right to left
pygame.draw.circle(surface, color, (width-275, height-350), radius, width=2)
pygame.draw.circle(surface, color, (width-625, height-350), radius, width=2)

#hide lines
hidden_color = background_color
#from right to left in order, cubes that hide lines
pygame.draw.rect(surface, hidden_color, pygame.Rect(width-300, height-350, 50, 50))
pygame.draw.rect(surface, hidden_color, pygame.Rect(width-650, height-350, 50, 50))

#wheels
wheel_radius = 15
wheel_color = (255, 255, 255)
tread_radius = 20
tread_color = (0, 0, 0)
pygame.draw.circle(surface, wheel_color, (width-275, height-350), wheel_radius, width=0)
pygame.draw.circle(surface, wheel_color, (width-625, height-350), wheel_radius, width=0)
#tread of wheel
pygame.draw.circle(surface, tread_color, (width-275, height-350), tread_radius, width=5)
pygame.draw.circle(surface, tread_color, (width-625, height-350), tread_radius, width=5)

#upper body
#left to right starts with line off of bumper
#left side of the car
#shortest line
pygame.draw.line(surface, color, (width-725, height-350), (width-725, height-400), width=2)
#medium line
pygame.draw.line(surface, color, (width-725, height-400), (width-550, height-425), width=2)
#longest line
pygame.draw.line(surface, color, (width-550, height-425), (width-535, height-650), width=2)
#roof
pygame.draw.line(surface, color, (width-535, height-650), (width-350, height-650), width=2)
#right side of the car
#shortest line
pygame.draw.line(surface, color, (width-175, height-400), (width-175, height-350), width=2)
#medium line
pygame.draw.line(surface, color, (width-335, height-425), (width-175, height-400), width=2)
#longest line
pygame.draw.line(surface, color, (width-350, height-650), (width-335, height-425), width=2)

#windows
window_color = (0, 190, 210)
pygame.draw.polygon(surface, window_color, ((width-525, height-640), (width-445, height-640), (width-445, height-425), (width-537, height-425)), width=0)
pygame.draw.polygon(surface, window_color, ((width-357, height-640), (width-440, height-640), (width-440, height-425), (width-345, height-425)), width=0)

#handles
handle_color = (0, 0, 0)
pygame.draw.line(surface, handle_color, (width-480, height-400), (width-450, height-400), width=4)
pygame.draw.line(surface, handle_color, (width-440, height-400), (width-410, height-400), width=4)

#road
road_color = (0, 0, 0)
pygame.draw.line(surface, road_color, (width-1920, height-330), (width, height-330), width=4)



#flip function
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False






