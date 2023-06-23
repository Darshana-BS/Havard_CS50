from calculator import square

# --------------------------------------------------------
#approach1
# def main():
#     test_square()

# def test_square():
#     if square(2) != 4:
#         print('Incorrect 2')
#     if square(3) != 9:
#         print('Incorrect 3')

# if __name__ == "__main__":
#     main()
# --------------------------------------------------------


# --------------------------------------------------------
#approach2 with  AssertionError error 
# def main():
#     test_square()

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9

# if __name__ == "__main__":
#     main()
# --------------------------------------------------------

# --------------------------------------------------------
#approach3 multiple try except
# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 suqare is wrong")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 square is wrong")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 square is wrong")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 square is wrong")

# if __name__ == "__main__":
#     main()
# --------------------------------------------------------

# --------------------------------------------------------
#approach4 user give input = int
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
# --------------------------------------------------------

# --------------------------------------------------------
#approach4 user inputs strings? = pending / assignment
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
# --------------------------------------------------------