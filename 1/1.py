def parse_file(path:str)-> tuple[list, list]:
    list1, list2 = [], []
    with open(path, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_list = line.split()
            list1.append(int(line_list[0]))
            list2.append(int(line_list[1]))
    return list1, list2

def compute_distance(list1, list2):
    list1.sort()
    list2.sort()
    total_distance = 0

    if(len(list1) != len(list2)):
        raise(ValueError("Lenght of list must be the same"))
    
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance


if __name__=="__main__":
    list1, list2 = parse_file("input.txt")
    #print(list1)
    #print(list2)

    total_dist = compute_distance(list1, list2)
    print(total_dist)