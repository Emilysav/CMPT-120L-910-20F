
 #   - Add code in the defined function to sum up the internal arrays. 
 # - Returning an array of the sums.
    
  #  - Your input will be a 2d array
    
   # - Output should be a 1d array
    
    #- If a sub array is empty the sum is 0
   

def sum_2d_array(two_d_array):
    ar = []
    for row in two_d_array:
        print(row)
        ar.append(sum(row))
    return ar


if __name__ == "__main__":
    two_d_array = [
        [2, 6, 7, 98, 3, 434, 2, 4, 2],
        [-12, 3, 454, 6778, 234, -999, 2543, -2323],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [],
        [1000000000000000],
        [1],
        [0]
        ]
    answers = sum_2d_array(two_d_array)
    
    print(answers)