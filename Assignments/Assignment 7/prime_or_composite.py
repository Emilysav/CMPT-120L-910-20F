
def prime_or_composite(number):
    num1 = number - 1
    for i in range(2,num1):
        if number % i == 0:
            return False
    pass

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201, 47055833459]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)
    