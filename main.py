
with open("input.txt", "rt") as inp:
    lines = inp.read().splitlines()

lista = [int(x) for x in lines ]

ttask = lista[0];
umax = lista[1];
users = lista[2:];



if 1<= ttask <= 10 or 1<= umax <= 10:
    tick = 0;
    servidores = [];
    text = '';
    cost = 0;

    while True:
      
        if servidores == []:
            for i in range(0, users[tick]):
                if i == 0:
                    servidores.append([ttask])
                else:
                    control = True
                    for k in servidores:
                        if len(k) < umax:
                            k.append(ttask)
                            control = False
                            break
                        else:
                            continue
                    
                    if control:
                        servidores.append([ttask])
                
        else:
            try:
                for i in range(0, users[tick]):
                    control = True
                    for k in servidores:
                        if len(k) < umax:
                            k.append(ttask)
                            control = False
                            break
                        else:
                            continue
                    
                    if control:
                        servidores.append([ttask])

            except IndexError:
                pass
        
        tick += 1

        count = 0;
        for i in servidores:
            t = len(i)
            count += 1
            
            

            if i == servidores[-1]:
                text = text + '{0}'.format(t)
            else:
                text = text + '{0}, '.format(t)
        cost = cost + count
        text = text + '\n'
        # print(servidores, tick)
        
        
        for i in servidores:
            for j in range(0, len(i)):
                i[j] = i[j] - 1

        for i in range(0, len(servidores)):
            servidores[i] = [x for x in servidores[i] if x != 0]
        
        servidores = [i for i in servidores if i != []]

        if servidores == []:
            text = text + '0 \n{0}'.format(cost) 
            break
        

    out =  open("Output.txt", "wt")
    out.write(text)
    out.close()
    

