class ZeroDenominatorError(Exception):
    pass


while True:

    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        if b == 0:
            raise ZeroDenominatorError()
    except ValueError:
        print("Numerator and denominator must be integers!")
    else:
        print("executed if there are no exceptions.")
        # moved the print in try to else, since after checking for executions, it is going to be executed.
        print(a / b)

    finally:
        print("executed independent of whether exception is raised or not.")
