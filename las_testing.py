import las_converter

# init'd well log instance
## based on file input
log1 = las_converter.WellLog("/home/dimaswehhh/Downloads/well log data/WA1.LAS")

# get LAS data description
## it will describe well data section
## for null arguments
log1.get_description()

## display specific description for well information
log1.get_description("well_information")

# let's try with another well instance ...
log2 = las_converter.WellLog("/home/dimaswehhh/Downloads/well log data/1045139086.las")

# ... and also display well 2 information
log2.get_description()
log2.get_description("well_information")
