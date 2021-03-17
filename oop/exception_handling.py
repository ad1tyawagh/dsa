# a = (apple))  # SyntaxError
# onetwo = '1' + 2  # TypeError
# a = 10 / 0  # ZeroDivisionError
# b  # NameError

while True:

    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the Denominator: "))
        print(a / b)
        break

    # except ValueError:
    #     print("Numerator and denominator should be integers.")
    #
    # except ZeroDivisionError:
    #     print("Division by 0")

    except (ValueError, ZeroDivisionError):
        print(
            "Use integer values in numerator and non-zero integer values in denominator."
        )

    # Default exception should be at the last.
    # except:
    #     print("Default exception")
