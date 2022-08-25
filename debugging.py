def div(n):
    return [i for i in range(1, n+1) if n % i == 0]

def main():
    num = int(input("Enter a number: "))
    print(div(num))
    print('Program ended')

if __name__ == '__main__':
    main()
