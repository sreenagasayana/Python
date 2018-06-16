def HL ( size ):
    return " ---" * size + " \n"

def VL ( size ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += HL(size)
        board += VL(size)
    board += HL(size)
    return board

if __name__ == "__main__":
    size = int(input("What size game board do You want? "))
    print(gameboard(size))