import random


def main():
    numbers = []
    while len(numbers) < 5:
        randomNum = random.randint(0,100)
        numbers.append(randomNum)

    

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
