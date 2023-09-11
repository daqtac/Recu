# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

def read_api_key(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

API_KEY = read_api_key('Sep5thStart/api_key.txt')

def read_model_engine(file_path):
    """Read Model_engine_file info and store it in a variable. This needs to be done, 
    otherwise in the next loop chatgpt will change it to a 2021 version of chatgpt 
    (since it is the "latest" from what it can tell, when in reality the external files have the latest version for it.)"""
    with open(file_path, 'r') as f:
        return f.read().strip()

MODEL_ENGINE = read_model_engine('Sep5thStart/model_engine.txt')

def import_instrucConst(file_path):
    "imports are less likely to be overwritten"

    with open(file_path, 'r') as f:
        return f.read().strip()

CONSTANT = import_instrucConst('Sep5thStart/instrucConstant.txt')


def read_dynamic_mem(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

DYNAMICMEMORY = read_api_key('Sep5thStart/DYNAMICMEMORY.txt')


