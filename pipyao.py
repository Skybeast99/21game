def determine_section(x1, x2, y1, y2):
    x = set()
    y = set()
    for i in range(x1, x2, 1):
        x.add(i)
    for m in range(y1, y2, 1):
        y.add(m)
    y.intersection(x)
    return

print(determine_section(1, 10, 5, 15))