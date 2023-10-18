import main


def sum_ev(numbers):


    return sum(num for num in numbers if num % 2 == 0)


if __name__ == '__main__':
    main.sum_ev([1,2,5])