import numpy as np

class WellLog():
    """
    WellLog
      description:
        Defines well log database with LAS file input.
     
      parameter input(s):
        - file (str)
            Specifies LAS file inputted for process well log data.
    """
    def __init__(self, file):
        """
        description:
          Initiate well log instance
        """
        self.file = open(file).readlines()
        self.info = {
            "description": {}
        }

        self.load_data()

        return
        
    def load_data(self):
        """
        load_data()
          description:
            Load data from LAS file.

          additional notes:
            The function will be executed by default
            when WellLog class is initiated.
        """
        for i in self.file:
            if (i[0] == "~"):
                las_section = (i[1:-1].lower().replace(" ", "_") 
                                    if "~a" not in i.lower()
                                    else "data_table")

                self.info["description"][las_section] = {}
                
                self.info[las_section] = {}

            else:
                section = list(self.info)
                if (i[0] != "#"):
                    if (section[-1] != "data_table"):
                        one_spaced_line = " ".join(i.split())
                        one_spaced_line_splitted_colon = one_spaced_line.split(":")
                        one_spaced_line_splitted_colon[1] = one_spaced_line_splitted_colon[1].strip()

                        # define informations properties
                        ## as key-value pair
                        prop_pattern = [j.strip()
                                            for j in one_spaced_line_splitted_colon[0]
                                            .split(" ", 1)]

                        prop_pattern[1] = (float(prop_pattern[1])
                                            if prop_pattern[1].isnumeric() == True
                                            else prop_pattern[1])

                        self.info[section[-1]][prop_pattern[0].lower()] = prop_pattern[1]

                        self.info["description"][section[-1]][prop_pattern[0].lower()] = one_spaced_line_splitted_colon[1]

                    else:
                        # fill the data table

                        # init'd the data table column
                        ## from curve information properties
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
                        
                        for j in range(len(well_specs_list)):
                            self.info["data_table"][
                                well_specs_list[j]
                                ] = np.append(self.info["data_table"][well_specs_list[j]],
                                              data_ranges[j])

        return
                        
    def get_description(self, section=None):
        """
        get_description:
        |-- description:
        |   - Get the loaded well log data description
        |
        |-- parameter input(s):
        |    - section (str)
        |        Get the well log information based on section input
        |        Return list of sections input provided if section is not given
        |        Default value = None
        |
        |-- output(s)
        |   - list of sections input provided (if section == None)
        |   - list of section properties based on section input given     
        """

        if (section == None):
            print("There are some well properties with description provided.")

            for i, j in self.info["description"].items():
                print("-", i)

        else:
            print("Describing well log information about '%s'" % (section))

            for i, j in self.info["description"][section].items():
                print("-", i, ":", j)

        return
