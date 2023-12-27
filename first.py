import os


def check_is_nb(str):
    """check if a number is an int or a float"""
    try:
        float(str)
        return True
    except ValueError:
        return False
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return False


def load():
    """Function that loads the data for theta 0+1"""
    path = 'thetas.txt'
    try:
        thetas = [0, 0]
        if os.path.exists(path):
            f = open(path, "r")
            content = f.read()

            # verif data
            data = content.split(',')
            if len(data) != 2:
                return None
            if (data[0] and check_is_nb(data[0])):
                thetas[0] = float(data[0])
            else:
                return None
            if (data[1] and check_is_nb(data[1])):
                thetas[1] = float(data[1])
            else:
                return None
        return thetas
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None


def main():
    """main function"""
    try:
        mileage = input('Mileage: ')
        if (not mileage.isnumeric()):
            raise AssertionError('Not a numeric value')
        mileage = int(mileage)
        thetas = load()
        if (thetas is None):
            print("Error in thethas file")
            return
        estimation = mileage * thetas[0] + thetas[1]
        print(f"For a mileage of {mileage} the price \
is estimated to be {estimation}")
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
    return


if __name__ == "__main__":
    main()
