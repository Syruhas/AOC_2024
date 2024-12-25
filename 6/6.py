def parse_file(filepath:str):
    with open(filepath, "r") as f:
        lines = f.readlines()

    return lines



def one():
    field = parse_file("input.txt")
    dx = 0
    dy = -1
    ymax = len(field)
    xmax = len(field[0])

    visited = set()

    for index, line in enumerate(field):
        if "^" in line:
            print("found")
            y = index
            x = line.index("^")
            print(x,y)

    while True:
        #print(f'At x:{x}, y:{y}')
        if(x+dx>=xmax or y+dy>=ymax or x+dx<0 or y+dy<0):
            return len(visited)
        if(field[y+dy][x+dx]=="#"):
            # Rotate
            dx, dy = -dy, dx
        else:
            x = x+dx
            y = y+dy
            visited.add((x,y))

if __name__=="__main__":
    print(one())