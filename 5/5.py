def parse_file(filepath:str):

    with open(filepath, "r") as f:
        lines = f.readlines()
        sep = lines.index("\n")
        rules = [line.strip() for line in lines[:sep]]
        pages = [[int(x) for x in line.strip().split(",")] for line in lines[sep+1:]]

        rules_as_dic = { }
        for entry in rules:
            first, second = list(map(int,entry.split("|")))
            if first in rules_as_dic:
                rules_as_dic[first].append(second)
            else:
                rules_as_dic[first] = [second]

        return (rules_as_dic, pages)


def check_page(rules, page):
    for index, element in enumerate(page[:-1]):
        for succ in page[index+1:]:
            # CHECK BETWEEN ELEMENT AND RULE
            if(element in rules.get(succ, [])):
                return 0
    return 1

def one():
    sum = 0
    rules_as_dic, pages = parse_file("input.txt")
    for page in pages:
        if check_page(rules_as_dic, page):
            sum += page[len(page)//2]

    return sum

if __name__=="__main__":
    print(one())