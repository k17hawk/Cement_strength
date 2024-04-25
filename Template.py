import os
from pathlib import Path
import logging
from datetime import datetime



#time stamp for getting current time in each run 
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
#directory for storing log file
LOG_DIR = "logs"
#filname of the log file is based on current time stamp, which will generate unique file in each run
LOG_FILE_NAME = f"log_{TIMESTAMP}.log"

#create if not exist
os.makedirs(LOG_DIR, exist_ok=True)

#joing file path and filename
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

#loging for storing logs
logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="w",
                    format='[%(asctime)s] \t%(levelname)s \t%(lineno)d \t%(filename)s \t%(funcName)s() \t%(message)s',
                    level=logging.INFO
                    )

#parent package folder
package_name = 'strength'

#list of files we need. 
list_of_files = [
    ".github/workflows/.gitkeep", #for empty folder just create .gitkeep file so that it will stored in gitub
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py", 
    f"src/{package_name}/utility/__init__.py", #for common function like reading file ,creating folders
    f"src/{package_name}/config/__init__.py", #for wrting spark session 
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py", #define the object 
    f"src/{package_name}/constant.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    "configs/config.yaml",
    "tests/__init__.py",
    "tests/unit/__init__.py", #unit test
    "tests/integration/__init__.py", #integration test
    "dvc.yaml",             #for dvc pipeline
    "init_setup.sh",        #shell script for creation of environment
    "requiremets.txt",      #
    "requirements_dev.txt", #for creation of development steps
    "setup.py",             
    "setup.cfg",            #setup config
    "pyproject.toml",       #for python packages only
    "tox.ini",              #testing of project locally
    "research/trials.ipynb", #our jupyter trails test
]

#create these files
for filepath in list_of_files:
    filepath = Path(filepath)
    #since some files are created with no folder but some has folder
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating the directory: {filedir} for file :{filename}")

    #if file already present and have size then don't create it again
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,"w")as f:
            pass #creating an empty files
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"filename already exist:{filename}")

        