"""
   LAS file converter
   convert LAS (CWLS Log ASCII Standard) file
   into more structured file that can be analyzed
   through data science.
"""
class WellLog():
    def __init__(self, file):
        """
        Initiation of well log instance
        exact one argument file: LAS file location
        example:
        - log1 = WellLog("file://WA1.LAS")
        """
        self.file = open(file).readlines()
        self.info = {}

        # print([i[1:-1] for i in self.file if i[0] == "~"])
        pass
        
    def load_data(self):
        """
        Load data from LAS file
        """
        for i in self.file[:50]:
            if (i[0] == "~"):
                las_section = i[1:-1].lower() if "~a" not in i.lower() else "data table"
                self.info[las_section] = {}
            else:
                section = list(log1.info)
                if (i[0] != "#"):
                    if (section[-1] != "data table"):
                        one_spaced_line = " ".join(i.split())
                        one_spaced_line_splitted_colon = one_spaced_line.split(":")
                        prop_pattern = [j.strip() for j in one_spaced_line_splitted_colon[0].split(" ", 1)]
                        print(prop_pattern)

                        self.info[section[-1]][prop_pattern[0]] = prop_pattern[1]
                    else:
                        print(" ".join(i.split()).split(" "))

# log1 = WellLog("/home/dimaswehhh/Downloads/well log data/WA1.LAS")
log1 = WellLog("/home/dimaswehhh/Downloads/well log data/1045139086.las")

log1.load_data()

print(log1.info)
print(list(log1.info))
