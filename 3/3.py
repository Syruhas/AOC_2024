import re

def parse_file(filepath:str) ->list[str]:

    with open(filepath, "r") as file: 
        lines = file. readlines()
        file_content = ''. join(lines)
        matches = re.findall("mul\(\d+,\d+\)", file_content)

        return matches


def main() -> int:

    matches = parse_file("input.txt")
    total = 0

    for match in matches:
        digits = re.findall("\d+", match)
        total += int(digits[0])*int(digits[1])
    
    print(total)

def two(filepath:str) -> int:

    with open(filepath, "r") as file: 
        lines = file. readlines()
        text = ''. join(lines)

        text = re.sub("\n", "", text)
        text_split = re.split("don't\(\)", text)
        verified_content = [text_split[0]]

        for desactived_segment in text_split[1:]:
            re_activated_segment = re.split("do\(\)", desactived_segment, maxsplit=1)

            if(len(re_activated_segment)>1):
                verified_content.append(re_activated_segment[1])

        final_content = "".join(verified_content)
        matches = re.findall("mul\(\d+,\d+\)", final_content)
        
        total = 0
        for match in matches:
            digits = re.findall("\d+", match)
            total += int(digits[0])*int(digits[1])

        return total


if __name__=="__main__":
    print(two("input.txt"))