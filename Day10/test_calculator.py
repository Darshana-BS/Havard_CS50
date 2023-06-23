from calculator_unitetests import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("code error 2")
    if square(3) != 9:
        print("code error 22")

if __name__ == "__main__":
    main()