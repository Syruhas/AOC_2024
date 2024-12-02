def parse_file(file_path:str) -> list[list[int]]:
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
        file_list = []
        for line in file_lines:
            file_list.append(list(map(int, line.split())))
    return file_list

def compute_numberofsaferows(row_list: list[list[int]]):
    counter = 0
    for row in row_list:
        counter += is_safe_row(row)
    return counter

def is_safe_row(row:list[int]):
    consecutive_diff = [ row[k+1] - row[k] for k in range(len(row)-1)]
    m, M = min(consecutive_diff), max(consecutive_diff)
    return (not m < 0 < M) and (abs(m)<=3) and (abs(M)<=3) and not(0 in consecutive_diff)


def test():
    row_list = parse_file("input_test.txt")
    #print(is_safe_row(row_list[0]))
    print(compute_numberofsaferows(row_list))

def main():
    row_list = parse_file("input.txt")
    print(compute_numberofsaferows(row_list))

if __name__=="__main__":
    #test()
    main()