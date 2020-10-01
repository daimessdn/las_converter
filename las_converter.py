"""
   LAS file converter
   convert LAS (CWLS Log ASCII Standard) file
   into more structured file that can be analyzed
   through data science.
"""

class WellLog():
    def __init__(self, file):
        self.file = open(file).readlines()
        self.info = {}
        
        # print([i[1:-1] for i in self.file if i[0] == "~"])
        
    def load_data(self):
        # sections = [
        #     "~version",
        #     "~well",
        #     "~curve",
        #     "~parameter",
        #     "~other",
        #     "~a"
        # ]

        # s = 0
        
        for i in self.file[:50]:
            if (i[0] == "~"):
                las_section = i[1:-1].lower() if "~a" not in i.lower() else "data table"
                self.info[las_section] = {}
            else:
                if (i[0] != "#"):
                    print(i[:-1])
                    print(" ".join(i.split()).split(":"))

log1 = WellLog("/home/dimaswehhh/Downloads/well log data/WA1.LAS")
# log1 = WellLog("/home/dimaswehhh/Downloads/well log data/1051326093.las")
log1.load_data()
# print(log1.info["version"])
print(log1.info)
print(list(log1.info))
