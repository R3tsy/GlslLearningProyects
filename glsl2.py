import pygame, time
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

obj = open("test.obj")

def OBJ(object):
    points = []
    edges = set()
    for line in object:
        if line[0]+line[1] in 'v ':
            newstr = ''
            for s in line:
                if s.isalnum() or s in ' .-':
                    newstr += s

            lst = newstr.split(' ')
            lst.pop(0)
            for i in range(len(lst)):
                lst[i] = float(lst[i])

            points.append(lst)

        if line[0] in 'f':
            temp = ''
            for l in line:
                if l.isnumeric() or l in ' /':
                    temp += l
                else:
                    temp += ''
            temp = temp.replace('//', ',')
            lst = temp.split(" ")
            lst.pop(0)

            verts = []
            for st in lst:
                verts = verts + [int(st.split(",")[0]) - 1]

            for p in range(len(verts)):
                v1 = verts[p]
                v2 = verts[(p + 1) % len(verts)]
                edge = tuple(sorted((v1, v2)))
                edges.add(edge)

        if line[0] in 'l':
            lst = []
            for n in line:
                if n.isnumeric():
                    lst.append(int(n) - 1)
            edge = tuple(sorted((lst[0], lst[1])))
            edges.add(edge)

    return points, edges

with open("test.obj") as obj_file:
    verticies, lines = OBJ(obj_file)

def robject():
    glBegin(GL_LINES)
    for line in lines:
        for vertex in line:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 3, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        robject()
        pygame.display.flip()
        pygame.time.wait(10)

main()