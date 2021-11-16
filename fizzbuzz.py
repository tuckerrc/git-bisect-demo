

def calc_fizz_buzz(number):
    s = ""
    if (number % 3 == 0):
        s += "fizz"
    if (number % 5 == 0):
        s += "buzz"
    if (number % 7 == 0):
        s += "fuzz"
    if (number % 11 == 0):
        s += "bizz"
    if (number % 13 == 0):
        s += "biff"
    if (s == ""):
        s = number
    return s


if __name__ == "__main__":
    for i in range(1, 110):
        print(calc_fizz_buzz(i))
