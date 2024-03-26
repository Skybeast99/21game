def determine_section(x1, x2, y1, y2) -> str:
    x = set()
    y = set()

    if x1 < x2:
        for i in range(x1, x2 + 1, 1):
            x.add(i)   
    elif x1 > x2:
        for i in range(x1, x2 + 1, -1):
            x.add(i)
    else:
        x.add(x1)
    

    if y1 < y2:
        for m in range(y1, y2 + 1, 1):
            y.add(m)
    elif y1 > y2:    
        for m in range(y1, y2 + 1, -1):
            y.add(m)
    else:
        y.add(y2)


    if y.intersection(x):
        return 'да'
    else:
        return 'нет'
    

print(determine_section(7, 9, 10, 15))

