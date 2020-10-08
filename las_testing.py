
# importing las_converter
import las_converter
## from las_converter import WellLog

# # init'd well log instance
# ## based on file input
# log1 = las_converter.WellLog("/home/dimaswehhh/Downloads/well log data/WA1.LAS")

# # get LAS data description
# ## it will describe well data section
# ## for null arguments
# log1.get_description()

# ## display specific description for well information
# log1.get_description("well_information")

# let's try with another well instance ...
log2 = las_converter.WellLog("https://certmapper.cr.usgs.gov/data/PubArchives/of00-200/wells/WALAKPA2/LAS/WA2.LAS")
# log2 = las_converter.WellLog("/home/dimaswehhh/Downloads/WA2.LAS")

# ... and also display well 2 information
log2.get_description()
log2.get_description("well_information")

# let's test for saving well 2
## in JSON
# log2.save_file("json")