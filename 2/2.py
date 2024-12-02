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

    m,M = row[1]-row[0],row[1]-row[0] 
    for k in range(len(row)-1):
        diff = row[k+1] - row[k]

        if diff>M:
            M = diff

        if diff<m:
            m = diff
        
        if M*m<=0 or M>3 or m<-3:
            return (0,k)
    
    return (1,0)


def compute_numberofsaferows_2(row_list: list[list[int]]):
    counter = 0
    for row in row_list:
        counter += is_safe_row_2(row)
    return counter

def is_safe_row_2(row:list[int]):
    '''
    Now we have one wildcard that we can tolerate
    '''

    # Regular check
    safe = is_safe_row(row) 
    if safe[0]:
        return 1
    else:
        index = safe[1]
        row1 = row.copy()
        row2 = row.copy()
        row3 = row.copy()
        row1.pop(index)
        row2.pop(index+1)
        row3.pop(index-1)
        return (is_safe_row(row1)[0] or is_safe_row(row2)[0] or is_safe_row(row3)[0])
    

def test():
    row_list = parse_file("input_test.txt")
    #test_row = [1, 2, 5, 8, 9, 6, 10]
    #print(is_safe_row(test_row))
    print(compute_numberofsaferows_2(row_list))

def main():
    row_list = parse_file("input.txt")
    print(compute_numberofsaferows_2(row_list))


if __name__=="__main__":
    test()
    main()