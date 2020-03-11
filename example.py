def check_add(a, b):
    """Returns true if addition is correct."""
    if a + b == 10:
        return True
    return False

if __name__ == "__main__":
    if check_add(5, 5):
        print("Calculation is correct")
    else:
        print("Calculation is incorrect")
