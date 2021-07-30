import math


class InputFile:
    def __init__(self, args):
        self.args = args

    def rows(self):
        input_file_name = self.args[2]
        f = open(input_file_name, 'r')
        input_file_content = list(f.read())
        mdf_input_file_content = []
        for i in input_file_content:
            if i == '1' or i == '0':
                mdf_input_file_content.append(i)
        no_of_elements = len(mdf_input_file_content)
        rows = math.sqrt(no_of_elements)
        rows = float("{:.2f}".format(rows))
        if rows * rows == no_of_elements:
            rows = int(rows)
        else:
            print("Given file does not contain square matrix")
            return 0
        return rows

    def file_content(self):
        input_file_name = self.args[2]
        f = open(input_file_name, 'r')
        input_file_content = list(f.read())
        mdf_input_file_content = []
        for i in input_file_content:
            if i == '1' or i == '0':
                mdf_input_file_content.append(i)
        no_of_elements = len(mdf_input_file_content)
        rows = math.sqrt(no_of_elements)
        rows = float("{:.2f}".format(rows))
        if rows * rows == no_of_elements:
            rows = int(rows)
            coloumns = rows
        maze = [[0 for i in range(rows)] for j in range(coloumns)]
        k = 0
        for i in range(rows):
            for j in range(coloumns):
                maze[i][j] = int(mdf_input_file_content[k])
                k += 1
        return maze
