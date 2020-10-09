# las_converter
## Python projects for well log analysis

### What is LAS file
**LAS** file contains physical properties data of vertical subsurface
used in well log analysis. Well log data saved in LAS file contains
some information, including its file **version**, **well description**,
**physical rock curve** along with data table and other information related
to the well data.

### Project feature(s)
- Load LAS data from various sources:
    - URL link (`https://example.com/.../.../path/to/lasfile.LAS`)
    - Local file (`path/to/lasfile.LAS` instead without `https`)
- Getting well log description.
- Save well log data into JSON file.

### Project dependencies
This project uses **Python 3** with dependencies provided in **requirements.txt**. 

### Project setup
Python environment setup is recommended for using this project repository. Type `./check-pyenv.sh` (using Linux/Unix terminal console or WSL console) for validating Python environments. By default, Python `virtualenv` has not been set yet so that it will be return results as below.

```sh
'env' directory is not exist.
 you can install Python virtualenv (and also activate it) by
 virtualenv env; source env/bin/activate 

 install Python dependencies then by
 pip install -r requirements.txt
```

In terminal, just type the yellow text given to proceed.

### Getting started
For the first time use, firstly import the external function by
```py
# import las_converter
import las_converter

# get help
help(las_converter)
```

or

```py
# import las_converter
from las_converter import WellLog

# get help
help(WellLog)
```

There is a file named `las_testing.py` used for testing purposes and can be used. There is also Jupyter Notebook file called `using_las_converter_in_well_log_analysis.ipynb` that also can be used in Jupyter console.

