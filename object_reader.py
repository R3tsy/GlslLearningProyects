def objInterpreter(model: str, points: list, edges: set):

    obj = open(model)

    for line in obj:
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
            if (line.split('/'))[1].isdigit():
                temp = temp.replace('/', ',')
            else:
                temp = temp.replace('//', ',')
            lst = temp.split(" ")
            lst.pop(0)

            verts = []
            for st in lst:
                verts = verts + [int(st.split(",")[0]) - 1]

            for p in range(len(verts)):
                v1 = verts[p]
                v2 = verts[(p + 1) % len(verts)]
                edges.add(tuple(sorted((v1, v2))))

        if line[0] in 'l':
            lst = []
            for n in line:
                if n.isnumeric():
                    lst.append(int(n) - 1)
            edge = tuple(sorted((lst[0], lst[1])))
            edges.add(edge)