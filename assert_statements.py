# assert 
def palindrome(word):
    assert len(word) > 0, "Empty string"
    return word == word[::-1]

def main():
    word = input("Enter a word: ").lower()
    print({True: "{} is a palindrome".format(word), False: "{} is not a palindrome".format(word)}[palindrome(word)])
    
if __name__ == '__main__':
    main()