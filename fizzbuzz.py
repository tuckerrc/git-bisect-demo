
def calc_fizz_buzz(number):
    if (number % 3 == 0 and number % 5 == 0 and number % 7 == 0):
        return "fizzbuzzfuzz"
    if (number % 3 == 0 and number % 7 == 0):
        return "fizzfuzz"
    if (number % 5 == 0 and number % 7 == 0):
        return "buzzfuzz"
    if (number % 3 == 0 and number % 5 == 0):
        return "fizzbuzz"
    if (number % 7 == 0):
        return "fuzz"
    if (number % 3 == 0):
        return "fizz"
    elif (number % 5 == 0):
        return "buzz"
    else:
        return str(number)


if __name__ == "__main__":
    for i in range(1, 110):
        print(calc_fizz_buzz(i))
