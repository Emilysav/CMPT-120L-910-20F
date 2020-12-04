import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reverse", help="This will reverse the order of the array")
parser.add_argument("number", help="This number will print from one to the number")
args = parser.parse_args()

def array_of_numbers(number):
    arr = []
    for index in range(number + 1):
       arr = sum(arr.append(index))

    return arr



