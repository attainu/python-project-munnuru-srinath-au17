from input_file_content import InputFile
from back_tracking import BackTracking
from output_file_content import OutputFile
import sys
menu = \
"****************************************\n\
*                                      *\n\
*      WELCOME TO MAZE SOLVER          *\n\
*                                      *\n\
****************************************"

def display_output(output):
    print("The output is written in to output file\nIf you want to display output type 'YES'\nTo exit type 'NO'")
    string = input()
    if string == "YES":
        if type(output) == list:
            for i in output:
                for j in i:
                    print(str(j) + " ", end="")
                print("")
        else:
            print("No path")
    else:
        return False


if __name__ == "__main__":
    print(menu)
    args = sys.argv
    rows = InputFile(args)
    rows = rows.rows()
    if rows == 0:
        exit
    else:
        maze = InputFile(args)
        maze = maze.file_content()
        solve = BackTracking(rows)
        output = solve.solveMaze(maze)
        output_maze = OutputFile(args, output)
        output_maze.write_output()
        if display_output(output) is False:
            exit
