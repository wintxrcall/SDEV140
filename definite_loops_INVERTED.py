# Author Renee Guldi	
# SDEV140 MPJovanovich
# This Python program is to be used to build a number pyramid
# based on a given height (integer) - INVERTED

    ## Prompt the user for input and return it as the correct data type.
def get_input() -> int:
        height = int(input("Enter the height of your pyramid: "))
        return height

def write_pyramid_row(row: int, height: int) -> None:
  
    # Print spaces before numbers
    for _ in range(height - row):
        print(" ", end=" ")

    # Print increasing numbers
    for num in range (1, row + 1):
         print(num, end=" ")
    # Print decreasing numbers (if there are any)
    for num in range (row - 1, 0, -1):
         print(num, end=" ")
    
    # this will push the next pyramid row to the next line
    print("\n")


def create_pyramid(height: int) -> None:
    # Loop through write_pyramid_row to create the full pyramid
    # to invert the pyramid, the order of iterations had
    # to be changed
    for row in range(height, 0, -1):
        write_pyramid_row(row, height)
        


if __name__ == "__main__":
    height = get_input()
    create_pyramid(height)