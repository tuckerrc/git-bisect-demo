

def calc_fizz_buzz(number):
    output = ""
    if (number % 3 == 0):
        output += "fizz"
    if (number % 5 == 0):
        output += "buzz"
    if (number % 7 == 0):
        output += "fuzz"
    if (number % 11 == 0):
        output += "bizz"
    if (number % 13 == 0):
        output += "biff"
    if (output == ""):
        output = number
    return output


if __name__ == "__main__":
    for i in range(1, 25):
        print(calc_fizz_buzz(i))
