import random


def main():
    numbers = []
    while len(numbers) < 5:
        randomNum = random.randint(0,100)
        numbers.append(randomNum)
    total = 0
    for number in numbers:
        total += number
    

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
