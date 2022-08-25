# try, except, raise, finally
# raise Exception("Something went wrong")
from operator import le


def palindrome(word):
    try: 
        if len(word) == 0:
            raise ValueError("Empty string")
        return word == word[::-1]
    except ValueError as e:
        print(e)
        print("Program ended")
        return False
def main():
    try:
        word = input("Enter a word: ").lower()
        if palindrome(word):
            print("{} is a palindrome".format(word))
        else:
            print("{} is not a palindrome".format(word))
    except TypeError as e:
        print(e)
        print("Program ended")

if __name__ == '__main__':
    main()