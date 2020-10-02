import numpy as np

class WellLog():
    """
    WellLog class
    representation of well log database
log1 = WellLog("/home/dimaswehhh/Downloads/well log data/TU1.LAS")
# log1 = WellLog("/home/dimaswehhh/Downloads/well log data/1045139086.las")

# print(log1.info)
# print(log1.info["data_table"].keys())
# print(log1.info["data_table"])
    params:
    - file : str
      specifies file inputted for process well log data
      LAS file needed
    """
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
        self.load_data()
        
    def load_data(self):
        """
        Load data from LAS file
        """
        for i in self.file:
            if (i[0] == "~"):
                las_section = (i[1:-1].lower().replace(" ", "_") 
                                    if "~a" not in i.lower()
                                    else "data_table")
                self.info[las_section] = {}
            else:
                section = list(self.info)
                if (i[0] != "#"):
                    if (section[-1] != "data_table"):
                        one_spaced_line = " ".join(i.split())
                        one_spaced_line_splitted_colon = one_spaced_line.split(":")

                        # define informations properties as key-value pair
                        prop_pattern = [j.strip()
                                            for j in one_spaced_line_splitted_colon[0]
                                            .split(" ", 1)]

                        prop_pattern[1] = (float(prop_pattern[1])
                                            if prop_pattern[1].isnumeric() == True
                                            else prop_pattern[1])

                        self.info[section[-1]][prop_pattern[0].lower()] = prop_pattern[1]

                    else:
                        if (self.info["data_table"] == {}):
                            well_specs =  self.info[
                                [k for k in section if "curve_info" in k][0]
                            ]
                            well_specs_list = list(well_specs)

                            self.info[[k for k in section if "curve_info" in k][0]] = well_specs_list
                            well_specs = well_specs_list

                            # init'd empty space for each curve property
                            for j in well_specs_list:
                                self.info["data_table"][j] = np.array([])

                        data_ranges = np.array([j for j in " ".join(i.split()).split(" ")]).astype("float64")
                        # print(data_ranges)
                        
                        for j in range(len(well_specs_list)):
                            self.info["data_table"][
                                well_specs_list[j]
                                ] = np.append(self.info["data_table"][well_specs_list[j]],
                                              data_ranges[j])

                            # print(well_specs_list[j],
                            #       self.info["data_table"][well_specs_list[j]].dtype,
                            #       self.info["data_table"][well_specs_list[j]])

# log1 = WellLog("/home/dimaswehhh/Downloads/well log data/TU1.LAS")
# log1 = WellLog("/home/dimaswehhh/Downloads/well log data/1045139086.las")

# print(log1.info)
# print(log1.info["data_table"].keys())
# print(log1.info["data_table"])
# print(log1.info["data_table"]["m__depth.ft"])