def parse_file(path:str)-> tuple[list, list]:
    list1, list2 = [], []
    with open(path, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            line_list = line.split()
            list1.append(int(line_list[0]))
            list2.append(int(line_list[1]))
    return list1, list2

def compute_distance(list1:list[int], list2:list[int]) -> int:
    list1.sort()
    list2.sort()
    total_distance = 0

    if(len(list1) != len(list2)):
        raise(ValueError("Lenght of list must be the same"))
    
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance


def compute_similarity_score(list1:list[int], list2:list[int]) -> int:
    number_of_occurence = {}
    similarity_score = 0

    for value in list1:
        if(number_of_occurence.get(value)):
            break
        number_of_occurence[value] = list2.count(value)

    for value in list1:
        similarity_score += value * number_of_occurence.get(value, 0)

    return similarity_score


def part_one():
    list1, list2 = parse_file("input.txt")
    print(list1)
    print(list2)

    total_dist = compute_distance(list1, list2)
    print(total_dist)

def part_two():
    list1, list2 = parse_file("input.txt")
    print(list1)
    print(list2)

    sim_score = compute_similarity_score(list1, list2)
    print(sim_score)


if __name__=="__main__":
    part_two()