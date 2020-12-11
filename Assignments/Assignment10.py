import argparse
import logging 

parser = argparse.ArgumentParser()
parser.add_argument("-s", help = "This will help find the summnation", action = "store_true")
parser.add_argument("number", help= "This is the number imputed")  
args = parser.parse_args()

logger = logging.getLogger()
logging.basicConfig(level = logging.DEBUG, format = f'%(asctime)s %(levelname)s : %(message)s')

def notation(number):
    n = 0
    for index in range(number + 1):
        n += index
    return n

logging.warning(notation(int(args.number)))