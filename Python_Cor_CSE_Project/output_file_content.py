class OutputFile():
    def __init__(self, args, output):
        self.args = args
        self.output = output

    def write_output(self):
        output_file_name = self.args[4]

        f = open(output_file_name, "w")
        if type(self.output) == list:
            for i in self.output:
                for j in i:
                    f.write(str(j))
                    f.write(" ")
                f.write("\n")
        else:
            f.write("-1")
