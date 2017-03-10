def toDecimal(n):
    """Function that converts binary to decimal

    Args:
        n - number to be converted

    Returns:
        Binary converted to decimal
    """
    return int(str(n), 2)

def toBinary(n):
    """Function that converts decimal to binary

    Args:
        n - number to be converted

    Returns:
        Decimal converted to binary
    """
    return int(bin(n)[2:])


def main():
    decimal(n)
    binary(n)

if __name__ == '__main__':
    main()
