import pygame, threading
import numpy as np

from object_reader import objInterpreter

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = []
lines = set()

def Display_object():
    glBegin(GL_LINES)
    for line in lines:
        glVertex3fv(vertices[line[0]])
        glVertex3fv(vertices[line[1]])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    clock = pygame.time.Clock()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('OpenGL | Python')

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    objInterpreter("test.obj", vertices, lines)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Display_object()
        print(int(round(clock.get_fps(), 0)))
        pygame.display.flip()
        clock.tick(0)

main()