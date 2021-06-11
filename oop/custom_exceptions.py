class ZeroDenominatorError(Exception):
    pass


while True:

    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        if b == 0:
            raise ZeroDenominatorError()
        print(a / b)
    except ValueError:
        print("Numerator and denominator must be integers!")
