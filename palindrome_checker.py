"""
Author: Logan Maupin
Date: 11/09/2022 (MM/DD/YYYY)

This is a simple program that checks if a given string is a palindrome.
A palindrome is a word that is spelled the same both forwards and backwards. For example, the
word "racecar", is a palindrome.
"""


def palindrome_test(string: str):

    lower_case_string = string.lower()

    if string:

        if not string.isalpha():
            print(f"{string.title()} is not acceptable. Please input a string without characters or digits.")
            return False

        else:

            # This is the part of the code that reverses the string.
            # After reversing the string, make sure it's the same as the original lower case enforced string.
            if lower_case_string[::-1] == lower_case_string:
                print(f"{string.title()} is a palindrome.")
                return True

            else:
                print(f"{string.title()} is not a palindrome.")
                return False

    else:
        print("String argument can not be empty. Please run this function again with a non empty string.")
        return False


def main():
    palindrome_test("")
    palindrome_test("Racecar123")
    palindrome_test("Test")
    palindrome_test("Racecar")


if __name__ == "__main__":
    main()
