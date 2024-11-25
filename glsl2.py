import pygame, numpy as np

from object_reader import objInterpreter

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = []
lines = set()


def vbo(points: list, edges: set):
    points = np.array(points, dtype = np.float32)
    temp = []
    for edge in edges:
        for point in edge:
            temp.append(point)
    set_points = np.array(temp, dtype = np.uint32)

    points_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, points_vbo)
    glBufferData(GL_ARRAY_BUFFER, points.nbytes, points, GL_STATIC_DRAW)

    set_points_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, set_points_vbo)
    glBufferData(GL_ARRAY_BUFFER, set_points.nbytes, set_points, GL_STATIC_DRAW)

    return points_vbo, set_points_vbo, len(set_points)


def Display_object(vertices_vbo: np.ndarray, idx_vbo: np.ndarray, idxlen: int):

    glBindBuffer(GL_ARRAY_BUFFER, vertices_vbo)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, None)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, idx_vbo)

    glDrawElements(GL_LINES, idxlen, GL_UNSIGNED_INT, None)
    glDisableClientState(GL_VERTEX_ARRAY)

def main():
    pygame.init()
    display = (800,600)
    clock = pygame.time.Clock()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    objInterpreter("test.obj", vertices, lines)
    vertices_vbo, idx_vbo, idxlen = vbo(vertices, lines)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Display_object(vertices_vbo, idx_vbo, idxlen)
        pygame.display.flip()
        print(f'FPS: {int(round(clock.get_fps(), 0))}')
        clock.tick(120)

main()