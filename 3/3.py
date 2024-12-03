import re

def parse_file(filepath:str):
    with open(filepath, "r") as file: 
        lines = file. readlines()
        file_content = ''. join(lines)

        matches = re.findall("mul\(\d+,\d+\)", file_content)
        return matches


def main():
    matches = parse_file("input.txt")
    total = 0
    for match in matches:
        digits = re.findall("\d+", match)
        total += int(digits[0])*int(digits[1])
    
    print(total)

if __name__=="__main__":
    main()