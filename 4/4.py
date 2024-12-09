def part_one():
    with open("input.txt", "r") as f:
        mat = f.readlines()
        n_line = len(mat)
        n_char = len(mat[-1])
        tot = 0

        for line in range(n_line):
            for pos in range(n_char):
                if mat[line][pos]=="X":
                    #print(mat[line][pos])
                    tot += find_xmas(line, pos, mat, n_line, n_char)
        
        print(tot)

def find_xmas(line:int, pos:int, mat: list[list[str]], n_line:int, n_char:int):

    count = 0
    #HORIZONTAL
    if(pos<n_char-4) and ("".join(mat[line][pos:pos+4])=="XMAS"):
        count += 1

    if(pos>=3) and ("".join(mat[line][pos-3:pos+1])=="SAMX"):
        count += 1
    
    #VERTICAL
    if(line<=n_line-4) and ("".join([mat[line+i][pos] for i in range(4)])=="XMAS"):
        count += 1
    
    if(line>=3) and ("".join([mat[line-i][pos] for i in range(4)])=="XMAS"):
        count += 1
    ##DIAG
    ##down right
    if(line<=n_line-4 and pos<=n_char-4) and ("".join([mat[line+i][pos+i] for i in range(4)])=="XMAS"):
        count += 1
    ##down left
    if(line<=n_line-4 and pos>=3) and ("".join([mat[line+i][pos-i] for i in range(4)])=="XMAS"):
        count += 1
    
    #up right
    if(line>=3 and pos<=n_char-4) and ("".join([mat[line-i][pos+i] for i in range(4)])=="XMAS"):
        count += 1
    
    #up left
    if(line>=3 and pos>=3) and ("".join([mat[line-i][pos-i] for i in range(4)])=="XMAS"):
        count += 1
    
    return count
    

def part_two():
    with open("input.txt", "r") as f:
        mat = f.readlines()
        n_line = len(mat)
        n_char = len(mat[-1])
        tot = 0

        for line in range(1,n_line-1):
            for pos in range(1,n_char-1):
                if mat[line][pos]=="A":
                    tot += find_xmas2(line, pos, mat, n_line, n_char)
        print(tot)
    
def find_xmas2(line, pos, mat, n_line, n_char):

    diag1 = "".join([mat[line-1+i][pos-1+i] for i in range(3)])
    diag2 = "".join([mat[line+1-i][pos-1+i] for i in range(3)])

    if( (diag1=="MAS" or diag1=="SAM") and (diag2=="MAS" or diag2=="SAM")):
        return 1
    return 0

if __name__=="__main__":
    part_two()